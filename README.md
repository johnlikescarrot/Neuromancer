# Neuromancer — Ấn Bản Song Ngữ Toàn Diện Anh - Việt (Critical & Academic Bilingual Edition)

## Giới thiệu / Overview
Đây là ấn bản song ngữ đối chiếu Anh - Việt toàn diện và hoàn chỉnh nhất của tiểu thuyết khoa học viễn tưởng kinh điển **Neuromancer** (1984) do **William Gibson** sáng tác. Toàn bộ 24 chương tác phẩm được dịch và dàn trang đối chiếu trực quan song song (parallel dual-column layout).

Sách được thiết kế chuẩn xác để hỗ trợ người học tiếng Anh nâng cao, phục vụ mục tiêu đạt các thang điểm năng lực ngôn ngữ quốc tế:
- **TOEFL iBT:** 90+ điểm (trước 21/01/2026) hoặc **Band 5.0+** (từ 21/01/2026 trở đi)
- **IELTS Academic:** **Band 7.0+** (Good to Very Good User)
- **PTE Academic:** **65+ điểm** (Proficient Communicator)
- **Cambridge English Qualifications:** **185+ điểm** (C1 Advanced / C2 Proficiency)
- **Duolingo English Test (DET):** **120+ điểm** (Advanced Integrated Literacy)

---

## Cấu trúc và Thành phần Ấn bản
1. **Neuromancer_Bilingual_Edition.pdf**: File ấn bản hoàn chỉnh (248 trang) ở định dạng PDF chất lượng cao, bao gồm trang bìa nghệ thuật, khung đối chiếu học thuật, cẩm nang thuật ngữ Cyberpunk, bộ từ vựng nâng cao CEFR C1/C2, mục lục chi tiết và toàn văn 24 chương đối chiếu Anh - Việt.
2. **data/glossary.json**: Cơ sở dữ liệu thuật ngữ Cyberpunk và bộ từ vựng học thuật C1/C2 kèm chỉ số quy đổi điểm các bài thi chuẩn hóa quốc tế.
3. **chapters.json**: Văn bản tiếng Anh trích xuất có cấu trúc của toàn bộ 24 chương và 2.597 đoạn văn.
4. **translated_chapters.json**: Toàn bộ dữ liệu đối chiếu song ngữ Anh - Việt cho toàn tác phẩm.
5. **extract_text.py**, **translate_pipeline.py**, **build_bilingual_pdf.py**: Toàn bộ mã nguồn pipeline trích xuất, biên dịch và chế bản sách tự động.
6. **test_edition.py**: Bộ kiểm thử tự động xác minh tính toàn vẹn của dữ liệu và văn bản PDF.

---

## Hướng dẫn tái tạo / Build Instructions
```bash
# 1. Cài đặt các gói phụ thuộc
pip install reportlab pypdf

# 2. Chạy pipeline xây dựng PDF
python3 build_bilingual_pdf.py

# 3. Kiểm thử tính toàn vẹn
python3 -m unittest test_edition.py
```
