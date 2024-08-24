"""Pull notes from Dendron to Hugo."""

import logging
import re
from dataclasses import dataclass
from pathlib import Path

import arrow
import frontmatter
from rich.logging import RichHandler

logging.basicConfig(
    level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)

#: stored by Dendron as integer timestamps
TIMESTAMP_FIELDS = ["created", "updated"]

#: How I prefer to store timestamps
TIMESTAMP_FORMAT = "YYYY-MM-DD HH:mm:ss"

VAULT_LINK_RE = re.compile(
    r"""\[\[ (?P<fname>[^\]]+) \]\]""",
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
    logging.info("Note: '%s'", note)
    # replace Dendron-style links with Hugo-style links
    content = note.post.content
    for match in VAULT_LINK_RE.finditer(content):
        link = match.group("fname")

        if link in link_for:
            title = link_for[link]["title"]
            ref_for_link = "/" + link_for[link]["ref"]
            partial = '{{< relref "' + ref_for_link + '" >}}'
            content = content.replace(
                match.group(0),
                f"[{title}]({partial})",
            )
        else:
            logging.warning("Link not found: %s", link)
            content = content.replace(match.group(0), f"*{link}*")

    note.post.content = content
    content_path = Path(f"content/{note.content_path}")
    content_path.parent.mkdir(parents=True, exist_ok=True)
    content_path.write_text(frontmatter.dumps(note.post), encoding="utf-8")


def main():
    logging.info("Initializing...")
    vault_path = Path("~/Documents/dendron-brain").expanduser()
    notes_path = vault_path / "notes"
    public_note_paths = sorted(
        [note for note in notes_path.glob("*.md") if note.stem.startswith("pub")]
    )
    notes = [Note.from_path(note, public_note_paths) for note in public_note_paths]
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
