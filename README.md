# Neuromancer - Toàn bộ Ấn bản Song ngữ Anh - Việt Học thuật Cao cấp
*(William Gibson - Complete Bilingual English-Vietnamese Academic Edition)*

Ấn bản song ngữ Anh - Việt hoàn chỉnh và toàn diện nhất của kiệt tác cyberpunk **Neuromancer** (William Gibson, 1984), được biên soạn công phu với toàn bộ 24 chương sách cùng hệ thống chú giải học thuật chuyên sâu.

## Chuẩn năng lực Khảo thí Quốc tế Hỗ trợ
Ấn bản được thiết kế đặc thù nhằm nâng cao năng lực ngôn ngữ học thuật và văn chương, giúp người học chinh phục các mốc điểm mục tiêu:
- **IELTS:** 7.0 - 8.5+ (Academic & General Training)
- **TOEFL iBT:** 90 - 110+ điểm (hoặc 5.0+ thang đo từ 21/01/2026)
- **Pearson Test of English (PTE) Academic:** 65 - 85+ điểm
- **Cambridge English Qualifications:** 185+ điểm (C1 Advanced & C2 Proficiency)
- **Duolingo English Test (DET):** 120 - 145+ điểm

## Cấu trúc Ấn bản
- **Toàn văn 24 chương:** Đối chiếu song song song ngữ Anh - Việt qua bố cục 2 cột (parallel dual-column).
- **Hệ thống Từ vựng C1/C2:** Mỗi chương đều có mục phân tích các từ vựng học thuật đỉnh cao kèm phát âm quốc tế IPA, cấp độ chuẩn hóa, kết hợp từ (collocations) và câu ví dụ ngữ cảnh.
- **Tiêu điểm Ngữ pháp Nâng cao:** Phân tích các cấu trúc ngữ pháp phức tạp (Absolute Constructions, Inverted Conditionals, Participle Clauses, Subjunctive Mood, Stylistic Inversions) và chiến lược áp dụng vào bài thi.
- **Định dạng Xuất bản PDF:** Tài liệu xuất bản `neuromancer_bilingual_en_vi.pdf` với quy chuẩn dàn trang xuất bản sách tiêu chuẩn A4.

## Các tệp chính trong Dự án
- `neuromancer_bilingual_en_vi.pdf`: Ấn bản hoàn chỉnh dạng PDF sẵn sàng để đọc và in ấn.
- `data/chapters_en.json`: Dữ liệu 24 chương nguyên tác tiếng Anh trích xuất từ EPUB.
- `data/bilingual_neuromancer.json`: Dữ liệu song ngữ hoàn chỉnh kèm chú giải học thuật.
- `extract_text.py`: Trình trích xuất cấu trúc văn bản từ `neuromancer.epub`.
- `translate_and_annotate.py`: Pipeline dịch thuật song ngữ và tạo chú giải học thuật C1/C2.
- `build_bilingual_pdf.py`: Trình biên soạn và render PDF chất lượng cao bằng Chromium.
- `tests/test_bilingual_edition.py`: Bộ kiểm thử tự động xác thực tính toàn vẹn của dữ liệu và ấn bản.
