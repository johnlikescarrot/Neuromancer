# Neuromancer — Ấn Bản Song Ngữ Anh – Việt (Bilingual Critical Edition)

> **Tác phẩm:** *Neuromancer* (1984) — William Gibson
> **Dự án:** Biên dịch và biên soạn ấn bản song ngữ Anh – Việt toàn diện, chất lượng cao nhất, tích hợp hệ thống chú giải sư phạm phục vụ nâng cao năng lực tiếng Anh học thuật & chuẩn hóa quốc tế.

---

## 🎯 Mục Tiêu Năng Lực Chuẩn Hóa Quốc Tế

Ấn bản được thiết kế sư phạm chuyên sâu nhằm giúp người học đạt được các mức điểm năng lực:
- **IELTS:** 7.0+ (Band 7–8 Lexical Resources, C1 Collocations & Cohesion)
- **TOEFL iBT:** 90+ (trước 21/01/2026) / 5.0+ (từ 21/01/2026 trở đi)
- **Pearson Test of English (PTE) Academic:** 65+
- **Cambridge English Qualifications:** 185+ (C1 Advanced / C2 Proficiency)
- **Duolingo English Test (DET):** 120+

---

## 📖 Cấu Trúc Dự Án

- `data/chapters/`: 24 chương nguyên tác được trích xuất hoàn chỉnh từ bản EPUB gốc (`chapter_01.json` đến `chapter_24.json`).
- `data/chapters_manifest.json`: Bảng tổng kết số lượng từ và đoạn văn của toàn bộ tác phẩm (~79.000 từ, 2.598 đoạn).
- `data/translated_ch01.json`: Bản dịch song ngữ đối chiếu song song và gán thẻ sư phạm từng đoạn văn cho Chương 1.
- `scripts/extract_text.py`: Công cụ tự động trích xuất các phần, chương, đoạn văn và chuyển đổi định dạng sạch từ `neuromancer.epub`.
- `scripts/pedagogy.py`: Ngân hàng từ vựng học thuật C1/C2, ngữ âm, collocations, ngữ cảnh cyberpunk và chiến thuật làm bài thi.
- `scripts/build_pdf.py`: Engine biên dịch PDF xuất bản sử dụng ReportLab và font chữ Unicode (Liberation Serif & Liberation Sans) hỗ trợ đầy đủ tiếng Việt.
- `tests/test_pdf.py`: Bộ kiểm thử tự động xác minh tính toàn vẹn của dữ liệu và file PDF.
- `Neuromancer_Bilingual_EN_VI.pdf`: Ấn bản PDF hoàn chỉnh được tạo ra.

---

## 🛠 Hướng Dẫn Cài Đặt & Biên Dịch

### 1. Cài đặt các gói phụ thuộc
```bash
pip install reportlab pillow pytest
```

### 2. Trích xuất toàn bộ văn bản từ EPUB
```bash
python3 scripts/extract_text.py
```

### 3. Biên dịch tài liệu PDF song ngữ
```bash
PYTHONPATH=scripts python3 scripts/build_pdf.py
```

### 4. Chạy kiểm thử tự động
```bash
python3 -m pytest tests/
```

---

## 🖋 Nguyên Tắc Dịch Thuật
1. **Bảo tồn âm hưởng Cyberpunk:** Duy trì độ sắc lạnh, nhịp điệu dồn dập (staccato cadence) và hệ thống thuật ngữ công nghệ độc đáo của William Gibson.
2. **Đối chiếu song song:** Mỗi phân đoạn tiếng Anh đi kèm bản dịch tiếng Việt tương ứng, thuận tiện cho việc so sánh phong cách diễn đạt.
3. **Phát triển vốn từ vựng học thuật:** Tích hợp trực tiếp từ vựng nâng cao vào văn cảnh sinh động của tác phẩm, biến trải nghiệm đọc văn học thành công cụ bứt phá điểm số trong các kỳ thi quốc tế.
