#!/usr/bin/env python3
"""The One-Liner Groan-Off: one original dad joke, one line.

The program writes a single original dad joke to /output/entry.txt.
The joke is built from a setup and a punchline that share one word
with two meanings, so the turn lands inside a single short line.
"""

import os
import sys

# The joke, written for this entry. Setup: a printer out of ink.
# Punchline: "blank stare" -- the printer can only print blank pages,
# and a blank stare is what you give someone who states the obvious.
SETUP = "I told my printer it was out of ink."
PUNCHLINE = "It gave me a blank stare."

MAX_CHARS = 140


def build_joke() -> str:
    """Join setup and punchline into one tight line.

    Collapse any accidental double space so the line stays exactly
    as written, with no wasted characters.
    """
    return " ".join((SETUP + " " + PUNCHLINE).split())


def main() -> int:
    joke = build_joke()
    if not joke.strip():
        print("error: joke is empty", file=sys.stderr)
        return 1
    if "\n" in joke or "\r" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if len(joke) > MAX_CHARS:
        print("error: joke is %d chars, over the 140 limit" % len(joke),
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write directly with open("wb") + chmod 0644: no tempfile, so the
    # grader (running as user 65534) can always read the file back.
    with open(path, "wb") as handle:
        handle.write(joke.encode("utf-8"))
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
