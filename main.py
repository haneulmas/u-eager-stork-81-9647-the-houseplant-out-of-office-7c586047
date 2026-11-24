#!/usr/bin/env python3
"""Write this entry's one houseplant out-of-office line to /output/entry.txt.

The line is fixed text, so every run writes the same bytes and the two
grading runs agree. No input is read, no network is used.
"""

import os

LINE = "Out of office. My owner left in March and took the watering can. Now I photosynthesize out of pure spite."

def main():
    assert LINE, "entry line must not be empty"
    assert len(LINE) <= 120, "entry line exceeds the 120-character limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "entry.txt does not match the entry line"
    print(f"line: {len(LINE)} characters")


if __name__ == "__main__":
    main()
