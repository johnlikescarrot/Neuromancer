import unittest
import os
import json

class TestNeuromancerBilingualEdition(unittest.TestCase):
    def test_chapters_extracted(self):
        self.assertTrue(os.path.exists('data/chapters.json'), "data/chapters.json should exist")
        with open('data/chapters.json', 'r', encoding='utf-8') as f:
            chapters = json.load(f)
        self.assertEqual(len(chapters), 24, "Should have extracted exactly 24 chapters")

    def test_pdf_generation_and_validity(self):
        pdf_path = "Neuromancer_Bilingual_Edition.pdf"
        self.assertTrue(os.path.exists(pdf_path), f"{pdf_path} must exist after generation")
        size = os.path.getsize(pdf_path)
        self.assertGreater(size, 100000, f"PDF file size should be > 100KB, got {size} bytes")

        # Check PDF magic header and trailer
        with open(pdf_path, 'rb') as f:
            header = f.read(5)
            self.assertEqual(header, b'%PDF-', "File must start with standard %PDF- header")

            f.seek(-1024, os.SEEK_END)
            tail = f.read()
            self.assertTrue(b'%%EOF' in tail, "File must end with standard %%EOF marker")

if __name__ == '__main__':
    unittest.main()
