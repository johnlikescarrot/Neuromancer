import unittest
import json
import os

class TestBilingualEdition(unittest.TestCase):
    def setUp(self):
        self.en_json_path = 'data/chapters_en.json'
        self.bilingual_json_path = 'data/bilingual_neuromancer.json'
        self.pdf_path = 'neuromancer_bilingual_en_vi.pdf'

    def test_english_chapters_exist_and_complete(self):
        self.assertTrue(os.path.exists(self.en_json_path), "chapters_en.json must exist")
        with open(self.en_json_path, 'r', encoding='utf-8') as f:
            chapters = json.load(f)
        self.assertEqual(len(chapters), 24, "Must contain exactly 24 chapters")
        total_paras = sum(len(c['paragraphs']) for c in chapters)
        self.assertGreater(total_paras, 2500, "Must contain all paragraphs from the original text")

    def test_bilingual_structure_and_translation(self):
        self.assertTrue(os.path.exists(self.bilingual_json_path), "bilingual_neuromancer.json must exist")
        with open(self.bilingual_json_path, 'r', encoding='utf-8') as f:
            bilingual_chapters = json.load(f)
        self.assertEqual(len(bilingual_chapters), 24, "Must contain all 24 chapters")

        for ch in bilingual_chapters:
            ch_num = ch["chapter_number"]
            self.assertIn("title_en", ch)
            self.assertIn("title_vi", ch)
            self.assertIn("part_en", ch)
            self.assertIn("part_vi", ch)
            self.assertIn("paragraphs", ch)
            self.assertIn("pedagogical_notes", ch)

            # Check paragraphs non-empty
            self.assertGreater(len(ch["paragraphs"]), 0)
            for pair in ch["paragraphs"]:
                self.assertTrue(len(pair["en"].strip()) > 0)
                self.assertTrue(len(pair["vi"].strip()) > 0)

            # Check pedagogical notes: all 24 chapters must have vocabulary and grammar focus
            ped = ch["pedagogical_notes"]
            self.assertIn("vocabulary", ped)
            self.assertGreater(len(ped["vocabulary"]), 0, f"Chapter {ch_num} must have vocabulary")
            for item in ped["vocabulary"]:
                self.assertIn("word", item)
                self.assertIn("pos", item)
                self.assertIn("ipa", item)
                self.assertIn("meaning_vi", item)
                self.assertIn("level", item)
                self.assertIn("collocation", item)
                self.assertIn("sample", item)

            self.assertIn("grammar_focus", ped)
            self.assertIn("pattern", ped["grammar_focus"])
            self.assertIn("explanation", ped["grammar_focus"])
            self.assertIn("exam_tip", ped["grammar_focus"])

    def test_terminology_consistency(self):
        with open(self.bilingual_json_path, 'r', encoding='utf-8') as f:
            bilingual_chapters = json.load(f)

        # Check Chapter 1 text for Case, Wage, Kirin beer
        ch1_text_vi = " ".join(p["vi"] for p in bilingual_chapters[0]["paragraphs"])
        self.assertIn("Case", ch1_text_vi)
        self.assertIn("Wage", ch1_text_vi)
        self.assertIn("Kirin", ch1_text_vi)
        self.assertNotIn("Vụ án", ch1_text_vi)

    def test_pdf_generated_and_non_empty(self):
        self.assertTrue(os.path.exists(self.pdf_path), "neuromancer_bilingual_en_vi.pdf must exist")
        pdf_size = os.path.getsize(self.pdf_path)
        self.assertGreater(pdf_size, 1_000_000, "PDF must be at least 1MB for full novel")

if __name__ == '__main__':
    unittest.main()
