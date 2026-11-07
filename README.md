# Neuromancer — William Gibson
## Ấn Bản Song Ngữ Anh - Việt Toàn Diện & Chuẩn Mực Học Thuật (Comprehensive Bilingual EN-VI Edition)

Dự án biên soạn và dịch thuật tác phẩm kinh điển khoa học viễn tưởng **Neuromancer** (1984) của William Gibson thành ấn bản song ngữ Anh - Việt hoàn chỉnh, định dạng PDF chất lượng cao, tích hợp hệ thống chú giải học thuật phục vụ người học tiếng Anh nâng cao hướng tới các chuẩn điểm khảo thí quốc tế.

---

### 🎯 Khung Mục Tiêu Năng Lực Tiếng Anh (Target Exam Benchmarks)
Ấn bản được thiết kế để hỗ trợ đắc lực độc giả đạt được các mốc năng lực ngôn ngữ học thuật hàng đầu:
- **TOEFL iBT**: **90 điểm** (đối với kỳ thi trước ngày 21/01/2026) / **5 điểm** (thang điểm mới áp dụng từ 21/01/2026 trở đi).
- **IELTS Academic**: **7.0+** (Good user / C1 Operational Command).
- **PTE Academic**: **65 điểm**.
- **Cambridge English Qualifications**: **185 điểm** (Trình độ C1 Advanced hoặc C2 Proficiency).
- **Duolingo English Test (DET)**: **120+ điểm**.

---

### 📖 Đặc Trưng Nổi Bật Của Ấn Bản
1. **Đối chiếu đoạn song song (Parallel Bilingual Reading)**: Văn bản tiếng Anh gốc của William Gibson và bản dịch tiếng Việt văn học chuẩn mực được đặt song song từng đoạn, giúp người đọc vừa thưởng thức được phong cách cyberpunk sắc lạnh, vừa rèn luyện kỹ năng dịch thuật và cảm thụ văn phong.
2. **Khung từ vựng học thuật & nâng cao (Academic Vocabulary Boxes)**: Mỗi hồi và chương đều tích hợp các hộp từ vựng C1/C2 với phiên âm quốc tế chuẩn IPA, giải nghĩa Anh - Anh học thuật và định nghĩa ngữ cảnh tiếng Việt.
3. **Chú giải văn hóa & công nghệ Cyberpunk (Cyberpunk Footnotes)**: Phân tích nguồn gốc các thuật ngữ mang tính thời đại: *Cyberspace, Matrix, Console Cowboy, ICE (Intrusion Countermeasures Electronics), Street Samurai, Zaibatsu, Arcology...*
4. **Định dạng PDF chuẩn in ấn cao cấp**: Được biên dịch thông qua pipeline tự động hóa sử dụng HTML5/CSS Paged Media và Playwright Chromium engine với typography cổ điển, lề trang tiêu chuẩn, running headers và đánh số trang tự động.

---

### 🛠 Cấu Trúc Dự Án & Hướng Dẫn Biên Dịch (Build Instructions)

```bash
Neuromancer/
├── data/
│   ├── chapters.json          # Toàn bộ 24 chương trích xuất từ nguồn EPUB
│   ├── glossary.json          # Cơ sở dữ liệu thuật ngữ & benchmark khảo thí
│   ├── ch1_vi_cache.json      # Bản dịch đối chiếu Chương 1
│   └── ch2_vi_cache.json      # Bản dịch đối chiếu Chương 2
├── content/
│   ├── ch01_bilingual.json    # Dữ liệu song ngữ & ghi chú Chương 1
│   └── ch02_bilingual.json    # Dữ liệu song ngữ & ghi chú Chương 2
├── templates/
│   ├── book_template.html     # Khung giao diện HTML sách
│   └── book_style.css         # Thiết kế CSS chuẩn trang sách Paged Media
├── scripts/
│   ├── extract_text.py        # Trích xuất và cấu trúc hóa văn bản từ EPUB
│   ├── build_ch1_bilingual.py # Biên soạn song ngữ Chương 1
│   ├── build_ch2_bilingual.py # Biên soạn song ngữ Chương 2
│   └── compile_pdf.py         # Trình biên dịch tạo file PDF sách
├── tests/
│   └── test_translation_pipeline.py # Kiểm thử chất lượng và tính toàn vẹn
└── Neuromancer_Bilingual_Edition.pdf # File PDF sản phẩm cuối cùng
```

#### Các lệnh tạo lại PDF:
```bash
# 1. Trích xuất văn bản từ EPUB
python3 scripts/extract_text.py

# 2. Biên soạn dữ liệu chương song ngữ
python3 scripts/build_ch1_bilingual.py
python3 scripts/build_ch2_bilingual.py

# 3. Biên dịch ra PDF
python3 scripts/compile_pdf.py --output Neuromancer_Bilingual_Edition.pdf

# 4. Chạy kiểm thử tự động
python3 -m unittest discover tests
```
