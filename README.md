# Neuromancer — Bilingual Study Edition

Ấn bản đối sánh **Anh–Việt** kết hợp đọc văn chương Cyberpunk với học liệu phát triển tiếng Anh **B2–C1**. Pipeline xuất bản đã được viết lại bằng **TypeScript**, sử dụng design tokens từ **Astryx Gothic**, phân trang bằng Paged.js, xuất PDF bằng Chromium và bổ sung navigation bằng pdf-lib.

## Thành phẩm

- **PDF:** [`output/neuromancer_bilingual_edition.pdf`](output/neuromancer_bilingual_edition.pdf) — 329 trang A4.
- **Báo cáo build:** [`output/build-report.json`](output/build-report.json) — số trang, checksum SHA-256 và thống kê nguồn.
- **HTML trung gian:** `data/novel_bilingual.html`, chứa toàn bộ CSS/Astryx tokens và có thể xem độc lập.

Ấn bản giữ nguyên dữ liệu hiện có: **5 phần gồm coda, 24 chương, 2.598 cặp đoạn và 25 mục thuật ngữ**. Thiết kế mới gồm bìa editorial, mục lục có số trang/liên kết, running headers, bookmarks PDF, metadata, phụ lục thuật ngữ và sáu module học tập nguyên bản.

> **Phạm vi minh bạch:** dữ liệu dịch cũ được bảo toàn, chưa được tuyên bố là đã hiệu đính toàn diện. Có 36 đoạn tiếng Việt trùng tiếng Anh; phần lớn là tên riêng, mốc giờ hoặc chuỗi ký tự cố ý giữ nguyên. Tất cả được đánh dấu để rà soát theo ngữ cảnh, không bị pipeline tự ý thay bằng bản dịch mới. Các ví dụ ngữ pháp trong study guide được gọi đúng là **ví dụ học thuật minh họa**, không mặc định là trích dẫn nguyên tác.

## Định hướng năng lực

| Bài thi | Mốc mục tiêu của học liệu | Trọng tâm |
|---|---:|---|
| IELTS | 7.0 | Lexical Resource, Grammatical Range, đọc lập luận |
| TOEFL iBT | 90 trước 21/01/2026 / 5 từ 21/01/2026 | Inference, Rhetorical Purpose, Reading to Learn |
| Cambridge English | 185, C1 Advanced | Use of English, sắc thái, biến đổi cấu trúc |
| PTE Academic | 65 | Từ vựng trong ngữ cảnh, tóm tắt, xử lý văn bản |
| DET | 120 | Ngữ cảnh câu, nhận diện từ, sản xuất ngôn ngữ |

Đây là **định hướng học tập**, không phải bảo đảm điểm số hay bảng quy đổi chính thức. Ngườ i học cần kết hợp đề mẫu và rubric hiện hành của tổ chức thi.

## Sáu module học tập

1. Chu trình đọc bốn lượt, ghi chú tối giản và spaced retrieval.
2. Bóc tách câu dài, suy luận có bằng chứng và rhetorical purpose.
3. Word family, collocation, register và paraphrase theo cấu trúc.
4. Xây dựng đoạn lập luận, đảo ngữ/câu chẻ có chọn lọc, tự hiệu đính.
5. Chuyển giao kỹ năng sang IELTS, TOEFL, Cambridge, PTE và DET.
6. Kế hoạch bốn tuần với chẩn đoán, sản xuất và đánh giá lại.

## Chạy pipeline

Yêu cầu **Node.js 22+**.

```bash
npm ci
npm run build   # render HTML → phân trang → PDF → report
npm test        # typecheck + unit tests + kiểm tra dữ liệu/PDF
```

Các lệnh riêng:

```bash
npm run render
npm run pdf
npm run typecheck
```

`@sparticuz/chromium` cung cấp Chromium qua npm để build không phụ thuộc CDN trình duyệt. Pipeline tự giải nén thư viện tương thích khi cần. Có thể dùng Chromium cài sẵn:

```bash
CHROMIUM_PATH=/path/to/chromium npm run pdf
```

## Cấu trúc TypeScript

```text
src/
├── types.ts           # Kiểu dữ liệu và thống kê nguồn
├── study-material.ts  # Học liệu B2–C1 nguyên bản
├── styles.css         # Hệ thống dàn trang A4 / Paged.js
├── render.ts          # Escape HTML và render toàn bộ ấn bản
├── pdf.ts             # Chromium, pagination, bookmarks, metadata, report
└── validate.ts        # Đối chiếu nguồn, HTML và PDF đầu ra
tests/
├── pipeline.test.ts        # Unit tests cho TypeScript renderer
└── test_bilingual_edition.py # Kiểm tra legacy vẫn được giữ
```

`data/bilingual_novel.json` là dữ liệu đầu vào bất biến trong pipeline mới. Các script Python cũ được giữ để tham chiếu lịch sử, nhưng không còn cần cho quy trình xuất bản chính.

## Quyết định thiết kế Astryx

[`facebook/astryx`](https://github.com/facebook/astryx) hiện chuyển hướng sang `meta/astryx`. Astryx là design system React/StyleX đang ở beta; theme Gothic cung cấp typography và color tokens phù hợp editorial. Dự án dùng chính package `@astryxdesign/theme-gothic` và embed `theme.css`, tránh kéo React vào tài liệu in tĩnh. Lớp CSS in ấn cục bộ override text tokens để bảo đảm tương phản trên giấy trắng, đồng thời giữ dark surfaces cho bìa và part dividers.

Tác phẩm gốc và bản dịch thuộc quyền của các chủ sở hữu tương ứng. Học liệu bổ sung và mã nguồn pipeline phục vụ mục đích học tập, không thay thế ấn bản xuất bản chính thức.
