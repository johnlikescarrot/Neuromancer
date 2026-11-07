# Neuromancer — ấn bản song ngữ Anh–Việt

Quy trình này tạo một **PDF học tập Anh–Việt đầy đủ** từ `neuromancer.epub` do người dùng cung cấp: lời đề tặng, bốn phần, 24 chương và đoạn kết; tiếng Anh và tiếng Việt được đặt xen kẽ theo đoạn với ID truy vết ổn định.

> **Trạng thái chất lượng:** đây là bản dịch **máy hỗ trợ**, có cơ chế đánh dấu rà soát thủ công. Kiểm tra tự động xác nhận độ phủ và tính toàn vẹn của tệp, không chứng minh chất lượng văn học. Không gọi đây là “bản dịch tốt nhất” khi chưa có biên tập song ngữ độc lập toàn sách.

## Kết quả

Khi workflow hoàn tất, tải hai tệp từ release **`bilingual-learning-latest`**:

- `Neuromancer-EN-VI-Bilingual.pdf` — ấn bản song ngữ, có mục lục/bookmark, font Unicode nhúng, text layer và liên kết thuật ngữ.
- `qa-report.json` — kiểm tra độ phủ 2.597 đoạn, lỗi định dạng, số trang, font, liên kết, điểm đầu/cuối và SHA-256 của PDF.

PDF và model là sản phẩm sinh/tệp lớn nên nằm ở release/artifact, không bị commit lặp lại vào Git. Dữ liệu dịch `translation/vi.json` và QA cấu trúc `translation/qa.json` được commit để review trong PR.

## Kiểm kê nguồn

| Hạng mục | Kết quả |
|---|---:|
| Tác giả / tựa | William Gibson / *Neuromancer* |
| EPUB SHA-256 | `c1c38a9fbf06a36ad86054e7e11083c95d3d20d0f3988ac01c12ca7553b4ba60` |
| Lời đề tặng | Có, song ngữ trên trang riêng |
| Phần + đoạn kết | 4 + 1 |
| Chương | 24, đánh số liên tục |
| Đoạn thân bài | 2.597 |
| Từ thân bài tiếng Anh | 78.944 (tách bằng khoảng trắng sau chuẩn hóa) |
| Tài liệu thân bài trong EPUB | `EPUB/text/ch002.xhtml` |

`EPUB/text/ch001.xhtml` chứa tựa, mục lục và lời đề tặng; `title_page.xhtml` là trang tựa. Không có chú thích, phụ lục hoặc lời bình của tác giả trong EPUB này. Việc đủ 24 chương chứng minh tính đầy đủ **theo cấu trúc của tệp nguồn**, chưa phải đối chiếu từng dòng với một ấn bản in được cấp phép.

Nguyên tác vẫn có bản quyền. Metadata Internet Archive mô tả đây là EPUB tự tạo từ plain text trên mạng, không cấp giấy phép dịch hoặc phát hành lại. Người phát hành cần tự xác định quyền sử dụng theo luật hiện hành; ghi công không thay thế cho giấy phép khi giấy phép là bắt buộc.

## Thiết kế cho người học

- Trình bày Anh trước, Việt sau; mã như `ch01-p0001` dùng để trích dẫn khi báo lỗi.
- Hướng dẫn bốn lượt đọc: ngữ cảnh → đối chiếu → ngôn ngữ → thu hồi.
- Phụ lục 40 mục thuật ngữ/địa danh cyberpunk, có liên kết tới lần xuất hiện đầu tiên tìm được.
- Phụ lục mô tả pipeline, giới hạn và cách đóng góp bản dịch thay thế có truy vết.
- Mục tiêu TOEFL, IELTS, PTE, Cambridge và DET được trình bày **không đồng nhất**. Theo các nguồn chính thức được tra ngày 07/11/2026: TOEFL 90 cũ được ETS khuyến nghị chuyển thành 4,5; TOEFL 5 mới và IELTS 7,0 thuộc C1; Cambridge 185 là C1; PTE 65 và DET 120 thuộc B2 theo bảng CEFR của Pearson/Duolingo. Sách hỗ trợ đọc B2→C2, không cam kết điểm thi hoặc thay thế luyện nghe/nói/viết.

Nguồn và bảng chi tiết nằm trong `edition/editorial.json` và phần đầu PDF.

## Tái tạo cục bộ

Yêu cầu: Python 3.11, các font DejaVu tại `/usr/share/fonts/truetype/dejavu`, khoảng 1 GB RAM cho dịch và dung lượng cho model/PDF.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt

# Tải model QuickMT Anh→Việt, bản CTranslate2 int8; kiểm tra kích thước/SHA-256.
python scripts/download_model.py

python scripts/extract_source.py
python scripts/translate.py --beam-size 4
python scripts/qa.py --output translation/qa.json
python scripts/build_pdf.py
python scripts/qa.py \
  --pdf dist/Neuromancer-EN-VI-Bilingual.pdf \
  --output dist/qa-report.json
```

Dịch một nhóm chương hoặc tiếp tục từ checkpoint:

```bash
python scripts/translate.py --chapters 1 6 12 18 \
  --output build/vi-group-01.json \
  --checkpoint build/units-group-01.jsonl
```

Checkpoint ghi sau mỗi lô; tệp tổng hợp ghi sau mỗi chương. SHA-256 của từng đoạn/đơn vị ngăn dùng nhầm bản dịch cho nguồn đã thay đổi.

## GitHub Actions

Workflow `.github/workflows/build-bilingual.yml` chạy thủ công (`workflow_dispatch`):

1. Tải/verify và cache model; chạy unit test.
2. Dịch 24 chương trong sáu job song song, mỗi job tạo một artifact nhóm.
3. Ghép đủ sáu nhóm; từ chối nếu thiếu, trùng ID hoặc khác nguồn.
4. Chạy QA, dựng PDF, mở lại PDF để kiểm tra.
5. Commit dữ liệu dịch/QA vào **cùng nhánh làm việc**, tải artifact và cập nhật release.
6. Không merge PR và không đụng vào `main`.

Chạy bằng `gh`:

```bash
gh workflow run build-bilingual.yml \
  --ref arena/8c970cb2-neuromancer -f beam_size=4
gh run list --workflow=build-bilingual.yml --limit 3
```

## Review bản dịch

- Kết quả máy nằm trong `translation/vi.json`, trạng thái `machine-draft`.
- Bản thay thế đã rà soát nằm trong `translation/overrides.json`, theo paragraph ID; khi chạy lại, đoạn đó được ghi `human-reviewed`.
- Không sửa tay rồi để nguyên trạng thái máy; không thay đổi ID để tái sử dụng checkpoint.
- `edition/editorial.json` chứa tên phần, lời đề tặng, thuật ngữ và dữ liệu hướng dẫn học.

## Kiểm thử

```bash
python -m unittest discover -s tests -v
python scripts/qa.py --output build/translation-qa.json
```

Các kiểm tra bắt buộc gồm: đủ chương/đoạn, hash nguồn, không rỗng/token lỗi/ký tự điều khiển, phát hiện vòng lặp, PDF có đủ mã đoạn và text layer. Cảnh báo tên riêng, tỷ lệ độ dài hoặc nghi vấn chưa dịch cần con người đánh giá theo ngữ cảnh.

## Ghi công model

- Model gốc: **QuickMT English→Vietnamese**, CC BY 4.0.
- Bản chuyển đổi: [`thiennq/quickmt-en-vi-ct2-int8`, release `v1`](https://github.com/thiennq/quickmt-en-vi-ct2-int8/releases/tag/v1).
- Thư viện: CTranslate2, SentencePiece, pysbd, ReportLab, PyMuPDF, Beautiful Soup.

Chi tiết kiểm kê chương và nghiên cứu nguồn: [`docs/RESEARCH.md`](docs/RESEARCH.md).
