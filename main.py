#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes a single-line tombstone epitaph of famous last words to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The epitaph is fixed and deterministic: the same line, byte for byte,
on every run. It is 52 characters, well inside the 150-character cap.
"""

import os

EPITAPH = "Tell the kids I loved them. Tell the bank I did not."


def main():
    # The gate requires 1-150 characters of non-whitespace UTF-8 text.
    text = EPITAPH.strip()
    assert 1 <= len(text) <= 150, f"epitaph is {len(text)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
