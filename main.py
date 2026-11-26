#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun program/v1 entry.

Writes one funny one-line pitch to /output/entry.txt. Fully deterministic:
no model calls, no randomness, no network, no clock, no environment input.
The same bytes are written on every run.
"""

import os

LINE = (
    "New: the Terms & Conditions pizza \u2014 topped with 47 pages of "
    "fine print you never read but already agreed to eat."
)


def main() -> None:
    # Gate: /output/entry.txt must be 1-200 chars of UTF-8, not whitespace-only.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line violates the gate"
    out_dir = "/output"
    # Never chmod the output directory itself: on the grader it is root-owned
    # and the program runs as uid 65534, so chmod would raise PermissionError.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Outputs are collected as another user: leave the file world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
