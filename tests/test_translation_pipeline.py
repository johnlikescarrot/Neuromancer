import unittest
import os
import json

class TestTranslationPipeline(unittest.TestCase):
    def test_data_chapters_exist(self):
        self.assertTrue(os.path.exists('data/chapters.json'))
        with open('data/chapters.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertGreaterEqual(len(data), 24)

    def test_glossary_benchmarks(self):
        self.assertTrue(os.path.exists('data/glossary.json'))
        with open('data/glossary.json', 'r', encoding='utf-8') as f:
            glossary = json.load(f)
        benchmarks = glossary.get('benchmarks', {})
        self.assertIn('TOEFL', benchmarks)
        self.assertIn('IELTS', benchmarks)
        self.assertIn('PTE_Academic', benchmarks)
        self.assertIn('Cambridge', benchmarks)
        self.assertIn('Duolingo_DET', benchmarks)

    def test_ch01_content_integrity(self):
        self.assertTrue(os.path.exists('content/ch01_bilingual.json'))
        with open('content/ch01_bilingual.json', 'r', encoding='utf-8') as f:
            ch1 = json.load(f)
        self.assertEqual(ch1.get('chapter'), 'CHAPTER 1')
        parallels = [s for s in ch1.get('sections', []) if s.get('type') == 'parallel']
        self.assertGreaterEqual(len(parallels), 200)
        # Check first parallel paragraph
        first_p = parallels[0]
        self.assertIn("The sky above the port", first_p['en'])
        self.assertIn("Bầu trời phía trên bến cảng", first_p['vi'])

    def test_ch02_content_integrity(self):
        self.assertTrue(os.path.exists('content/ch02_bilingual.json'))
        with open('content/ch02_bilingual.json', 'r', encoding='utf-8') as f:
            ch2 = json.load(f)
        self.assertEqual(ch2.get('chapter'), 'CHAPTER 2')
        parallels = [s for s in ch2.get('sections', []) if s.get('type') == 'parallel']
        self.assertGreaterEqual(len(parallels), 160)
        # Check first parallel paragraph
        first_p = parallels[0]
        self.assertIn("Chiba Hilton", first_p['en'])
        self.assertIn("Chiba Hilton", first_p['vi'])

    def test_pdf_generated(self):
        pdf_path = 'Neuromancer_Bilingual_Edition.pdf'
        self.assertTrue(os.path.exists(pdf_path))
        self.assertGreater(os.path.getsize(pdf_path), 50000)

if __name__ == '__main__':
    unittest.main()
