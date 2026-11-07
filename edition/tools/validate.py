#!/usr/bin/env python3
"""Validate the bilingual study companion dataset and build integrity."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "edition"))

from content.chapters_01_07 import CHAPTERS as c1
from content.chapters_08_12 import CHAPTERS as c2
from content.chapters_13_18 import CHAPTERS as c3
from content.chapters_19_24 import CHAPTERS as c4

def main():
    chapters = c1 + c2 + c3 + c4
    print(f"Validating {len(chapters)} chapters...")
    assert len(chapters) == 24, f"Expected 24 chapters, got {len(chapters)}"

    total_vocab = 0
    for idx, ch in enumerate(chapters, 1):
        assert ch["n"] == idx, f"Chapter {idx} has mismatched number {ch['n']}"
        assert ch["title"], f"Chapter {idx} missing title"
        assert ch["vi_title"], f"Chapter {idx} missing vi_title"
        assert ch["summary_en"], f"Chapter {idx} missing summary_en"
        assert ch["summary_vi"], f"Chapter {idx} missing summary_vi"
        assert ch["lens_en"], f"Chapter {idx} missing lens_en"
        assert ch["lens_vi"], f"Chapter {idx} missing lens_vi"
        assert ch["q_en"], f"Chapter {idx} missing q_en"
        assert ch["q_vi"], f"Chapter {idx} missing q_vi"
        assert ch["a_en"], f"Chapter {idx} missing a_en"
        assert ch["a_vi"], f"Chapter {idx} missing a_vi"
        assert ch["grammar_en"], f"Chapter {idx} missing grammar_en"
        assert ch["grammar_vi"], f"Chapter {idx} missing grammar_vi"
        assert ch["task_en"], f"Chapter {idx} missing task_en"
        assert ch["task_vi"], f"Chapter {idx} missing task_vi"

        vocab = ch.get("vocab", [])
        assert len(vocab) >= 8, f"Chapter {idx} expected >= 8 vocab words, got {len(vocab)}"
        total_vocab += len(vocab)
        for v in vocab:
            assert len(v) == 5, f"Vocab item {v} in ch {idx} does not have 5 fields"

    print(f"Validation successful! Total vocabulary terms: {total_vocab}")

if __name__ == "__main__":
    main()
