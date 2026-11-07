from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import pysbd  # noqa: E402

from extract_source import extract  # noqa: E402
from qa import validate_translation  # noqa: E402
from translate import paragraph_units  # noqa: E402


class FakeSentencePiece:
    def encode(self, text, out_type=str):
        return text.split()


class PipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = extract(ROOT / "neuromancer.epub")
        cls.editorial = json.loads(
            (ROOT / "edition/editorial.json").read_text(encoding="utf-8")
        )

    def test_source_is_complete_and_stable(self):
        self.assertEqual(self.source["chapter_count"], 24)
        self.assertEqual(self.source["paragraph_count"], 2597)
        self.assertEqual(self.source["body_word_count"], 78944)
        self.assertEqual(self.source["chapters"][0]["paragraphs"][0]["id"], "ch01-p0001")
        self.assertEqual(self.source["chapters"][-1]["paragraphs"][-1]["id"], "ch24-p0050")
        self.assertEqual(
            self.source["frontmatter"]["dedication_en"],
            ["for Deb", "who made it possible with love"],
        )
        self.assertEqual(
            self.source["source_sha256"],
            hashlib.sha256((ROOT / "neuromancer.epub").read_bytes()).hexdigest(),
        )

    def test_unit_segmentation_preserves_every_word(self):
        paragraph = {
            "id": "test-p0001",
            "en": 'He paused. "We need to reach the old lighthouse before nightfall." '
            + "This is a deliberately long clause with words that must remain intact. " * 35,
        }
        units = paragraph_units(paragraph, pysbd.Segmenter(language="en", clean=False), FakeSentencePiece())
        self.assertGreater(len(units), 1)
        self.assertEqual(" ".join(unit["en"] for unit in units), paragraph["en"].strip())
        self.assertTrue(all(unit["en_sha256"] for unit in units))

    def test_translation_coverage_contract(self):
        records = {}
        for chapter in self.source["chapters"]:
            for paragraph in chapter["paragraphs"]:
                records[paragraph["id"]] = {
                    "vi": "Bản dịch tiếng Việt dùng để kiểm thử cấu trúc.",
                    "en_sha256": hashlib.sha256(paragraph["en"].encode()).hexdigest(),
                    "status": "machine-draft",
                    "unit_count": 1,
                }
        translation = {
            "source_sha256": self.source["source_sha256"],
            "completed_paragraphs": len(records),
            "paragraphs": records,
        }
        report = validate_translation(self.source, translation, self.editorial)
        self.assertEqual(report["translated_paragraphs"], 2597)
        self.assertEqual(report["errors"], [])

    def test_editorial_text_has_no_accidental_split_words(self):
        raw = json.dumps(self.editorial, ensure_ascii=False)
        for wrong in ("ngườ i", "Ngườ i", "thờ i", "củ a", "trờ i"):
            self.assertNotIn(wrong, raw)


if __name__ == "__main__":
    unittest.main()
