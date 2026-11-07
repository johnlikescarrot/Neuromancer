#!/usr/bin/env python3
"""Helper script to display source paragraphs for a chapter cleanly."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: inspect_chapter.py <ch_num> [start_idx] [end_idx]")
        sys.exit(1)
    ch_num = int(sys.argv[1])
    start = int(sys.argv[2]) if len(sys.argv) >= 3 else 1
    end = int(sys.argv[3]) if len(sys.argv) >= 4 else 999999

    ch_path = ROOT / "data" / "source" / f"ch{ch_num:02d}.json"
    ch = json.loads(ch_path.read_text(encoding="utf-8"))
    print(
        f"=== Chapter {ch['chapter']} ({ch['part_title_en']}) | "
        f"Total paras: {ch['paragraph_count']} | Words: {ch['word_count']} ==="
    )
    for p in ch["paragraphs"]:
        if start <= p["index"] <= end:
            print(f"[{p['index']:03d}] {p['en']}")


if __name__ == "__main__":
    main()
