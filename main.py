"""Worst Superpower — one-line entry writer.

Writes the chosen one-liner to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "I can see through any wall — but only walls made of glass, which everyone else just calls windows."

OUTPUT_PATH = "/output/entry.txt"


def _validate_entry(text):
    """The competition gate: UTF-8 text, 1-140 characters, one line,
    not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 140):
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = _validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
