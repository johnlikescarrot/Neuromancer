# Neuromancer — Bilingual Learning Companion

**An original English–Vietnamese study companion, not a translation or replacement of William Gibson’s novel.**

## Phạm vi / Scope

- Bao quát 24 chương và phần kết bằng tóm tắt, phân tích, câu hỏi và hoạt động học ngôn ngữ mới do dự án biên soạn.
- Không dịch toàn văn, không tái bản nguyên tác, không đưa các đoạn trích dài vào PDF.
- Dùng cùng một cuốn tiểu thuyết hợp pháp mà người đọc có quyền truy cập; số chương là mốc đối chiếu, không phải số trang.
- Hướng tới người học B2 tiến lên C1; các mục tiêu điểm thi là đích luyện tập, không phải chứng nhận tương đương hay cam kết kết quả.
- PDF là sản phẩm chính; nội dung có cấu trúc và mã dựng được lưu riêng để kiểm tra, sửa lỗi và tái lập.

The novel remains copyrighted. Availability in this repository or on the Internet Archive does not establish a licence to translate or redistribute it. This directory adds original pedagogy only. Existing archive files are left untouched.

## Build

Python 3.11+; dependencies are listed in `requirements.txt`. Fonts are Be Vietnam Pro, distributed under the SIL Open Font License in `fonts/OFL.txt`.

```sh
python -m venv .venv
.venv/bin/pip install -r edition/requirements.txt
.venv/bin/python edition/tools/audit_source.py
.venv/bin/python edition/tools/build_pdf.py
.venv/bin/python edition/tools/validate.py
```

Output: `edition/Neuromancer-Bilingual-Learning-Companion.pdf`.

## Editorial method

1. Inspect all repository files and the EPUB package, metadata, navigation and chapter structure.
2. Record reproducible counts and source limitations without exporting the novel.
3. Write independent bilingual chapter overviews; distinguish plot, inference and real-world facts.
4. Create original examples and exercises; do not disguise source sentences as teaching examples.
5. Check coverage, answer keys, Vietnamese glyph support, PDF navigation and rendering.

## Review workflow

Work stays on the session’s fixed Arena branch. GitHub permits only one open PR per head branch, so the initial PR receives frequent incremental commits rather than duplicate PRs. No PR is merged by the agent.
