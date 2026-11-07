#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validation script for Neuromancer Bilingual Learning Edition and generated PDF."""

import sys
import json
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import fitz  # PyMuPDF
import edition.data.companion_data as data


def validate():
    pdf_path = ROOT / "edition" / "Neuromancer-Bilingual-Learning-Companion.pdf"
    print(f"Validating PDF artifact at {pdf_path}...")

    # 1. Check file existence and size
    assert pdf_path.exists(), f"Error: PDF does not exist at {pdf_path}"
    file_size = pdf_path.stat().st_size
    print(f"  [PASS] File exists. Size: {file_size:,} bytes")
    assert file_size > 50_000, f"Error: PDF size is suspiciously small ({file_size} bytes)"

    # 2. Check PDF loadability and page count with PyMuPDF
    doc = fitz.open(pdf_path)
    page_count = len(doc)
    print(f"  [PASS] PyMuPDF opened successfully. Total pages: {page_count}")
    assert page_count >= 25, f"Error: Expected at least 25 pages, got {page_count}"

    # 3. Extract text from all pages and test coverage
    full_text = []
    for page_num in range(page_count):
        page = doc[page_num]
        text = page.get_text()
        full_text.append(text)
    combined_text = "\n".join(full_text)

    # 4. Verify all 24 chapters are referenced in extracted text
    print("  Checking chapter coverage...")
    for ch in range(1, 25):
        assert f"Chapter {ch}:" in combined_text or f"Chương {ch}:" in combined_text, (
            f"Error: Chapter {ch} not found in PDF text"
        )
    print("  [PASS] All 24 chapters verified in generated PDF.")

    # 5. Verify Vietnamese character encoding and diacritics
    test_vietnamese_phrases = [
        "Khúc Ca Buồn Thành Phố Chiba",
        "Chuyến Đi Sắm Vũ Khí",
        "Nửa Đêm Trên Đường Jules Verne",
        "Cuộc Đột Kích Biệt Thự Ánh Sao",
        "Khởi Hành và Điểm Đến",
        "đối chiếu",
        "không gian",
        "thần kinh",
        "mô phỏng"
    ]
    print("  Checking Vietnamese diacritics rendering...")
    for phrase in test_vietnamese_phrases:
        assert phrase in combined_text or phrase.lower() in combined_text.lower(), (
            f"Error: Vietnamese phrase '{phrase}' not extracted correctly from PDF"
        )
    print("  [PASS] Vietnamese font rendering & diacritics validated without missing glyphs.")

    # 6. Verify standardized exam benchmarks presence
    benchmarks = ["TOEFL", "IELTS", "PTE", "Cambridge", "Duolingo"]
    print("  Checking exam benchmark references...")
    for bm in benchmarks:
        assert bm in combined_text, f"Error: Benchmark {bm} missing in PDF text"
    print("  [PASS] All standardized exam competencies and benchmarks verified in PDF text.")

    # 7. Check audit consistency with EPUB
    audit_path = ROOT / "edition" / "reports" / "source-audit.json"
    if audit_path.exists():
        with open(audit_path, "r", encoding="utf-8") as f:
            audit_data = json.load(f)
        assert audit_data["structure"]["chapter_count"] == 24, "Audit must reflect 24 chapters"
        print("  [PASS] Source audit data matches 24-chapter requirement.")

    print("\n==========================================")
    print("ALL VALIDATION CHECKS PASSED SUCCESSFULLY!")
    print(f"Total Pages: {page_count} | Chapters: 24 | Vocabulary Items: {sum(len(c['vocabulary']) for c in data.CHAPTERS_DATA)}")
    print("==========================================\n")


def main():
    try:
        validate()
    except Exception as e:
        print(f"Validation FAILED: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
