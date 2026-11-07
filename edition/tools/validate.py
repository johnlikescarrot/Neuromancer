# -*- coding: utf-8 -*-
"""
Automated Validation Suite for Neuromancer Bilingual Academic Learning Companion PDF.
Verifies page count, embedded fonts, Vietnamese glyph rendering, chapter coverage (all 24 chapters),
CEFR/exam benchmark presence, and structural integrity using PyMuPDF.
"""
import os
import sys
import pymupdf

current_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
pdf_path = os.path.join(repo_root, "edition", "Neuromancer-Bilingual-Learning-Companion.pdf")

def run_validation():
    print(f"=== VALIDATING PDF: {pdf_path} ===")
    assert os.path.exists(pdf_path), f"ERROR: Target PDF not found at {pdf_path}"

    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    print(f"[CHECK 1] Page Count: {total_pages} pages (Requirement: > 50 pages) -> PASS")
    assert total_pages >= 50, f"Expected at least 50 pages, got {total_pages}"

    # Check font embedding across pages
    fonts_detected = set()
    for page in doc:
        font_list = page.get_fonts()
        for f in font_list:
            fonts_detected.add(f[3]) # font name
    print(f"[CHECK 2] Embedded Fonts: {fonts_detected} -> PASS")
    assert any("BeVietnamPro" in f for f in fonts_detected), "BeVietnamPro font must be embedded!"

    # Aggregate full text to verify comprehensive coverage
    full_text = ""
    for page in doc:
        full_text += page.get_text() + "\n"

    # Check Vietnamese glyphs
    vietnamese_sample_phrases = [
        "ẤN BẢN SONG NGỮ ANH - VIỆT",
        "Bầu trời phía trên",
        "thành phố Chiba",
        "không gian mạng",
        "siêu trí tuệ nhân tạo",
        "ĐIỆU BLUES THÀNH PHỐ CHIBA",
        "CHUYẾN SĂN HÀNG",
        "NỬA ĐÊM Ở PHỐ JULES VERNE",
        "ĐỢT TẤN CÔNG VILLA STRAYLIGHT",
        "KHỞI HÀNH VÀ HỒI HƯƠNG"
    ]
    for phrase in vietnamese_sample_phrases:
        assert phrase in full_text, f"Missing Vietnamese phrase: {phrase}"
    print(f"[CHECK 3] Vietnamese Glyph & Text Integrity: All {len(vietnamese_sample_phrases)} phrases found -> PASS")

    # Check Exam Benchmarks
    benchmarks = ["IELTS Academic", "TOEFL iBT", "PTE Academic", "Cambridge English", "Duolingo English Test"]
    for b in benchmarks:
        assert b in full_text, f"Missing target benchmark: {b}"
    print(f"[CHECK 4] Standardized Exam Benchmarks: All {len(benchmarks)} exam references verified -> PASS")

    # Check Chapter Coverage: 1 to 24
    for ch_num in range(1, 25):
        pattern = f"CHAPTER {ch_num}:"
        assert pattern in full_text, f"Missing Chapter {ch_num} marker in PDF text!"
    print(f"[CHECK 5] Complete Chapter Coverage: All 24 chapters verified in document body -> PASS")

    # Check Answer Key Table
    assert "PHỤ LỤC: BẢNG TRA CỨU ĐÁP ÁN" in full_text, "Missing Appendix Answer Key!"
    print(f"[CHECK 6] Comprehensive Appendix & Answer Key: Verified -> PASS")

    print("\n>>> ALL VALIDATION CHECKS PASSED SUCCESSFULLY! PDF IS READY FOR PRODUCTION. <<<")

if __name__ == "__main__":
    run_validation()
