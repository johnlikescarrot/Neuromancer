import unittest
import os
import json
import pypdf

class TestNeuromancerBilingualEdition(unittest.TestCase):
    def test_chapters_json_integrity(self):
        self.assertTrue(os.path.exists("chapters.json"), "chapters.json must exist")
        with open("chapters.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data["total_chapters"], 24, "Must have exactly 24 chapters")
        self.assertEqual(data["total_paragraphs"], 2597, "Must have 2597 total paragraphs")
        self.assertEqual(len(data["chapters"]), 24)

    def test_glossary_integrity(self):
        self.assertTrue(os.path.exists("data/glossary.json"), "data/glossary.json must exist")
        with open("data/glossary.json", "r", encoding="utf-8") as f:
            glossary = json.load(f)
        self.assertIn("cyberpunk_terms", glossary)
        self.assertGreaterEqual(len(glossary["cyberpunk_terms"]), 10)
        self.assertIn("academic_vocabulary_cefr_c1_c2", glossary)
        self.assertGreaterEqual(len(glossary["academic_vocabulary_cefr_c1_c2"]), 10)
        self.assertIn("test_proficiency_framework", glossary)
        framework = glossary["test_proficiency_framework"]
        self.assertIn("TOEFL_iBT", framework)
        self.assertIn("IELTS", framework)
        self.assertIn("PTE_Academic", framework)
        self.assertIn("Cambridge", framework)
        self.assertIn("DET", framework)

    def test_translated_chapters_completeness(self):
        self.assertTrue(os.path.exists("translated_chapters.json"), "translated_chapters.json must exist")
        with open("translated_chapters.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data["total_chapters"], 24)
        total_pairs = sum(len(c["paragraphs"]) for c in data["chapters"])
        self.assertEqual(total_pairs, 2597, "All 2597 paragraphs must be translated")
        for ch in data["chapters"]:
            for p in ch["paragraphs"]:
                self.assertTrue(p["en"].strip(), "English text must not be empty")
                self.assertTrue(p["vi"].strip(), "Vietnamese text must not be empty")

    def test_pdf_generation_and_pages(self):
        self.assertTrue(os.path.exists("Neuromancer_Bilingual_Edition.pdf"), "PDF must exist")
        size = os.path.getsize("Neuromancer_Bilingual_Edition.pdf")
        self.assertGreater(size, 1000000, "PDF size must be greater than 1MB")
        reader = pypdf.PdfReader("Neuromancer_Bilingual_Edition.pdf")
        self.assertGreaterEqual(len(reader.pages), 200, "Book must have at least 200 pages")

if __name__ == "__main__":
    unittest.main()
