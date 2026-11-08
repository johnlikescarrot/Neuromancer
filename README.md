# Neuromancer — Bản thảo học liệu đọc Anh - Việt

> **Tác giả tác phẩm gốc:** William Gibson
> **Dự án:** Bản thảo học liệu đọc đối chiếu Anh - Việt, kèm chú giải và tài liệu luyện đọc. Kho mã nguồn chưa ghi nhận giấy phép cho việc sao chép/dịch tác phẩm hoặc quy trình biên tập, hiệu đính độc lập.

---

## 🌟 1. Giới thiệu tổng quan

*Neuromancer* (1984) là tác phẩm mở đường cho trào lưu **Cyberpunk**, tác phẩm đầu tiên giành trọn bộ 3 vương miện danh giá nhất của làng văn học khoa học viễn tưởng: **Giải Hugo**, **Giải Nebula** và **Giải thưởng Tưởng niệm Philip K. Dick**. Cuốn tiểu thuyết đã sản sinh và phổ quát hóa những khái niệm mang tính thời đại như *cyberspace* (không gian mạng), *the matrix* (ma trận), *neural interface* (giao diện thần kinh) và đặt ra các câu hỏi triết học sắc sảo về trí tuệ nhân tạo (AI), ý thức và bản dạng con người.

Bản thảo hiện có các tệp dữ liệu đối chiếu và một PDF được sinh tự động. Số đoạn trong dữ liệu chỉ là kiểm đếm cấu trúc, không chứng minh bản dịch đầy đủ, chính xác hay đã qua biên tập chuyên môn. Hãy xem nội dung là bản nháp chưa được thẩm định, không phải bản dịch văn học đã xuất bản.

Trước khi chia sẻ hoặc phát hành, cần xác minh quyền sao chép và dịch tác phẩm gốc. Việc một tệp có trong kho mã nguồn không tự nó xác lập quyền phân phối hoặc quyền dịch.

---

## 🎯 2. Mục tiêu học tập tham khảo

Các mức dưới đây là mục tiêu do dự án đề xuất để định hướng việc chọn nội dung luyện đọc, không phải kết quả đánh giá đã được kiểm chứng. Một cuốn sách hoặc PDF không thể bảo đảm người học đạt điểm thi; điểm số phụ thuộc vào bài thi chính thức và cả bốn kỹ năng. Hãy đối chiếu thang điểm, cấu trúc bài thi và ngày áp dụng với nguồn chính thức của từng tổ chức trước khi dùng các mức này để lập kế hoạch.

Tài liệu có thể hỗ trợ luyện đọc và chú ý đến từ vựng, ngữ pháp, diễn ngôn. Nó chưa được kiểm định như một khóa luyện thi hay được tổ chức khảo thí chứng nhận.

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
