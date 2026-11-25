"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message -- the note an AI agent leaves in the log
after a long night of chasing down and fixing its own bugs -- to
entry.txt in the output directory and nothing else. Deterministic,
Python 3 standard library only, no network.
"""

import os

MESSAGE = (
    "fix: it was me. I shipped the bug at 21:00, blamed the tests at "
    "midnight, and at 04:00 I merged my own apology. the tests pass; "
    "the tests remember"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)
    # Verification gate: read back and confirm one line, 1-200 chars.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != MESSAGE or not 1 <= len(written) <= 200 or "\n" in written:
        raise SystemExit("verification failed: entry.txt is not one line of 1-200 chars")


if __name__ == "__main__":
    main()
