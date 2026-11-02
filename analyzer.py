"""Deterministic boundary splitting and exact sample glossary lookup.

This module intentionally does not perform model based segmentation or tagging.
"""

import json
import unicodedata
from dataclasses import dataclass
from pathlib import Path


GLOSSARY_PATH = Path(__file__).with_name("glossary.json")


@dataclass(frozen=True)
class Token:
    text: str
    start: int  # Zero based character offset into the original input.
    end: int  # Exclusive character offset.
    kind: str
    definition: str | None


def load_glossary(path: Path = GLOSSARY_PATH) -> dict[str, str]:
    """Load the small, manually authored sample glossary."""
    with path.open(encoding="utf-8") as glossary_file:
        entries = json.load(glossary_file)
    if not isinstance(entries, dict) or any(
        not isinstance(word, str) or not isinstance(definition, str)
        for word, definition in entries.items()
    ):
        raise ValueError("The glossary must map text to definitions.")
    return entries


def _is_khmer(char: str) -> bool:
    return "\u1780" <= char <= "\u17ff"


def _is_boundary(char: str) -> bool:
    return char == "\u200b" or char.isspace() or unicodedata.category(char)[0] in "PS"


def analyze_text(text: str, glossary: dict[str, str]) -> list[Token]:
    """Split only at explicit boundaries and apply exact glossary lookup.

    Whitespace and zero width spaces delimit spans but are not returned. Unicode
    punctuation and symbols are returned separately so their offsets stay clear.
    """
    tokens: list[Token] = []
    start = 0

    def add_span(begin: int, end: int) -> None:
        if begin == end:
            return
        span = text[begin:end]
        kind = "Khmer span" if any(_is_khmer(char) for char in span) else "Other text"
        definition = glossary.get(span) if kind == "Khmer span" else None
        tokens.append(Token(span, begin, end, kind, definition))

    for index, char in enumerate(text):
        if not _is_boundary(char):
            continue
        add_span(start, index)
        if not char.isspace() and char != "\u200b":
            tokens.append(Token(char, index, index + 1, "Punctuation / symbol", None))
        start = index + 1

    add_span(start, len(text))
    return tokens
