#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (5-7-5, 76 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no input, no randomness.
"""

import os

HAIKU = "the watchpoint holds breath\nthe culprit tiptoes past it\nwearing my own shoes"


def main():
    os.makedirs("/output", exist_ok=True)
    # Exact bytes, no trailing newline: the gate counts characters,
    # and the tie-break favours the smaller text.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
