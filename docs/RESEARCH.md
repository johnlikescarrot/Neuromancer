# Kiểm kê nguồn và quyết định biên tập

Ngày kiểm tra: **07/11/2026**. Tài liệu này tách các dữ kiện kiểm chứng được khỏi các mục tiêu biên tập chưa hoàn thành.

## 1. Nguồn được cung cấp

Kho chứa `neuromancer.epub` cùng metadata/torrent/thumbnail của Internet Archive item `neuromancer_202209`. `README.md` ban đầu chỉ có tựa `# Neuromancer`, không mô tả ấn bản hoặc giấy phép.

Metadata XML ghi:

- creator: William Gibson; date: 1984-07-01; language: English;
- uploader tự mô tả EPUB là bản tự tạo từ các plain-text version trên mạng, tiền xử lý để dễ đọc;
- ngày tải lên archive: 21/09/2022;
- không có giấy phép dịch, phát hành lại hoặc xác nhận quyền của chủ sở hữu nguyên tác.

EPUB là EPUB 3 do Pandoc tạo ngày 21/09/2022, UUID `6c139d53-b882-4f65-9825-d41e06837943`. Spine gồm `title_page.xhtml`, `ch001.xhtml`, `ch002.xhtml`. Phần thân duy nhất có toàn bộ 24 chương nằm ở `ch002.xhtml` (473.205 byte trong ZIP).

**Kết luận phạm vi:** lời đề tặng và 24 chương/đoạn kết được đưa vào PDF. Trang tựa và danh mục liên kết là paratext điều hướng, được thay bằng trang tựa/mục lục mới; EPUB không có lời tựa học thuật, chú thích cuối sách hay phụ lục tác giả để dịch thêm.

**Giới hạn:** chưa đối chiếu từng dòng với một ấn bản Ace/Penguin được cấp phép. Vì vậy “đầy đủ” nghĩa là đầy đủ nội dung văn học trong tệp nguồn, không phải chứng nhận textual collation với mọi ấn bản in.

## 2. Kiểm kê cấu trúc toàn văn

Số từ là token phân tách bằng khoảng trắng sau khi hợp nhất whitespace; số này dùng để kiểm soát sản xuất, không phải thống kê từ vựng ngôn ngữ học.

| Chương | Phần | Đoạn | Từ tiếng Anh |
|---:|---|---:|---:|
| 1 | PART ONE - CHIBA CITY BLUES | 221 | 8,132 |
| 2 | PART ONE - CHIBA CITY BLUES | 166 | 4,287 |
| 3 | PART TWO - THE SHOPPING EXPEDITION | 119 | 3,651 |
| 4 | PART TWO - THE SHOPPING EXPEDITION | 125 | 5,002 |
| 5 | PART TWO - THE SHOPPING EXPEDITION | 85 | 2,803 |
| 6 | PART TWO - THE SHOPPING EXPEDITION | 47 | 1,448 |
| 7 | PART TWO - THE SHOPPING EXPEDITION | 136 | 4,108 |
| 8 | PART THREE - MIDNIGHT IN THE RUE JULES VERNE | 137 | 3,074 |
| 9 | PART THREE - MIDNIGHT IN THE RUE JULES VERNE | 125 | 2,699 |
| 10 | PART THREE - MIDNIGHT IN THE RUE JULES VERNE | 157 | 4,205 |
| 11 | PART THREE - MIDNIGHT IN THE RUE JULES VERNE | 165 | 4,280 |
| 12 | PART THREE - MIDNIGHT IN THE RUE JULES VERNE | 54 | 1,843 |
| 13 | PART FOUR - THE STRAYLIGHT RUN | 54 | 2,006 |
| 14 | PART FOUR - THE STRAYLIGHT RUN | 121 | 3,010 |
| 15 | PART FOUR - THE STRAYLIGHT RUN | 92 | 4,164 |
| 16 | PART FOUR - THE STRAYLIGHT RUN | 147 | 4,175 |
| 17 | PART FOUR - THE STRAYLIGHT RUN | 78 | 3,643 |
| 18 | PART FOUR - THE STRAYLIGHT RUN | 118 | 3,704 |
| 19 | PART FOUR - THE STRAYLIGHT RUN | 60 | 1,951 |
| 20 | PART FOUR - THE STRAYLIGHT RUN | 91 | 3,401 |
| 21 | PART FOUR - THE STRAYLIGHT RUN | 51 | 1,381 |
| 22 | PART FOUR - THE STRAYLIGHT RUN | 90 | 2,241 |
| 23 | PART FOUR - THE STRAYLIGHT RUN | 108 | 2,518 |
| 24 | CODA - DEPARTURE AND ARRIVAL | 50 | 1,218 |
| **Tổng** | **4 phần + coda** | **2,597** | **78,944** |

Lời đề tặng nguồn:

> for Deb<br/>
> who made it possible with love

Bản Việt biên tập: “Dành cho Deb, / người đã giúp hiện thực hóa cuốn sách này bằng tình yêu.”

## 3. Quyết định dịch và đối chiếu

- **Không rút gọn:** mỗi một trong 2.597 đoạn nguồn phải có đúng một record Việt với hash tiếng Anh tương ứng.
- **ID ổn định:** `chXX-pYYYY`; đơn vị dịch thêm hậu tố `uZZZ`. ID là đơn vị review, không phải số trang của ấn bản in.
- **Ngữ cảnh gần:** pysbd chia câu rồi gom tới 320 token SentencePiece; câu quá dài được chia đệ quy, ghép lại phải khớp nguyên văn trước khi gọi model.
- **Không giấu nguồn gốc bản dịch:** `machine-draft` và `human-reviewed` là hai trạng thái khác nhau, hiển thị cả trong dữ liệu và PDF.
- **Thuật ngữ theo ngữ cảnh:** giữ các tên như `deck`, `joeboy`, `Neuromancer`; giải thích ICE, simstim, construct, meat… trong phụ lục thay vì áp một nghĩa cho mọi câu.
- **Không tự nhận “tốt nhất”:** QuickMT tạo bản nháp toàn văn. Chất lượng văn học cần rà soát độc lập, đặc biệt đại từ, tiếng lóng, nhịp noir, danh từ tự tạo, câu thoại và ẩn dụ.
- **Không phát tán trọng số/PDF qua Git history:** model nằm trong cache; PDF/QA cuối ở release; dữ liệu dịch và cấu hình review được commit.

## 4. Mục tiêu học và nguồn thang điểm

Các mục tiêu trong yêu cầu không tạo thành một hàng tương đương CEFR. Ấn bản giữ nguyên mục tiêu của người học nhưng ghi chú khác biệt:

| Bài thi | Mục tiêu yêu cầu | Ghi chú nghiên cứu |
|---|---:|---|
| TOEFL iBT trước 21/01/2026 | 90 | ETS khuyến nghị yêu cầu 90 cũ chuyển sang **4,5** trên thang mới; không phải 5. |
| TOEFL iBT từ 21/01/2026 | 5 | **C1**; bảng ETS cho tổng điểm tham chiếu từ 95/120. |
| IELTS | 7,0 | **C1** theo IELTS. |
| PTE Academic | 65 | **B2** theo thang CEFR của Pearson; bảng PTE–IELTS và PTE–CEFR là hai phép đối chiếu khác nhau. |
| Cambridge C1 Advanced / C2 Proficiency | 185 | **C1** trên Cambridge English Scale; C2 Proficiency 180–199 được báo cáo Level C1. |
| Duolingo English Test | 120 | **B2** theo công bố CEFR 2026; C1 là 130–150. |

Nguồn chính thức (truy cập 07/11/2026):

1. ETS, *Understanding TOEFL iBT scores*: https://www.ets.org/toefl/test-takers/ibt/scores/understand-scores.html
2. IELTS, *Everything you need to know about IELTS and the CEFR*: https://ielts.org/news-and-insights/everything-you-need-to-know-about-ielts-and-the-cefr
3. Pearson, *Specification for PTE Academic*: https://www.pearsonpte.com/content/dam/ELL/pte/pearsonpte/policy-and-help-center/documents/Specification-for-PTE-Academic-V7-June-2022.pdf
4. Cambridge English, *The Cambridge English Scale — information for institutions*: https://www.cambridgeenglish.org/exams-and-tests/cambridge-english-scale/institutions/
5. Duolingo English Test, *Is the Duolingo English Test aligned with the CEFR?*: https://blog.englishtest.duolingo.com/duolingo-test-aligned-with-cefr/

Không suy ra rằng đọc xong tiểu thuyết sẽ đạt điểm. Sách hỗ trợ trực tiếp đọc hiểu/từ vựng/phong cách; nghe, nói, viết, tốc độ và chiến thuật bài thi cần luyện riêng.

## 5. Kiểm chứng kỹ thuật

### Trước PDF

- 24 chương liên tục, 2.597 ID không trùng; lời đề tặng đúng nguồn.
- Toàn bộ key Anh–Việt khớp nhau; SHA-256 từng đoạn và EPUB khớp.
- Không bản Việt rỗng, ký tự điều khiển, `<unk>`, token SentencePiece hoặc vòng lặp sáu từ lặp ít nhất bốn lần.
- Cảnh báo tỷ lệ độ dài, tên riêng bị mất, văn bản quá giống tiếng Anh hoặc không có dấu Việt được lưu để con người xem, không tự động kết luận lỗi dịch.

### Sau PDF

- Mở lại bằng PyMuPDF; đủ mã đoạn, câu mở đầu, đoạn cuối và lời đề tặng song ngữ.
- Có metadata, outline/mục lục, liên kết, text layer và font nhúng.
- Không có text block vượt khỏi trang; ghi nhận trang trống để rà soát.
- Ghi SHA-256 và kích thước chính xác của artifact vào `qa-report.json`.

QA tự động không chấm BLEU vì không có bản dịch tham chiếu độc lập; dùng một bản dịch khác làm “đáp án” sẽ tạo cảm giác chính xác giả.

## 6. Quy trình biên tập tiếp theo nếu mục tiêu là ấn bản xuất bản

1. Rà soát toàn bộ theo chương bởi biên tập viên Anh–Việt có kinh nghiệm SF; ưu tiên chương 1, các cảnh chuyển POV/simstim và phần Straylight.
2. Lập translation memory cho quyết định thuật ngữ theo từng nghĩa, không chỉ song ngữ từ–từ.
3. Rà chéo một mẫu phân tầng theo phần/chương/loại văn bản (thoại, miêu tả, ma trận); ghi lỗi nghĩa, sót/thêm ý, danh từ, giọng, cú pháp và chính tả.
4. Đọc tiếng Việt độc lập để sửa nhịp, sau đó đối chiếu hai chiều để tránh “trôi nghĩa”.
5. Chỉ nâng trạng thái từng đoạn qua `overrides.json`; chạy lại QA và diff PDF sau mỗi PR.
6. Xin xác nhận quyền trước phát hành công khai/thương mại khi luật hiện hành yêu cầu.

Đây là lộ trình còn lại, không phải công việc đã hoàn thành trong bản máy hỗ trợ.
