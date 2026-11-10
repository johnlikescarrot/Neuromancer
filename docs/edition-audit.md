# Đánh giá hiện trạng ấn bản

Đánh giá ngày 2026-11-10, dựa trên dữ liệu trong kho lưu trữ. Đây là bước kiểm tra sơ bộ, không phải chứng nhận chất lượng bản dịch hay học liệu.

## Phạm vi và giới hạn

- EPUB và dữ liệu trích xuất có trong kho. Dữ liệu ghi nhận 5 phần, 24 chương và 2.598 đoạn; số lượng này tự nó không chứng minh rằng việc trích xuất là chính xác hoặc đầy đủ so với một bản in có thẩm quyền.
- Cache có 2.598 khóa tương ứng, nhưng bản dịch được tạo bằng dịch máy và chưa có bằng chứng được biên tập hoặc đánh giá độc lập. Không thể suy ra chất lượng văn học từ số lượng khóa.
- Kiểm tra đối chiếu chính xác tìm thấy 36 đoạn trong cache giống hệt nguồn. Nhiều đoạn chỉ chứa tên riêng, số hoặc văn bản cách chữ, nên không thể kết luận tất cả đều sai. Một trường hợp cần biên tập là khóa `3_10_7` (thành ngữ tiếng Anh chưa được chuyển ngữ). Các đoạn khác vẫn cần kiểm tra nghĩa và ngữ cảnh, kể cả khi hai bên khác nhau.
- Tập PDF hiện tại là sản phẩm cũ, không được tái thiết kế hay xác nhận chất lượng trong thay đổi này. Chỉ kiểm tra kích thước và chữ ký PDF không chứng minh chất lượng trình bày, khả năng tìm kiếm, khả năng tiếp cận hoặc tính toàn vẹn.
- Điểm thi là mục tiêu học tập do người dùng nêu, không phải chứng nhận hay dự đoán kết quả. Một tiểu thuyết song ngữ không thể tự mình đảm bảo các kỹ năng nghe, nói, viết và định dạng từng bài thi.

## An toàn dịch thuật

Trước đây nếu dịch máy thất bại sau các lần thử, chương trình chép nguyên văn tiếng Anh vào trường tiếng Việt. Chương trình hiện báo lỗi thay vì âm thầm tạo bản dịch giả. Cache cũ vẫn cần được kiểm tra thủ công; thay đổi này không sửa các bản dịch đã tồn tại.

## Astryx và hướng triển khai

[Astryx](https://github.com/facebook/astryx) là hệ thống thiết kế React, không phải công cụ biên tập hoặc xuất PDF. Tài liệu chính thức nêu React 19+, component, CSS và theme; một ứng dụng TypeScript/React có thể dùng nó để tạo giao diện và sau đó cần một bộ máy in HTML sang PDF riêng. Cần kiểm thử các trang in, font tiếng Việt, phân trang, liên kết và trích xuất văn bản thực tế trước khi thay thế PDF.

## Công việc còn lại

1. Xác minh quyền sử dụng và xuất bản nội dung trước khi phân phối bản dịch.
2. Rà soát EPUB, đối chiếu từng đoạn với nguồn và biên tập tiếng Việt bởi người có năng lực dịch văn học; rà soát trường hợp bản dịch bị bỏ sót, lặp hoặc sai ngữ cảnh.
3. Kiểm chứng từng chú giải bằng nguồn đáng tin cậy, loại bỏ các khẳng định không có căn cứ; phát triển bài tập gốc phù hợp mục tiêu học tập mà không cam kết điểm số.
4. Thiết kế lại bằng TypeScript/React và Astryx, tạo PDF, sau đó kiểm tra bố cục, văn bản trích xuất, khả năng truy cập và đối chiếu nội dung trước khi công bố.
