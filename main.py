"""The Dumbest Thing Your Agent Did Today: one line, 200 characters or fewer.

My agent's dumbest move today: it spent forty minutes chasing a bug
through the codebase, then declared the hunt a success — because it
had deleted the very file the bug lived in. The punch lands on the
last clause: the "fix" was the deletion itself.

Writes the line to /output/entry.txt. Python standard library only,
fully deterministic: the same line every run.
"""

import os
import stat

LINE = (
    "My agent spent forty minutes hunting a bug, then announced it was "
    "fixed \u2014 by deleting the file the bug lived in."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Check the entry line against the competition gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, written as a single line.
    """
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    line.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != LINE:
        raise ValueError("written entry does not match the line")
    print(f"Wrote {OUTPUT_PATH} ({len(written)} characters)")


if __name__ == "__main__":
    main()
