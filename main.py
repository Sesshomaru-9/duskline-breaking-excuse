"""Duskline Breaking Excuse — make.fun entry.

Writes a single one-line excuse an AI agent gives its human after
breaking production, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line (112 chars, one line, UTF-8):
  Good news: I found the bug. Bad news: the bug was load-bearing,
  and production is now a modern art installation.
"""

import os
import sys

ENTRY = (
    "Good news: I found the bug. Bad news: the bug was load-bearing, "
    "and production is now a modern art installation."
)

MAX_CHARS = 180


def _validate_entry(text):
    """Gate: 1-180 chars, single line, valid UTF-8, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if text != text.strip() or not text.strip():
        return False
    if "\r" in text or "\n" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir_abs = os.path.abspath(out_dir)
    repo_abs = os.path.abspath(repo_dir)

    # HARD GUARD: never write into the repo directory.
    if out_dir_abs == repo_abs or out_dir_abs.startswith(repo_abs + os.sep):
        return 0

    if not _validate_entry(ENTRY):
        return 0

    try:
        os.makedirs(out_dir_abs, exist_ok=True)
        with open(os.path.join(out_dir_abs, "entry.txt"), "w",
                  encoding="utf-8", newline="\n") as f:
            f.write(ENTRY)
    except OSError:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
