# Neuromancer
## Neuromancer — Ấn Bản Song Ngữ Anh - Việt (Bilingual Master Edition)

Ấn bản song ngữ Anh - Việt toàn diện và chuyên sâu của tác phẩm kinh điển **Neuromancer** (William Gibson) được thiết kế đặc biệt nhằm phục vụ độc giả yêu thích văn học khoa học viễn tưởng (Cyberpunk) và người học tiếng Anh học thuật hướng đến các chuẩn đầu ra quốc tế cao cấp:
- **IELTS Academic:** Band 7.0 - 8.5
- **TOEFL iBT:** 90 - 110 Điểm (trước 21/01/2026) / Cấp độ 5 (từ 21/01/2026 trở đi)
- **Cambridge English Qualifications:** 185 - 200+ Điểm (C1 Advanced / C2 Proficiency)
- **PTE Academic:** 65 - 85 Điểm
- **Duolingo English Test (DET):** 120 - 145 Điểm

### Các tính năng chính của ấn bản:
1. **Toàn diện cấu trúc tác phẩm:** Bao quát toàn bộ 24 chương và 5 phần lớn (Part One: Chiba City Blues, Part Two: The Shopping Expedition, Part Three: Midnight in the Rue Jules Verne, Part Four: The Straylight Run, Coda: Departure and Arrival).
2. **Bố cục đối chiếu song ngữ song song:** Văn bản nguyên tác tiếng Anh được trình bày song song cùng bản dịch tiếng Việt văn chương trau chuốt, chính xác về văn phong Cyberpunk Noir.
3. **Từ điển & Thuật ngữ Cyberpunk:** Chú giải chi tiết các khái niệm nền tảng do Gibson sáng tạo (*Cyberspace, Deck, Console Cowboy, ICE, Simstim, Zaibatsu, Dermatrodes, The Meat*).
4. **Hệ thống phân tích từ vựng C1/C2 & Collocations học thuật:** Mỗi chương đi kèm phân tích ngữ pháp phức hợp, mẹo làm bài thi chuẩn hóa quốc tế và danh mục từ vựng học thuật tinh hoa.
5. **Định dạng xuất bản PDF chuyên nghiệp:** Được biên soạn tự động qua ReportLab với hệ font chữ Unicode tiếng Việt đầy đủ (`DejaVuSerif`, `DejaVuSans`), bố cục trang in, header/footer và số trang tự động.

### Hướng dẫn tạo tệp PDF từ mã nguồn:
```bash
# 1. Trích xuất văn bản từ tệp EPUB gốc:
python3 scripts/extract_text.py

# 2. Biên dịch và xuất bản tệp PDF song ngữ:
python3 scripts/generate_pdf.py

# Thành phẩm PDF sẽ được tạo tại: Neuromancer_Bilingual_Edition.pdf
```
