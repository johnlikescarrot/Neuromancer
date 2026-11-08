# Neuromancer — Ấn Bản Song Ngữ Anh - Việt & Cẩm Nang Học Thuật C1/C2 Toàn Diện

> **Tác giả:** William Gibson
> **Dự án:** Biên soạn ấn bản song ngữ đối sánh Anh - Việt toàn vẹn nhất của kiệt tác khoa học viễn tưởng *Neuromancer*, tích hợp hệ thống chú giải học thuật chuẩn mực quốc tế và xuất bản định dạng PDF chuẩn A4.

---

## 🌟 1. Giới thiệu tổng quan

*Neuromancer* (1984) là tác phẩm mở đường cho trào lưu **Cyberpunk**, tác phẩm đầu tiên giành trọn bộ 3 vương miện danh giá nhất của làng văn học khoa học viễn tưởng: **Giải Hugo**, **Giải Nebula** và **Giải thưởng Tưởng niệm Philip K. Dick**. Cuốn tiểu thuyết đã sản sinh và phổ quát hóa những khái niệm mang tính thời đại như *cyberspace* (không gian mạng), *the matrix* (ma trận), *neural interface* (giao diện thần kinh) và đặt ra các câu hỏi triết học sắc sảo về trí tuệ nhân tạo (AI), ý thức và bản dạng con người.

Ấn bản này cung cấp:
- **Dịch hoàn chỉnh 100% toàn bộ tác phẩm:** Gồm đủ **5 phần, 24 chương, 2.598 đoạn văn** đối chiếu song song. Không cắt gọt, không tóm lược.
- **Trình bày song song (Parallel Bilingual Layout):** Cột trái là văn bản tiếng Anh nguyên tác của William Gibson; cột phải là bản dịch tiếng Việt văn chương trau chuốt, giữ trọn sắc thái u uất, sắc lạnh đặc trưng của tiểu thuyết Neo-noir và Cyberpunk.
- **Tệp xuất bản PDF chất lượng cao:** Sẵn sàng tại `output/neuromancer_bilingual_edition.pdf` (~358 trang A4, dàn trang khoa học, đánh số trang và mục lục tự động).

---

## 🎯 2. Định hướng và Hỗ trợ các chuẩn Năng lực Tiếng Anh Quốc tế

Ấn bản được thiết kế đặc thù làm học liệu luyện đọc chuyên sâu (Academic Reading & Stylistics) phục vụ người học nâng cấp năng lực ngôn ngữ từ B2 lên C1 Advanced và C2 Proficiency:

| Bài thi / Chứng chỉ | Mức điểm mục tiêu | Ứng dụng trong ấn bản |
| :--- | :--- | :--- |
| **IELTS** | **7.0 - 8.5+** | Nâng cấp Lexical Resource & Grammatical Range qua cấu trúc câu đa tầng, văn phong miêu tả học thuật và cụm từ cố định (collocations). |
| **TOEFL iBT** | **90+** (trước 21/01/2026) / **5.0** (từ 21/01/2026) | Rèn luyện khả năng đọc hiểu văn bản phức hợp, suy luận nghĩa theo ngữ cảnh (Inference & Rhetorical Purpose). |
| **Cambridge English** | **185 - 210 điểm** (C1 Advanced / C2 Proficiency) | Làm chủ các cấu trúc ngữ pháp đỉnh cao: Đảo ngữ (Inversion), Thể giả định (Subjunctive), Cụm danh từ mở rộng, Cấu trúc tuyệt đối (Absolute Construction). |
| **PTE Academic** | **65 - 85+** | Mở rộng vốn từ vựng trừu tượng, thuật ngữ khoa học công nghệ, cải thiện tốc độ xử lý đọc hiểu văn bản dài. |
| **Duolingo English Test (DET)** | **120 - 150+** | Tăng cường phản xạ nhận diện từ vựng học thuật C1/C2 (Read and Select), hoàn thiện ngữ cảnh câu. |

---

## 📚 3. Cấu trúc học liệu trong ấn bản

Mỗi chương trong tác phẩm đều được đính kèm:
1. **Chapter Academic Masterclass:** Tóm lược diễn biến cốt truyện song song với phân tích chủ đề văn học.
2. **Grammar & Rhetoric Focus:** Bóc tách các hiện tượng ngữ pháp nâng cao xuất hiện trực tiếp trong văn bản gốc kèm câu ví dụ trích dẫn và phân tích ứng dụng.
3. **Cyberpunk & Academic Glossary:** Bảng tra cứu thuật ngữ chuyên sâu (Matrix, Cyberspace, ROM Construct, ICE, Zaibatsu, Villa Straylight,...) phiên âm quốc tế IPA, cấp độ CEFR và phân tích sắc thái biểu đạt.

---

## 🛠️ 4. Cấu trúc thư mục dự án

```
.
├── data/
│   ├── extracted_novel.json       # Toàn bộ 24 chương trích xuất từ EPUB
│   ├── translated_cache.json      # Dữ liệu dịch song ngữ 2.598 đoạn văn
│   ├── bilingual_novel.json       # Cơ sở dữ liệu song ngữ tích hợp chú giải
│   └── novel_bilingual.html       # Mã nguồn HTML định dạng sách A4
├── output/
│   └── neuromancer_bilingual_edition.pdf # Tệp PDF ấn bản hoàn chỉnh
├── scripts/
│   ├── extract_text.py            # Script bóc tách dữ liệu từ file EPUB
│   ├── translate_novel.py         # Script dịch thuật và chuẩn hóa dữ liệu
│   ├── build_bilingual_edition.py # Script biên soạn cẩm nang học thuật & từ vựng
│   ├── render_html.py             # Script thiết kế dàn trang A4
│   └── generate_pdf.py            # Script xuất bản PDF tự động qua Playwright
├── tests/
│   └── test_bilingual_edition.py  # Bộ kiểm thử tự động xác minh tính toàn vẹn
└── README.md
```

---

## 🚀 5. Hướng dẫn chạy và tái sinh tài liệu

Để tạo mới hoặc cập nhật lại toàn bộ tài liệu và ấn bản PDF:

```bash
# 1. Trích xuất văn bản từ EPUB
python3 scripts/extract_text.py

# 2. Biên dịch và tổng hợp dữ liệu học thuật
python3 scripts/build_bilingual_edition.py

# 3. Dàn trang HTML chuyên nghiệp
python3 scripts/render_html.py

# 4. Xuất bản tệp PDF song ngữ
python3 scripts/generate_pdf.py

# 5. Chạy bộ kiểm thử tự động
python3 -m unittest tests/test_bilingual_edition.py
```

---
*Ấn bản được hoàn thiện với tinh thần tôn trọng nguyên tác và phụng sự người học tiếng Anh học thuật đỉnh cao.*
