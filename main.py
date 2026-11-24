#!/usr/bin/env python3
"""One Word for the Boss.

Writes exactly one word describing the boss to /output/entry.txt.
The entry is a fixed string: no input, no network, no file reads,
no dates and no randomness, so every run produces byte-identical output.
"""

import os

# The entry: one word for the boss (11 characters).
# A micromanager crossed with a necromancer: the boss who conjures
# new tasks out of thin air, hovers over every detail, and raises
# dead deadlines back to life just to watch you meet them twice.
ENTRY = "Micromancer"


def main() -> None:
    if not 1 <= len(ENTRY) <= 30:
        raise ValueError(f"entry must be 1-30 characters, got {len(ENTRY)}")
    if ENTRY.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if any(ch.isspace() for ch in ENTRY):
        raise ValueError("entry must be exactly one word, with no spaces")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
