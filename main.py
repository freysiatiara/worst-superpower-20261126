"""Worst Superpower entry.

Writes the one-line entry to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "I can stop any baby crying \u2014 but only by crying louder, and the baby has filed a complaint."

OUTPUT_PATH = "/output/entry.txt"


def _validate_entry(entry):
    """Check the entry against the competition gate.

    The gate requires UTF-8 text of 1 to 140 characters, a single line,
    not only whitespace, with no leading or trailing whitespace.
    """
    if not isinstance(entry, str):
        raise TypeError("entry must be a string")
    if not entry.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if entry != entry.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    return entry


def main():
    entry = _validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
