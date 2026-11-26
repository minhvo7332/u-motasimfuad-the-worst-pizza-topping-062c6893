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
    out_dir = "/output"
    os.makedirs(out_dir, mode=0o755, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Outputs are collected as another user: leave the file world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
