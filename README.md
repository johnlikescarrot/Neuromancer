# Neuromancer — Ấn bản song ngữ & học liệu đọc tiếng Anh

> **Phạm vi bản cập nhật này:** dự án đã có sẵn tệp PDF song ngữ và dữ liệu toàn văn trong checkout. Bản cập nhật hiện tại **không dịch tiếp, không mở rộng, không tái tạo** nội dung tiểu thuyết; thay vào đó, nó bổ sung một cẩm nang luyện đọc tiếng Anh nguyên bản, không trích nguyên văn tác phẩm. Các tệp PDF/dữ liệu song ngữ đã có không bị ghi đè. Nội dung hiện có trong kho không được xem là xác minh về quyền tái bản hay độ chính xác của bản dịch.

> **Tác giả:** William Gibson
> **Dự án:** Biên soạn ấn bản song ngữ đối sánh Anh - Việt toàn vẹn nhất của kiệt tác khoa học viễn tưởng *Neuromancer*, tích hợp hệ thống chú giải học thuật chuẩn mực quốc tế và xuất bản định dạng PDF chuẩn A4.

---

## 🌟 1. Giới thiệu tổng quan

*Neuromancer* (1984) là một tác phẩm tiêu biểu của dòng Cyberpunk và đặt ra những câu hỏi về trí tuệ nhân tạo, ý thức, công nghệ và bản dạng. Kho hiện có một tệp PDF song ngữ được lưu sẵn; nội dung, quyền sử dụng và độ chính xác của ấn bản đó không được xác minh trong cập nhật này.

Bản cập nhật TypeScript bổ sung:
- **Cẩm nang đọc tiếng Anh nguyên bản** ở `output/neuromancer_english_study_companion.pdf`: hướng dẫn đọc gần, kỹ năng suy luận, vốn từ, câu hỏi luyện tập và một đoạn mẫu do dự án tự viết.
- **Mục tiêu học tập có điều kiện:** tài liệu hỗ trợ luyện đọc và phân tích; không bảo đảm hay dự đoán điểm thi và không thay thế đề luyện chính thức.
- **Không thêm bản dịch/đoạn tiểu thuyết mới**; tệp `output/neuromancer_bilingual_edition.pdf` hiện có được giữ nguyên, không được tái sinh bởi script mới.

---

## 🎯 2. Định hướng và Hỗ trợ các chuẩn Năng lực Tiếng Anh Quốc tế

Ấn bản được thiết kế đặc thù làm học liệu luyện đọc chuyên sâu (Academic Reading & Stylistics) phục vụ người học nâng cấp năng lực ngôn ngữ từ B2 lên C1 Advanced và C2 Proficiency:

| Bài thi / Chứng chỉ | Mức điểm mục tiêu | Ứng dụng trong ấn bản |
| :--- | :--- | :--- |
| **IELTS** | **7.0 - 8.5+** | Nâng cấp Lexical Resource & Grammatical Range qua cấu trúc câu đa tầng, văn phong miêu tả học thuật và cụm từ cố định (collocations). |
| **TOEFL iBT** | Mục tiêu người dùng nêu: 90 (thang cũ) / 5.0 (thang mới) | Lưu ý hiệu chỉnh theo ETS: yêu cầu thang cũ 90 được khuyến nghị tương ứng 4.5 trên thang mới; 5.0 gắn với 95+ thang cũ. Kiểm tra yêu cầu chính thức của đơn vị nhận hồ sơ. |
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
│   ├── neuromancer_bilingual_edition.pdf # PDF song ngữ đã có (không được tái sinh)
│   └── neuromancer_english_study_companion.pdf # Học liệu tiếng Anh nguyên bản
├── scripts/
│   ├── extract_text.py            # Script bóc tách dữ liệu từ EPUB
│   ├── translate_novel.py         # Script dịch thuật hiện có
│   ├── build_bilingual_edition.py # Script biên soạn hiện có
│   ├── render_html.py             # Script dàn trang HTML hiện có
│   ├── generate_pdf.py            # Script xuất PDF hiện có
│   └── create_study_companion.ts # Trình tạo companion PDF nguyên bản
├── tests/
│   ├── test_bilingual_edition.py # Kiểm thử các tài sản hiện có
│   └── study_companion.test.ts   # Kiểm thử PDF companion
├── package.json                 # Lệnh build/test TypeScript
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
## 6. Cẩm nang TypeScript và dàn trang PDF

Bản cập nhật tạo một **PDF companion riêng**, không thay thế ấn bản song ngữ sẵn có:

```bash
npm install
npm run build:guide
npm test
npx tsc --noEmit
```

Đầu ra: `output/neuromancer_english_study_companion.pdf`. Trình tạo dùng TypeScript, `pdf-lib` và phông chữ Unicode DejaVu Sans/Liberation Sans. Có thể đặt `NEUROMANCER_FONT` trỏ tới tệp TTF nếu phông chữ hệ thống không ở đường dẫn mặc định.

Astryx tại `https://github.com/facebook/astryx` hiện chuyển hướng tới kho Meta Astryx. CLI của Astryx là bộ công cụ design-system/UI, không phải trình tạo PDF. Bản cập nhật đã dùng CLI để tra cứu token màu và spacing; bố cục PDF áp dụng các giá trị semantic tương ứng, còn việc ghi PDF do `pdf-lib` thực hiện. Xem `npm run design:tokens` để tra token màu (CLI 0.7.11).

Điểm thi trong bảng trên là mục tiêu học tập, không phải cam kết. Đặc biệt, TOEFL iBT đổi sang thang 1–6 ngày 21/01/2026; theo ETS, yêu cầu 90 ở thang cũ tương ứng khuyến nghị 4.5, không phải 5.0. Nguồn: [ETS — TOEFL iBT Score Scale Update](https://www.ets.org/toefl/institutions/ibt/score-scale-update.html).

*Cẩm nang này là tài liệu học tập không chính thức; không được xác nhận bởi tác giả, nhà xuất bản hay đơn vị tổ chức kỳ thi.*
