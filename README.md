# Neuromancer — Ấn Bản Song Ngữ Anh–Việt Toàn Văn & Tinh Thông Học Thuật (CEFR C1/C2)

**Complete Unabridged English–Vietnamese Bilingual & Academic Mastery Edition of *Neuromancer* by William Gibson (1984)**

---

## Tổng quan Dự án (Overview)

Dự án này biên soạn ấn bản song ngữ Anh–Việt **toàn văn 100%** (*5 Phần • 24 Chương • 2.597 Đoạn văn • ~79.000 từ tiếng Anh gốc*) của kiệt tác cyberpunk *Neuromancer*, kết hợp hệ thống học liệu ngôn ngữ chuyên sâu hướng tới 5 chuẩn điểm khảo thí quốc tế bậc **CEFR C1/C2**:

| Kỳ thi Quốc tế | Điểm Mục tiêu Thiết kế | Quy chiếu CEFR |
|---|---|---|
| **TOEFL iBT** | **90 điểm** *(trước 21/01/2026)* • **Band 5.0** *(từ 21/01/2026)* | C1 |
| **IELTS Academic / General Training** | **7.0 Overall** | C1 |
| **PTE Academic** | **65+** | C1 |
| **Cambridge English Qualifications** | **185+** *(C1 Advanced / C2 Proficiency)* | C1 → C2 |
| **Duolingo English Test (DET)** | **120+** | B2+ / C1 |

---

## Kiến trúc Kho mã & Quy trình Biên dịch (Repository Architecture)

- `UBIQUITOUS_LANGUAGE.md`: Chuẩn thuật ngữ cyberpunk, địa danh, công nghệ thần kinh và hồ sơ giọng điệu nhân vật xuyên suốt 24 chương.
- `data/source/`: Văn bản tiếng Anh nguyên tác trích xuất chuẩn xác 100% từ `neuromancer.epub` (`manifest.json` và `ch01.json`..`ch24.json`).
- `data/front_matter.json` & `data/back_matter.json`: Dẫn luận học thuật, bản đồ quy chiếu 5 kỳ thi, quy trình 5 bước tự học song ngữ và bộ đề tổng hợp cuối sách.
- `data/translations/ch01.vi.txt`..`ch24.vi.txt`: Bản dịch văn học tiếng Việt căn chỉnh 1–1 theo mã đoạn `[001]`..`[NNN]`.
- `data/pedagogy/ch01.study.json`..`ch24.study.json`: 24 Hồ sơ Tinh thông Ngôn ngữ C1/C2 cuối mỗi chương (Bảng từ vựng C1–C2 kèm IPA & collocations, Giải phẫu cú pháp nâng cao, Bài tập thực chiến đa kỳ thi kèm đáp án chi tiết).
- `scripts/extract_source.py`: Bộ trích xuất văn bản gốc từ EPUB.
- `scripts/verify_edition.py`: Công cụ kiểm định tự động tính toàn vẹn 1–1 từng đoạn văn, dấu tiếng Việt, thẻ in nghiêng và cấu trúc học liệu C1/C2.
- `scripts/build_pdf.py`: Trình biên dịch chế bản sách song ngữ khổ A4 chất lượng xuất bản bằng **Typst** (`Crimson Pro`, `Be Vietnam Pro`, `JetBrains Mono`).
- `Neuromancer_Bilingual_Vi_En_C1_Edition.pdf`: Ấn phẩm PDF hoàn chỉnh cuối cùng.

## Hướng dẫn Kiểm định & Chế bản PDF (Verification & Build)

```bash
# 1. Cài đặt phông chữ OpenType hỗ trợ đầy đủ tiếng Việt & môi trường Python
npm ci
python3 -m venv .venv
.venv/bin/pip install typst pymupdf

# 2. Kiểm định toàn diện bản dịch & hồ sơ C1/C2
.venv/bin/python scripts/verify_edition.py --all

# 3. Xuất bản ấn phẩm PDF toàn văn
.venv/bin/python scripts/build_pdf.py --require-complete --output Neuromancer_Bilingual_Vi_En_C1_Edition.pdf
```
