#!/usr/bin/env python3
"""The Router Confesses — make.fun bounty entry.

Writes one line to /output/entry.txt: a home Wi-Fi router excusing
itself for dropping the connection at a movie's climax.

Stdlib only; no network, no dependencies.
"""

import os
import sys

LINE = (
    "Forgive me \u2014 I got jealous. Six years behind this couch, "
    "and nobody's ever gasped like that when I came back."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    text = LINE.strip()
    if "\n" in text or "\r" in text:
        print("gate fail: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"gate fail: entry is {len(text)} chars, need 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: entry is blank", file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("gate fail: read-back mismatch", file=sys.stderr)
        return 1
    print(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
