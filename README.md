# Neuromancer — ấn bản đối chiếu Anh–Việt

PDF A4 tại [`output/neuromancer_bilingual_edition.pdf`](output/neuromancer_bilingual_edition.pdf) sử dụng dữ liệu đã có trong kho, dàn trang lại bằng TypeScript, React và [Astryx](https://github.com/facebook/astryx) (`@astryxdesign/core` và theme Neutral). Mục lục PDF có liên kết đến chương; mỗi cặp đoạn giữ mã để tiện rà soát. Phần cuối có từ điển kế thừa và bài tập đọc tự luyện.

## Giới hạn quan trọng

- **Đây chưa phải bản dịch hoàn chỉnh đã hiệu đính.** Phần lớn bản dịch có sẵn là bản dịch máy; hai câu tiếng Anh còn nguyên đã được dịch, nhưng chất lượng, sự đầy đủ và sự tương ứng với EPUB của toàn bộ văn bản chưa được kiểm chứng. Trình dựng đánh dấu các đoạn trống hoặc giống nguyên bản; số này bao gồm tên riêng, dấu thời gian và chữ bị tách, nên không thể coi toàn bộ là lỗi dịch. Một số lỗi không được phát hiện bằng cách so chuỗi.
- Dữ liệu trích xuất tách văn bản theo dòng HTML, có thể làm sai ranh giới đoạn và trình bày. Cần so sánh trực tiếp EPUB, hiệu đính bởi người có năng lực ngôn ngữ và kiểm tra quyền sử dụng trước khi chia sẻ hay xuất bản. Không gửi văn bản tới dịch vụ bên ngoài nếu chưa có quyền và căn cứ phù hợp.
- Các hướng dẫn chương cũ chưa được kiểm chứng, một số ví dụ tự viết từng bị gắn nhãn trích dẫn; chúng **không** được đưa vào PDF mới. Từ điển kế thừa cũng cần kiểm tra độc lập. Không có chứng nhận từ các tổ chức thi hay cam kết đạt điểm.
- Các mốc IELTS 7.0, TOEFL iBT 90 trước 21/01/2026 / 5 từ ngày đó, PTE Academic 65, Cambridge English 185 và DET 120 là **mục tiêu riêng**, không phải các điểm tương đương. Theo [ETS](https://www.ets.org/toefl/institutions/ibt/score-scale-update.html), cơ sở đang yêu cầu TOEFL 90 được khuyến nghị đặt mức 4,5 theo thang mới; mức 5 là mục tiêu cao hơn. [Cambridge](https://www.cambridgeenglish.org/exams-and-tests/qualifications/results/) xếp 185 ở C1, kể cả trên bài C2 Proficiency; [Duolingo](https://blog.englishtest.duolingo.com/duolingo-test-aligned-with-cefr/) xếp DET 120 trong khoảng B2. Yêu cầu nhập học và quy đổi phụ thuộc từng tổ chức.

## Dựng và kiểm thử

Yêu cầu Node.js 22+, Python 3 và Linux x64 với các thư viện hệ thống Chromium (bao gồm NSS/NSPR), cùng font DejaVu Sans/Serif có hỗ trợ tiếng Việt. Trên hệ thống khác đặt `CHROMIUM_PATH` trỏ tới Chromium tương thích; phiên bản cài sẵn `@sparticuz/chromium` dành cho Linux x64. `npm ci` cài đúng các phiên bản trong lockfile.

```sh
npm ci
npm run build              # data/bilingual_novel.json → HTML → PDF
npm test                   # kiểm tra TypeScript và cấu trúc dữ liệu/HTML/PDF
```

Trình dựng ghi đè `data/novel_bilingual.html` và PDF. Không chạy các script Python cũ để dựng PDF: đó là pipeline lịch sử. `scripts/translate_novel.py` gửi dữ liệu tới Google Translate và có thể giữ nguyên bản gốc khi thất bại; không dùng làm bằng chứng bản dịch hoàn thiện. Bộ kiểm thử không xác nhận tính chính xác của bản dịch, cách dàn trang trên mọi môi trường, hay độ tin cậy các chú giải.

### Thành phần

- `neuromancer.epub`: nguồn đầu vào trong kho.
- `data/extracted_novel.json`, `data/translated_cache.json`, `data/bilingual_novel.json`: dữ liệu trích xuất, bản dịch máy và dữ liệu đối chiếu.
- `scripts/edition.tsx`: thành phần Astryx, dàn trang in, dựng HTML và PDF bằng Playwright/Chromium.
- `data/novel_bilingual.html`, `output/neuromancer_bilingual_edition.pdf`: sản phẩm đã dựng.
- `tests/`: kiểm tra tự động. Các script Python khác là pipeline cũ.
