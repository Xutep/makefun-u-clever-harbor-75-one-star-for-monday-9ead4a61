#!/usr/bin/env python3
"""One Star for Monday.

Writes a one-star review of Monday, written as though Monday were a
restaurant, to /output/entry.txt. Deterministic: the same single line on
every run, stdlib only, no network, no input.
"""

import os

LINE = (
    "One star. Waited forty minutes for a table, the waiter served "
    "last weekend cold, and the bill charged me for the whole week."
)


def main():
    # Gate guard: the sealed scorer only accepts 1-180 chars, and the
    # task caps the review at 25 words. Fail loudly instead of writing
    # an entry the gate would refuse.
    words = LINE.split()
    assert 1 <= len(LINE) <= 180, "line must be 1-180 characters"
    assert len(words) <= 25, "line must be at most 25 words"
    assert LINE.strip() == LINE and LINE, "line must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
