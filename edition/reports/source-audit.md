# Source audit / Kiểm tra nguồn

## English

The supplied EPUB is an unprotected-by-DRM file, not thereby an uncopyrighted work. It identifies William Gibson as the author. Its archive metadata dates the novel to 1984 and describes a custom conversion from plain text. Public access is not a translation licence.
The structural pass finds **24 numbered chapters**, **4 numbered parts plus a coda**, and **78,967 body words** under the stated counting rule. This is not a print-edition word count.
EPUB SHA-256: `c1c38a9fbf06a36ad86054e7e11083c95d3d20d0f3988ac01c12ca7553b4ba60`.
ZIP integrity: PASS. Broken XHTML navigation links: 0.

| Chapter | Part | Words | Paragraphs |
|---:|---|---:|---:|
| 1 | PART ONE - CHIBA CITY BLUES | 8,129 | 222 |
| 2 | PART ONE - CHIBA CITY BLUES | 4,289 | 167 |
| 3 | PART TWO - THE SHOPPING EXPEDITION | 3,651 | 121 |
| 4 | PART TWO - THE SHOPPING EXPEDITION | 5,032 | 126 |
| 5 | PART TWO - THE SHOPPING EXPEDITION | 2,806 | 86 |
| 6 | PART TWO - THE SHOPPING EXPEDITION | 1,449 | 48 |
| 7 | PART TWO - THE SHOPPING EXPEDITION | 4,108 | 137 |
| 8 | PART THREE - MIDNIGHT IN THE RUE JULES VERNE | 3,074 | 138 |
| 9 | PART THREE - MIDNIGHT IN THE RUE JULES VERNE | 2,697 | 126 |
| 10 | PART THREE - MIDNIGHT IN THE RUE JULES VERNE | 4,207 | 158 |
| 11 | PART THREE - MIDNIGHT IN THE RUE JULES VERNE | 4,280 | 166 |
| 12 | PART THREE - MIDNIGHT IN THE RUE JULES VERNE | 1,843 | 55 |
| 13 | PART FOUR - THE STRAYLIGHT RUN | 2,010 | 55 |
| 14 | PART FOUR - THE STRAYLIGHT RUN | 3,012 | 122 |
| 15 | PART FOUR - THE STRAYLIGHT RUN | 4,164 | 93 |
| 16 | PART FOUR - THE STRAYLIGHT RUN | 4,162 | 148 |
| 17 | PART FOUR - THE STRAYLIGHT RUN | 3,647 | 79 |
| 18 | PART FOUR - THE STRAYLIGHT RUN | 3,693 | 119 |
| 19 | PART FOUR - THE STRAYLIGHT RUN | 1,954 | 61 |
| 20 | PART FOUR - THE STRAYLIGHT RUN | 3,401 | 92 |
| 21 | PART FOUR - THE STRAYLIGHT RUN | 1,381 | 52 |
| 22 | PART FOUR - THE STRAYLIGHT RUN | 2,242 | 91 |
| 23 | PART FOUR - THE STRAYLIGHT RUN | 2,518 | 109 |
| 24 | CODA - DEPARTURE AND ARRIVAL | 1,218 | 50 |

### Editorial cautions

- The archive metadata describes a custom EPUB assembled from online plain text; this is not evidence of public-domain status or permission to translate.
- The EPUB has no ISBN or print-edition statement. Do not invent print page numbers or claim equivalence to a licensed edition.
- The NCX nests later navigation points inside earlier ones; the XHTML navigation document is the clearer structural guide.
- Underscore emphasis survives in some paragraphs. Spelling and punctuation have not been silently corrected against a print edition.
- The final numbered chapter includes a dated inscription and acknowledgements after the narrative; chapter word counts include that paratext.
- This audit exports counts and bibliographic/structural facts only, not the source prose.

## Tiếng Việt

Tệp EPUB được cung cấp xác định tác giả là William Gibson. Siêu dữ liệu lưu trữ ghi năm xuất bản 1984 và mô tả việc dựng EPUB từ văn bản thuần. Khả năng truy cập công khai không đồng nghĩa với phạm vi công cộng hoặc giấy phép dịch.
Kiểm tra cấu trúc ghi nhận **24 chương đánh số**, **4 phần chính và một phần kết**, cùng **78,967 từ thân văn bản** theo quy tắc đếm trong JSON. Không có số trang bản in để đối chiếu.
Mục lục NCX có phân cấp lồng bất thường; mục lục XHTML rõ ràng hơn. Một số dấu nhấn dạng gạch dưới còn sót. Chính tả và dấu câu chưa được hiệu đính theo bản in. Chương 24 có lời đề tặng/ngày tháng và lời cảm ơn sau truyện; số từ chương bao gồm phần này.
Báo cáo chỉ xuất số liệu và cấu trúc, không xuất văn xuôi nguồn. Các tệp gốc không bị sửa.

## Rebuild / Tạo lại

```sh
python -m pip install beautifulsoup4
python edition/tools/audit_source.py
```
