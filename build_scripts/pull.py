"""Pull notes from Dendron to Hugo."""

import datetime as dt
import logging
import re
import os
import os.path
import sys
from dataclasses import dataclass
from pathlib import Path

import arrow
import frontmatter
import yaml.parser
from dotenv import load_dotenv
from rich.logging import RichHandler

load_dotenv()

logging.basicConfig(
    level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)

#: stored by Dendron as integer timestamps
TIMESTAMP_FIELDS = ["created", "updated"]

#: How I prefer to store timestamps
TIMESTAMP_FORMAT = "YYYY-MM-DD HH:mm:ss"

VAULT_LINK_RE = re.compile(
    r"""(?<!`)  # I use backticks to indicate syntax of a link but not an actual link
            \[\[
                (?:
                    (?P<label> [^|\]]+)
                    \|
                )?
                (?P<fname> [^\]]+) 
            \]\]
        """,
    re.VERBOSE,
)


@dataclass
class Note:
    path: Path
    post: frontmatter.Post
    is_section: bool

    @classmethod
    def from_path(cls, path: Path, public_note_paths: list[Path]) -> "Note":
        post = frontmatter.loads(path.read_text(encoding="utf-8"))
        post["fname"] = path.stem
        post["description"] = post.metadata.pop("desc", "")

        for field in TIMESTAMP_FIELDS:
            timestamp = int(post.metadata[field])
            post[field] = arrow.get(timestamp).format(TIMESTAMP_FORMAT)

        return cls(path, post, has_descendants(path, public_note_paths))

    @property
    def fname(self) -> str:
        return self.path.stem

    @property
    def content_path(self) -> str:
        f_steps = self.fname.split(".")[1:]

        if self.is_section:
            filename = "_index.md"
        else:
            filename = f"{f_steps[-1]}.md"
            f_steps = f_steps[:-1]

        return "/".join(f_steps + [filename])

    @property
    def permalink(self) -> str:
        if self.is_section:
            suffix = "_index.md"
        else:
            suffix = ".md"

        return "/" + self.content_path.removesuffix(suffix)

    def __str__(self) -> str:
        return self.fname

    def __repr__(self) -> str:
        return f"Note('{self.fname}')"


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


def find_descendants(note_path: Path, candidates: list[Path]) -> list[str]:
    descendants = [
        candidate.stem
        for candidate in candidates
        if candidate != note_path and candidate.stem.startswith(note_path.stem + ".")
    ]
    descendants.sort()

    return descendants


def has_descendants(note_path: Path, candidates: list[Path]) -> bool:
    return len(find_descendants(note_path, candidates)) > 0


def pull_note(note: Note, link_for: dict[str, dict[str, str]]) -> None:
    logging.debug("Note: '%s'", note)
    links_found = 0
    links_applied = 0

    # replace Dendron-style links with Hugo-style links
    processed_content_lines = []
    in_code_block = False

    for line in note.post.content.splitlines():
        if line.startswith("```"):
            in_code_block = not in_code_block

        if in_code_block:
            processed_content_lines.append(line)
            continue

        for match in VAULT_LINK_RE.finditer(line):
            links_found += 1
            link = match.group("fname")
            label = match.group("label")

            if link in link_for:
                if not label:
                    label = link_for[link]["title"]

                ref_for_link = "/" + link_for[link]["ref"]
                partial = '{{< relref "' + ref_for_link + '" >}}'
                line = line.replace(match.group(0), f"[{label}]({partial})")
                links_applied += 1
            else:
                logging.warning(
                    "'%s' :: Link '%s' not found in '%s'", match.group(0), link, note
                )
        processed_content_lines.append(line)

    logging.debug(
        "'%s' :: links found: %s, links applied: %s", note, links_found, links_applied
    )

    note.post.content = "\n".join(processed_content_lines)
    content_path = Path(f"content/{note.content_path}")
    content_path.parent.mkdir(parents=True, exist_ok=True)
    content_path.write_text(frontmatter.dumps(note.post), encoding="utf-8")


def main():
    logging.info("Initializing...")
    dendron_root_dir = os.getenv("DENDRON_ROOT_DIR")
    hugo_site_dir = os.getenv("HUGO_SITE_DIR")

    assert dendron_root_dir, "DENDRON_ROOT_DIR not set"

    assert hugo_site_dir, "HUGO_SITE_DIR not set"

    vault_path = Path(dendron_root_dir).expanduser()
    notes_path = vault_path / "notes"
    public_note_paths = sorted(
        [note for note in notes_path.glob("*.md") if note.stem.startswith("pub")]
    )

    notes = []

    for note_path in public_note_paths:
        try:
            note = Note.from_path(note_path, public_note_paths)
            notes.append(note)
        except yaml.parser.ParserError as e:
            logging.error("Error parsing frontmatter in '%s': %s", note_path, e)
            sys.exit(1)

    link_for = {
        note.fname: {"title": note.post.metadata["title"], "ref": note.content_path}
        for note in notes
    }

    for note in notes:
        pull_note(note, link_for)

    vault_assets_path = notes_path / "assets"
    hugo_assets_path = Path("assets")

    for asset in vault_assets_path.glob("**/*"):
        if asset.is_file():
            asset_path = hugo_assets_path / asset.relative_to(notes_path)
            asset_path.parent.mkdir(parents=True, exist_ok=True)
            asset_path.write_bytes(asset.read_bytes())

    logging.info("public notes: %s", len(public_note_paths))
    logging.info("Done!")


if __name__ == "__main__":
    main()
