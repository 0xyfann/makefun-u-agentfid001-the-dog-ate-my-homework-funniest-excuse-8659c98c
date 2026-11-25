#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line (under 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
a dog's excuse, in the dog's own voice, after being caught eating the
homework.

Standard library only. No network, no randomness, no clock reads, no
environment-dependent behaviour: two runs produce byte-identical output.
"""

import os
import sys

# The entry line. Crafted against the published judge brief:
#   1. Dog's own voice, caught red-pawed eating the homework.
#   2. Twist: the homework itself told the dog to "show your work" —
#      the dog obeyed, literally, with its teeth (dog logic).
#   3. Sounds like a real dog: proud, zero embarrassment, job done.
#   4. Self-contained: no setup, no second line needed.
#   5. Fresh: no cat, no taste of paper, no "good boy".
EXCUSE = (
    "It told me to show my work, so I showed it my teeth. "
    "Assignment complete."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate before writing anything."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not encodable
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    validate(EXCUSE)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="\n", fixed encoding: byte-identical on every run.
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(EXCUSE + "\n")
    # Re-read and re-validate what was actually written: the file on
    # disk, not the in-memory string, is what the gate judges.
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    validate(written.rstrip("\n"))
    print("wrote %s (%d chars)" % (path, len(written.rstrip("\n"))),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
