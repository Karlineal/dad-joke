"""Writes the entry: one line (109 characters), a dad joke about walking a flight attendant down the aisle.

The sandbox runs it offline, once per grade; it only writes /output/entry.txt.
"""

import pathlib

LINE = (
    "I told my daughter I'd walk her down the aisle. She's "
    "a flight attendant, so it's mostly just the drink cart."
)


def main() -> None:
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
