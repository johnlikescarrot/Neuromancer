import os
import json
import pytest
from reportlab.pdfbase import pdfmetrics

def test_json_manifest_exists():
    manifest_path = "data/chapters_manifest.json"
    assert os.path.exists(manifest_path)
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    assert len(manifest) == 24
    assert sum(c["paragraphs_count"] for c in manifest) > 2500

def test_chapter_json_files():
    for ch_num in range(1, 25):
        ch_file = f"data/chapters/chapter_{ch_num:02d}.json"
        assert os.path.exists(ch_file)
        with open(ch_file, "r", encoding="utf-8") as f:
            ch_data = json.load(f)
        assert ch_data["chapter_num"] == ch_num
        assert len(ch_data["paragraphs"]) > 0

def test_bilingual_ch1_data():
    bilingual_file = "data/translated_ch01.json"
    assert os.path.exists(bilingual_file)
    with open(bilingual_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["chapter"] == 1
    assert len(data["pairs"]) == 221
    # Check first pair
    assert "television" in data["pairs"][0]["english"]
    assert "vô tuyến" in data["pairs"][0]["vietnamese"]

def test_pdf_generation_and_integrity():
    pdf_path = "Neuromancer_Bilingual_EN_VI.pdf"
    assert os.path.exists(pdf_path)
    file_size = os.path.getsize(pdf_path)
    assert file_size > 50000  # Should be at least ~100KB

    with open(pdf_path, "rb") as f:
        header = f.read(5)
        assert header == b"%PDF-"

def test_pedagogy_vocabulary_schema():
    import sys
    sys.path.insert(0, "scripts")
    from pedagogy import CHAPTER_1_VOCAB, EXAM_TIPS

    assert len(CHAPTER_1_VOCAB) >= 10
    for word, item in CHAPTER_1_VOCAB.items():
        assert item.word
        assert item.cefr_level in ["B2", "C1", "C2"]
        assert len(item.target_tests) > 0
        assert item.vietnamese_def
        assert item.english_def

    assert "IELTS_READING" in EXAM_TIPS
    assert "TOEFL_SYNTAX" in EXAM_TIPS
    assert "C1_C2_COLLOCATIONS" in EXAM_TIPS
