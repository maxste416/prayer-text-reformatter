"""Core text formatting logic for prayer entries."""

from __future__ import annotations

from typing import Iterable


def reformat_prayer_text(text: str) -> str:
    """Return a reformatted version of *text* following the specified layout.

    The expected input format is a header line containing a date followed by a
    colon, the location/title segment, and any number of paragraphs separated by
    blank lines. The first paragraph remains unbulleted, while subsequent
    paragraphs are turned into bulleted lines that are separated by blank lines.
    """

    lines = _normalize_newlines(text).split("\n")
    header, remainder = _extract_header(lines)
    paragraphs = _collect_paragraphs(remainder)
    if not paragraphs:
        return header

    body = []
    body.append(paragraphs[0])

    for paragraph in paragraphs[1:]:
        body.append(f"- {paragraph}")

    return "\n\n".join([header, *body])


def _normalize_newlines(text: str) -> str:
    """Normalize CRLF line endings to LF to simplify processing."""

    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def _extract_header(lines: Iterable[str]) -> tuple[str, list[str]]:
    """Return the formatted header and the remaining lines to process."""

    iterator = iter(lines)
    for raw_line in iterator:
        line = raw_line.strip()
        if not line:
            continue
        formatted_header = _format_header(line)
        remainder = list(iterator)
        return formatted_header, remainder
    raise ValueError("The provided text does not contain a header line.")


def _format_header(line: str) -> str:
    """Format the header line into italic text with a vertical bar separator."""

    if ":" not in line:
        raise ValueError(
            "Header line must contain a colon separating date and location/title."
        )
    first, rest = line.split(":", 1)
    return f"*{first.strip()} | {rest.strip()}*"


def _collect_paragraphs(lines: Iterable[str]) -> list[str]:
    """Group the remaining lines into paragraphs separated by blank lines."""

    paragraphs: list[str] = []
    current: list[str] = []

    def flush_current() -> None:
        if current:
            paragraphs.append(" ".join(current).strip())
            current.clear()

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            flush_current()
            continue
        current.append(line)

    flush_current()
    return paragraphs


__all__ = ["reformat_prayer_text"]
