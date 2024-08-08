"""Pull notes from Dendron to Hugo."""

import datetime as dt
import logging
import os
import os.path
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import arrow
import frontmatter
import rich
from dotenv import load_dotenv
from rich.logging import RichHandler
from sqlite_utils import Database
from sqlite_utils.db import NotFoundError, Table

load_dotenv()

logging.basicConfig(
    level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)

#: stored by Dendron as integer timestamps
TIMESTAMP_FIELDS = ["created", "updated"]

#: How I prefer to store timestamps
TIMESTAMP_FORMAT = "YYYY-MM-DD HH:mm:ss"


@dataclass
class Paths:
    """Holds the paths we want to remember."""

    #: Where to find the Hugo site.
    site: Path

    #: What Dendron workspace to pull from
    root: Path

    #: Which vault to pull
    vault: Path

    @classmethod
    def from_env(cls) -> "Paths":
        """Return Paths from environment variables."""
        root_dir = os.getenv("DENDRON_ROOT_DIR")
        vault_subdir = os.getenv("DENDRON_VAULT_SUBDIR")
        hugo_site_dir = os.getenv("HUGO_SITE_DIR")

        assert root_dir, "DENDRON_ROOT_DIR not set"
        assert vault_subdir, "DENDRON_VAULT_SUBDIR not set"
        assert hugo_site_dir, "HUGO_SITE_DIR not set"

        logging.info("Root: '%s'", root_dir)
        logging.info("Vault: '%s'", vault_subdir)
        logging.info("Hugo site: '%s'", hugo_site_dir)

        site_path = Path(hugo_site_dir).expanduser()
        root_path = Path(root_dir).expanduser()
        vault_path = root_path / vault_subdir

        if not site_path.exists():
            raise FileNotFoundError(f"Site path not found: '{site_path}'")

        if not root_path.exists():
            raise FileNotFoundError(f"Root path not found: '{root_path}'")

        if not vault_path.exists():
            raise FileNotFoundError(f"Vault path not found: '{vault_path}'")

        return cls(
            site=site_path,
            root=root_path,
            vault=vault_path,
        )

    @property
    def site_content(self) -> Path:
        """Return the content path."""
        return self.site / "content"


def main():
    """Pull notes from Dendron to Hugo"""
    try:
        paths = Paths.from_env()
    except FileNotFoundError as error:
        logging.error(error)
        return

    db = create_database()
    load_notes(db, paths)
    logging.info("Notes in db: %s", db["notes"].count)
    logging.info("Note files in db: %s", db["note_files"].count)
    reset_hugo_content(paths.site_content)
    write_notes_for_hugo(db, paths.site_content)
    summarize_data(db)


def reset_hugo_content(content_dir: Path) -> None:
    """Ensure a blank slate for content files in Hugo site."""
    logging.info("Cleaning %s", content_dir)
    shutil.rmtree(content_dir)
    content_dir.mkdir()


def create_database() -> Database:
    """Return in-memory database ready to load notes."""
    logging.info("Creating database")
    db = Database(memory=True)
    # db = Database("dendron.db", recreate=True)

    logging.info("Defining schema for 'notes'")
    db.create_table(
        "notes",
        {
            "id": str,
            "parent": str,
            "title": str,
            "desc": str,
            "updated": dt.datetime,
            "created": dt.datetime,
            "fname": str,
        },
        pk="fname",
    )

    logging.info("Defining schema for 'note_contents'")
    db.create_table(
        "note_files",
        {
            "fname": str,
            "content_path": str,
            "content": str,
        },
        pk="fname",
    )

    logging.info("Defining view for 'children'")
    db.create_view(
        "children",
        """
        SELECT
            parent.fname as parent_fname,
            child.fname as fname,
            child.title as title
        FROM
            notes child
        INNER JOIN notes parent
            on parent.fname = child.parent
        INNER JOIN note_files existing_file
            on existing_file.fname == child.fname
    """,
    )

    logging.info("Defining view for 'parents'")
    db.create_view(
        "parents",
        """
        SELECT
            parent.id as id,
            parent.fname as fname,
            parent.title as title,
            child.fname as child_fname
        FROM
            notes parent
        INNER JOIN notes child
            on parent.fname = child.parent
        INNER JOIN note_files existing_file
            on existing_file.fname == parent.fname
        """,
    )

    logging.info("Defining view for 'missing_parents'")
    db.create_view(
        "missing_parents",
        """
        SELECT
            distinct(parent) as parent
            from notes
        WHERE parent not in (
            SELECT distinct(id) FROM parents
        )
        """,
    )

    logging.info("Defining view for 'orphans'")
    db.create_view(
        "orphans",
        """
        SELECT
            fname,
            parent
        FROM notes
        WHERE parent in (
            SELECT PARENT from missing_parents
        )
        """,
    )

    return db


def load_notes(db: Database, paths: Paths) -> None:
    """Populate db with meta and content for vault notes."""
    logging.info("Loading notes from '%s'", paths.vault)
    load_note_contents_from_vault(db, paths.vault)
    # add_slugs_for_missing_parents(db)


def build_note_tree(fnames: list[str]) -> dict[str, str]:
    """Return a tree of notes from a list of fnames."""
    root_note = "root"
    tree = {}
    tree[root_note] = ""
    non_root_fnames = [fname for fname in fnames if fname != root_note]

    for current_fname in non_root_fnames:
        parent = root_note
        candidates = sorted(
            [
                fname
                for fname in fnames
                if fname != current_fname and current_fname.startswith(f"{fname}.")
            ]
        )

        if candidates:
            parent = candidates[-1]

        tree[current_fname] = parent

    return tree


def load_note_contents_from_vault(db: Database, vault_path: Path) -> None:
    """Populate db with note contents from Vault files."""
    logging.info("Loading note contents from '%s'", vault_path)
    notes = cast(Table, db["notes"])
    note_files = cast(Table, db["note_files"])

    note_paths = list(vault_path.glob("*.md"))
    fnames = [note_path.stem for note_path in note_paths]
    tree = build_note_tree(fnames)

    for note_path in vault_path.glob("*.md"):
        logging.debug("Note path: '%s'", note_path)
        fname = note_path.stem

        if fname.startswith("@"):
            rich.print(fname)

        # Might get fancier here if we map dendron heirarchy to folders.
        if fname == "root":
            content_path = "_index.md"
        else:
            content_path = Path(fname) / "index.md"

        post = frontmatter.loads(note_path.read_text(encoding="utf-8"))
        data = {
            "id": post["id"],
            "title": post["title"],
            "desc": post["desc"],
            "fname": fname,
            "parent": tree[fname],
        }

        for field in TIMESTAMP_FIELDS:
            timestamp = int(post[field])
            data[field] = arrow.get(timestamp).format(TIMESTAMP_FORMAT)

        notes.insert(data)
        note_files.insert(
            {
                "fname": fname,
                "content": post.content,
                "content_path": str(content_path),
            }
        )

    logging.info("Note contents count: %s", db["note_files"].count)


def add_slugs_for_missing_parents(db: Database) -> None:
    """Fake some notes for defined parents that haven't been created."""
    missing_parents = db["missing_parents"]
    root = get_root(db)
    notes = cast(Table, db["notes"])
    note_files = cast(Table, db["note_files"])

    for row in db["missing_parents"].rows:
        rich.print(row)
        parent_id = row["parent"]
        orphans = db["orphans"].rows_where("parent = ?", [parent_id])
        orphans = [o["fname"] for o in orphans]
        fname = os.path.commonprefix(orphans)
        rich.print(orphans)

        if fname.endswith("."):
            fname = fname[:-1]
        else:
            fname = ".".join(fname.split(".")[:-1])

        rich.print(fname)
        parent_path = Path(fname) / "index.md"
        notes.insert(
            {
                "id": parent_id,
                "parent": root["id"],
                "title": fname,
                "desc": "slug",
                "updated": arrow.get().format(TIMESTAMP_FORMAT),
                "created": arrow.get().format(TIMESTAMP_FORMAT),
                "fname": fname,
            }
        )
        note_files.insert(
            {"fname": fname, "content": "SLUG", "content_path": str(parent_path)}
        )

    rich.print(f"Missing parent count: {missing_parents.count}")


def write_notes_for_hugo(db: Database, content_path: Path) -> None:
    """Translate loaded notes data into content files on disk."""
    logging.info("Writing notes to '%s'", content_path)

    for note_file in db["note_files"].rows:
        fname = note_file["fname"]
        content = note_file["content"]
        note_path = content_path / note_file["content_path"]
        logging.debug("%s -> %s", fname, note_path)
        meta = prepare_note_meta(db, fname)
        post = frontmatter.Post(content, **meta)
        note_path.parent.mkdir(exist_ok=True, parents=True)
        note_path.write_text(frontmatter.dumps(post), encoding="utf-8")


def prepare_note_meta(db: Database, fname: str) -> dict[str, Any]:
    """Return dictionary to use as frontmatter for a note."""
    logging.debug("Preparing meta for '%s'", fname)
    notes = cast(Table, db["notes"])

    try:
        note = notes.get(fname)
    except NotFoundError:
        logging.error("Note '%s' not found in db", fname)
        sys.exit(1)

    meta = {
        "title": note["title"],
        "desc": note["desc"],
        "created": note["created"],
        "updated": note["updated"],
        "fname": note["fname"],
    }
    meta["children"] = [
        {"fname": child["fname"], "title": child["title"]}
        for child in db["children"].rows_where("parent_fname = ?", [fname])
    ]

    if parent := get_parent(db, fname):
        meta["parent"] = parent

    return meta


def summarize_data(db: Database) -> None:
    """Print out info on what I loaded."""
    rich.print(f'Notes count: {db["notes"].count}')
    rich.print(f'Note files counts: {db["note_files"].count}')


def get_parent(db: Database, fname: str) -> dict[str, Any]:
    """Return the one parent for a named note."""
    parents = list(db["parents"].rows_where("child_fname = ?", [fname]))

    if len(parents) > 1:
        raise ValueError(f"Too many parents for '{fname}': {parents}")

    if not parents:
        logging.warning("No parent for '%s'", fname)
        return {}

    parent = parents[0]

    return {
        "fname": parent["fname"],
        "title": parent["title"],
    }


def get_root(db: Database) -> dict[str, Any]:
    """Return data for our root note."""
    notes = cast(Table, db["notes"])
    return notes.get("root")


if __name__ == "__main__":
    main()
