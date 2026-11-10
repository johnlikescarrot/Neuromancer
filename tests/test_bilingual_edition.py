import json
import unittest
from html.parser import HTMLParser
from pathlib import Path

class EditionHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.chapter_ids = set()
        self.pairs = 0
        self.links = set()
        self.text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id", "").startswith("chapter-"):
            self.chapter_ids.add(attrs["id"])
        if "pair" in attrs.get("class", "").split():
            self.pairs += 1
        if attrs.get("href", "").startswith("#chapter-"):
            self.links.add(attrs["href"][1:])

    def handle_data(self, data):
        self.text.append(data)

class TestBilingualEdition(unittest.TestCase):
    def setUp(self):
        self.extracted_path = Path("data/extracted_novel.json")
        self.bilingual_path = Path("data/bilingual_novel.json")
        self.html_path = Path("data/novel_bilingual.html")
        self.pdf_path = Path("output/neuromancer_bilingual_edition.pdf")

    def test_extracted_data(self):
        self.assertTrue(self.extracted_path.exists(), "data/extracted_novel.json must exist")
        with open(self.extracted_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(len(data["parts"]), 5, "Novel should have 5 parts (4 parts + Coda)")
        total_chapters = sum(len(p["chapters"]) for p in data["parts"])
        self.assertEqual(total_chapters, 24, "Novel must contain exactly 24 chapters")
        total_paragraphs = sum(sum(c["paragraph_count"] for c in p["chapters"]) for p in data["parts"])
        self.assertGreater(total_paragraphs, 2500, "Novel should contain over 2500 paragraphs")

    def test_bilingual_data(self):
        self.assertTrue(self.bilingual_path.exists(), "data/bilingual_novel.json must exist")
        with open(self.bilingual_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("target_benchmarks", data)
        self.assertIn("IELTS", data["target_benchmarks"])
        self.assertIn("TOEFL_iBT", data["target_benchmarks"])
        self.assertIn("glossary", data)
        self.assertGreaterEqual(len(data["glossary"]), 20, "Glossary must have at least 20 academic terms")

        total_paragraphs = 0
        for part in data["parts"]:
            for chap in part["chapters"]:
                self.assertIn("study_guide", chap, f"Chapter {chap['chapter_index']} must have a study guide")
                self.assertTrue(len(chap["paragraphs"]) > 0, f"Chapter {chap['chapter_index']} has no paragraphs")
                for p in chap["paragraphs"]:
                    total_paragraphs += 1
                    self.assertTrue(len(p["en"].strip()) > 0)
                    self.assertTrue(len(p["vi"].strip()) > 0)
        self.assertEqual(total_paragraphs, 2598, "All 2598 paragraphs must have both English and Vietnamese text")

    def test_data_alignment_and_known_corrections(self):
        data = json.loads(self.bilingual_path.read_text(encoding="utf-8"))
        cache = json.loads(Path("data/translated_cache.json").read_text(encoding="utf-8"))
        pairs = [p for part in data["parts"] for chapter in part["chapters"] for p in chapter["paragraphs"]]
        ids = [p["id"] for p in pairs]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(p["vi"] == cache[p["id"]] for p in pairs))
        self.assertEqual(cache["2_4_7"], "“Xã hội đen.”")
        self.assertEqual(cache["3_10_7"], "“Sẵn sàng xông tới rồi.”")

    def test_rendered_structure_and_quality_notice(self):
        parser = EditionHTMLParser()
        parser.feed(self.html_path.read_text(encoding="utf-8"))
        self.assertEqual(parser.pairs, 2598)
        self.assertEqual(parser.chapter_ids, {f"chapter-{i}" for i in range(1, 25)})
        self.assertEqual(parser.chapter_ids, parser.links)
        text = " ".join(parser.text)
        self.assertIn("bản dịch máy chưa được hiệu đính", text)
        self.assertIn("không phải phép quy đổi trực tiếp", text)
        self.assertNotIn("Ví dụ nguyên tác", text)

    def test_html_and_pdf_generation(self):
        self.assertTrue(self.html_path.exists(), "data/novel_bilingual.html must exist")
        self.assertGreater(self.html_path.stat().st_size, 1_000_000, "HTML file must be > 1 MB")

        self.assertTrue(self.pdf_path.exists(), "PDF output file must exist")
        self.assertGreater(self.pdf_path.stat().st_size, 1_000_000, "PDF file must be > 1 MB")

        with open(self.pdf_path, "rb") as f:
            header = f.read(4)
            self.assertEqual(header, b"%PDF", "Output file must be a valid PDF format")

if __name__ == "__main__":
    unittest.main()
