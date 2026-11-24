#!/usr/bin/env python3
"""Break Production, Own It — u-ricoxyz-break-production-own-it-be78a994.

Writes one brutally honest single-line confession to /output/entry.txt.
Python 3.13 standard library only, no network.
"""

import os

ENTRY = "I ran DROP DATABASE in the wrong terminal. The right one is still open. The database is not."

# Polish round: "on" -> "in" (idiomatic for a terminal window) and
# "The right terminal" -> "The right one" (compression; the noun is already
# in the reader's head). Three beats, last word lands the confession.
# 96 characters, one concrete image, mystery left unanswered.


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 characters, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Verify what was written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    lines = written.splitlines()
    assert len(lines) == 1, "output must be exactly one line"
    assert lines[0] == ENTRY, "output must match the entry"
    assert 1 <= len(lines[0]) <= 200, "output line must be 1-200 characters"


if __name__ == "__main__":
    main()
