# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Nguyễn Minh Quân** · Người gắn nhãn 2: **Nguyễn Nhật Minh**.

Nguồn người 1: [bản Quân đã commit](https://github.com/QuangNEU/K5-L3B-DAY13-Pilot-LaunchEconomics/blob/42385e0c74c30c649b8dafd690ba03545ec0563b/docs/labels/2A202603747_NguyenMinhQuan.md). Hai cột nhãn gốc được giữ riêng; Cột Nhãn thống nhất ghi các ca trùng và ba nhãn Minh đã chốt.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Ngữ cảnh | Do người dùng | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Ngầm | Hệ thống | Không | Hệ thống |

**Tỉ lệ đồng thuận:** **17 / 20 = 85%**, tính trên hai bộ nhãn gốc trước khi chốt. Ba ca không trùng: **9, 13, 20**.

## Quy tắc phân biệt cho các ca không trùng

Ba nhãn dưới đây được chốt theo yêu cầu của Nguyễn Nhật Minh; giữ nguyên lựa chọn ban đầu của Quân ở cột người 1.

- **Ca 9 — Do người dùng:** khách nhập mã đơn của sàn thay vì mã vận đơn; nguyên nhân gốc là đầu vào sai, còn thiếu hướng dẫn sửa mã là vấn đề cần khắc phục tiếp.
- **Ca 13 — Giới hạn hệ thống:** hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý; câu trả lời chung chung chưa nêu rõ giới hạn nhưng nguyên nhân gốc vẫn là ngoài phạm vi hỗ trợ.
- **Ca 20 — Hệ thống:** thiếu khoá chống trùng khiến một đơn được hoàn hai lần; đây là lỗi cơ chế xử lý, không xếp Ngầm chỉ dựa vào việc lỗi có thể chưa được ai nhận ra.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được bằng event, ngưỡng hoặc tần suất. Người phụ trách là một vai trò cụ thể, không ghi “cả đội”.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 6 | Do người dùng | Ghi event `request_type_mismatch`; cảnh báo khi vượt 2% yêu cầu/ngày. | Yêu cầu khách xác nhận lại loại khiếu nại và hướng dẫn chuyển từ “giao chậm” sang “hàng hỏng” trước khi xử lý. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa thông báo “đã hoàn” và giao dịch thành công trong sổ cái theo `trace_id`; ngưỡng cho phép là 0 trường hợp lệch. | Chỉ thông báo hoàn tiền sau khi sổ cái trả trạng thái thành công. Nếu lỗi sau 3 lần thử thì giữ trạng thái chờ và chuyển nhân viên xử lý. | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Ghi event `notification_sent` trong khoảng 22:00–07:00; ngưỡng là 0 thông báo không khẩn cấp vào ban đêm mỗi ngày. | Xếp hàng thông báo để gửi sau 08:00, trừ khi khách đã chọn nhận thông báo ngay. | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Ghi event `unsupported_input` với `format=audio`; thống kê số lượng và tỉ lệ hằng ngày. | Nêu rõ hệ thống chưa hỗ trợ âm thanh, yêu cầu khách gửi nội dung dạng văn bản hoặc chuyển cho nhân viên. | PM trợ lý hoàn phí |
| 5 | Ngầm | Kiểm tra ngẫu nhiên 100 đơn mỗi tuần, so sánh giá thực trả sau giảm giá với số tiền hoàn; cảnh báo khi trên 1% đơn bị lệch. | Tính tiền hoàn trên giá khách thực trả và tự động đối chiếu trước khi ghi giao dịch vào sổ cái. | Kế toán trưởng |

## Kiểm tra và bàn giao

- [x] Mỗi người có đủ 20 nhãn gốc trước khi so sánh.
- [x] Đồng thuận được tính trên nhãn gốc; các ca bất đồng có nhãn thống nhất và quy tắc phân biệt.
- [x] Tỉ lệ đồng thuận đạt 17/20 = 85%, không cần viết lại toàn bộ định nghĩa.
- [x] Bảng khắc phục có đủ năm loại lỗi, cách phát hiện đo được và vai trò phụ trách.
- [x] Cả hai người xác nhận trước khi cập nhật mục 5 của hồ sơ launch.