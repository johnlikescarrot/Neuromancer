import json
import unittest
from pathlib import Path

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

        # Assert full coverage of target international benchmarks
        self.assertIn("target_benchmarks", data)
        benchmarks = data["target_benchmarks"]
        self.assertIn("IELTS", benchmarks)
        self.assertIn("TOEFL_iBT", benchmarks)
        self.assertIn("Cambridge", benchmarks)
        self.assertIn("PTE_Academic", benchmarks)
        self.assertIn("DET", benchmarks)
        self.assertIn("90+", benchmarks["TOEFL_iBT"])
        self.assertIn("5.0", benchmarks["TOEFL_iBT"])
        self.assertIn("7.0", benchmarks["IELTS"])
        self.assertIn("185", benchmarks["Cambridge"])
        self.assertIn("65", benchmarks["PTE_Academic"])
        self.assertIn("120", benchmarks["DET"])

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

    def test_html_and_pdf_generation(self):
        self.assertTrue(self.html_path.exists(), "data/novel_bilingual.html must exist")
        self.assertGreater(self.html_path.stat().st_size, 1_000_000, "HTML file must be > 1 MB")

        self.assertTrue(self.pdf_path.exists(), "PDF output file must exist")
        self.assertGreater(self.pdf_path.stat().st_size, 1_000_000, "PDF file must be > 1 MB")

        with open(self.pdf_path, "rb") as f:
            header = f.read(4)
            self.assertEqual(header, b"%PDF", "Output file must be a valid PDF format")

    def test_typescript_build_files(self):
        self.assertTrue(Path("src/astryx_design_system.ts").exists())
        self.assertTrue(Path("src/render_astryx.ts").exists())
        self.assertTrue(Path("src/generate_pdf.ts").exists())
        self.assertTrue(Path("package.json").exists())
        self.assertTrue(Path("tsconfig.json").exists())

if __name__ == "__main__":
    unittest.main()
