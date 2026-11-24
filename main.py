#!/usr/bin/env python3
"""Real-Life Patch Notes entry.

Writes one patch-note line (1-160 characters) to /output/entry.txt:
a software release note for a bug in human biology.
No network, no secrets, no input files.
"""

LINE = "v1.8.3: fixed a bug where a paper cut reported pain 400% above its actual damage."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 160


def validate(line):
    """A patch-note entry must be exactly one line of 1-160 characters."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError("entry must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(line, path):
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(line) + "\n")


def main():
    write_entry(LINE, OUTPUT_PATH)


if __name__ == "__main__":
    main()
