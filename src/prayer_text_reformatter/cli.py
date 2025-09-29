"""Command line interface for the prayer text reformatter."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .formatter import reformat_prayer_text


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert prayer request text into the bullet-point format used by "
            "the prayer-text-reformatter project."
        )
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Path to the plain-text file to be reformatted.",
    )
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help=(
            "Optional path for the reformatted text. If omitted, the result is "
            "printed to standard output."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    raw_text = args.input.read_text(encoding="utf-8")
    formatted = reformat_prayer_text(raw_text)

    if args.output:
        args.output.write_text(formatted + "\n", encoding="utf-8")
    else:
        sys.stdout.write(formatted + "\n")

    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
