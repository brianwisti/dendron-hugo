"""Pull notes from Dendron to Hugo."""

import logging
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


@dataclass
class Note:
    path: Path
    is_section: bool

    @property
    def fname(self) -> str:
        return self.path.stem

    @property
    def content_path(self) -> str:
        filename = "index.md"

        if self.is_section:
            filename = "_index.md"

        return "/".join(self.fname.split(".")[1:] + [filename])

    def __str__(self) -> str:
        return self.fname

    def __repr__(self) -> str:
        return f"Note('{self.fname}')"


def find_descendants(note_path: Path, candidates: list[Path]) -> list[str]:
    descendants = [
        candidate.stem
        for candidate in candidates
        if candidate != note_path and candidate.stem.startswith(note_path.stem)
    ]
    descendants.sort()

    return descendants


def has_descendants(note_path: Path, candidates: list[Path]) -> bool:
    return len(find_descendants(note_path, candidates)) > 0


def main():
    logging.info("Initializing...")
    vault_path = Path("~/Documents/dendron-brain").expanduser()
    notes_path = vault_path / "notes"
    public_note_paths = [
        note for note in notes_path.glob("*.md") if note.stem.startswith("pub")
    ]

    for note_path in public_note_paths:
        note = Note(note_path, has_descendants(note_path, public_note_paths))
        post = frontmatter.loads(note_path.read_text(encoding="utf-8"))

        for field in TIMESTAMP_FIELDS:
            timestamp = int(post.metadata[field])
            post[field] = arrow.get(timestamp).format(TIMESTAMP_FORMAT)

        logging.info("Note: '%s'", note)
        logging.info("\tContent path: %s'", note.content_path)
        logging.info("\tcreated: %s", post["created"])
        logging.info("\tupdated: %s", post["updated"])

    logging.info("public notes: %s", len(public_note_paths))
    logging.info("Done!")


if __name__ == "__main__":
    main()
