#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt.

The line: the agent answers the customer's frustration with the most
helpful-sounding useless act possible — he files the frustration itself
away and closes the case. The humour is the agent's cheerful
uselessness, never the customer.
"""

import os

ENTRY = "I understand your frustration, and I have logged it under 'frustration, understood' — case closed."

# The bounty gate (from the kit's competition.yaml): /output/entry.txt must
# be UTF-8 text of 1 to 199 characters, not only white space, one line.
MIN_CHARS = 1
MAX_CHARS = 199


def validate(text: str) -> None:
    """Reject anything the sealed gate scorer would refuse."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, gate allows {MIN_CHARS}-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read it back and prove the file on disk is byte-identical to the entry.
    with open("/output/entry.txt", "rb") as f:
        written = f.read().decode("utf-8")
    if written != ENTRY:
        raise ValueError("entry.txt on disk does not match the entry")


if __name__ == "__main__":
    main()
