# Báo cáo cá nhân — Nguyễn Minh Quân — 2A202603747

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Quân
- MSSV: 2A202603747
- Email: minhquannm0905@gmail.com
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

Tôi phụ trách vai trò người gắn nhãn 1 trong nhiệm vụ phân tích lỗi của pilot.

Các công việc chính:

- Đọc độc lập 20 ca lỗi trong đề bài.
- Gắn nhãn nguyên nhân gốc theo năm nhóm của Google PAIR:
  - Do người dùng
  - Hệ thống
  - Ngữ cảnh
  - Giới hạn hệ thống
  - Ngầm
- Lưu bộ nhãn ban đầu trước khi trao đổi với người gắn nhãn 2.
- So sánh hai bộ nhãn và xác định các ca không đồng thuận.
- Thảo luận để thống nhất nhãn cho các ca khác nhau.
- Tham gia hoàn thiện bảng khắc phục cho năm ca, mỗi loại lỗi một ca.

## 3. Đóng góp cụ thể

Tôi đã hoàn thành bộ 20 nhãn độc lập với kết quả ban đầu như sau:

| Ca | Nhãn ban đầu |
| --: | --- |
| 1 | Do người dùng |
| 2 | Hệ thống |
| 3 | Ngữ cảnh |
| 4 | Giới hạn hệ thống |
| 5 | Ngầm |
| 6 | Do người dùng |
| 7 | Hệ thống |
| 8 | Hệ thống |
| 9 | Ngữ cảnh |
| 10 | Ngữ cảnh |
| 11 | Giới hạn hệ thống |
| 12 | Ngầm |
| 13 | Hệ thống |
| 14 | Do người dùng |
| 15 | Hệ thống |
| 16 | Ngữ cảnh |
| 17 | Ngầm |
| 18 | Ngữ cảnh |
| 19 | Giới hạn hệ thống |
| 20 | Ngầm |

Khi so sánh với bộ nhãn của người gắn nhãn 2, hai bên thống nhất 17/20 ca, tương đương 85%. Ba ca khác nhau là ca 9, 13 và 20.

Sau khi thảo luận, nhóm thống nhất:

- Ca 9 là **Do người dùng**, vì khách nhập mã đơn của sàn thay vì mã vận đơn.
- Ca 13 là **Giới hạn hệ thống**, vì yêu cầu hoàn phí bảo hiểm đối tác nằm ngoài phạm vi trợ lý.
- Ca 20 là **Hệ thống**, vì thiếu khóa chống trùng làm một đơn được hoàn tiền hai lần.

Tôi cũng tham gia hoàn thiện bảng khắc phục cho năm trường hợp đại diện:

- Ca 6 — Do người dùng
- Ca 7 — Hệ thống
- Ca 16 — Ngữ cảnh
- Ca 11 — Giới hạn hệ thống
- Ca 5 — Ngầm

Mỗi giải pháp đều có cách phát hiện đo được, ngưỡng hoặc tần suất kiểm tra, biện pháp khắc phục và vai trò chịu trách nhiệm.

## 4. Bằng chứng

Các bằng chứng cho phần việc của tôi:

- Bộ nhãn độc lập: `docs/labels/2A202603747_NguyenMinhQuan.md`
- Bảng đối chiếu và khắc phục chung: `report/team/bang_loi.md`
- Kết quả đồng thuận: 17/20 ca, tương đương 85%.
- Các ca không đồng thuận ban đầu: 9, 13 và 20.
- Năm ca được chọn cho bảng khắc phục: 6, 7, 16, 11 và 5.
- Bộ nhãn ban đầu đã được lưu riêng trước khi hợp nhất, nên vẫn truy vết được lựa chọn của từng người.

## 5. Công cụ AI đã dùng

Tôi sử dụng Codex để:

- Giải thích yêu cầu của từng checkpoint.
- Làm rõ sự khác nhau giữa năm loại lỗi của Google PAIR.
- Gợi ý cách trình bày bảng Markdown.
- Rà soát tính đo lường được của các biện pháp phát hiện và khắc phục.
- Hướng dẫn thao tác Git, tạo nhánh, commit, push và pull request.

Tôi không dùng kết quả AI làm nhãn chính thức một cách tự động. Tôi tự đọc từng ca trong đề bài, gắn bộ nhãn ban đầu độc lập, sau đó đối chiếu với người gắn nhãn 2. Các ca khác nhau được thảo luận và chốt dựa trên nguyên nhân gốc của lỗi.

## 6. Tự đánh giá

Tôi đã hoàn thành đúng vai trò người gắn nhãn 1:

- Có đủ 20 nhãn độc lập.
- Giữ lại bộ nhãn ban đầu để bảo đảm khả năng truy vết.
- Tham gia đối chiếu và xử lý ba ca không đồng thuận.
- Đạt tỉ lệ đồng thuận 85%, cao hơn yêu cầu tối thiểu 80%.
- Tham gia xây dựng biện pháp khắc phục cho đủ năm loại lỗi.
- Cung cấp bằng chứng bằng file, bảng và số liệu cụ thể.

Điểm tôi cần cải thiện là phân biệt rõ hơn giữa lỗi hệ thống, giới hạn hệ thống và lỗi ngầm ngay từ lần gắn nhãn đầu tiên. Ba ca 9, 13 và 20 giúp tôi hiểu rằng phải phân loại theo nguyên nhân gốc, không chỉ theo biểu hiện hoặc nơi cần sửa.