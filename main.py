"""Entry program for make.fun "One Word, One Username, One Reward".

Writes the entrant's own make.fun username, one word and nothing else,
to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

ENTRY = "tyrmeapart"

# Sealed gate: 1-30 characters, a single word, nothing else.
MAX_CHARS = 30


def main():
    if not ENTRY or len(ENTRY) > MAX_CHARS or len(ENTRY.split()) != 1:
        raise SystemExit("entry fails the gate: must be one word, 1-30 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
