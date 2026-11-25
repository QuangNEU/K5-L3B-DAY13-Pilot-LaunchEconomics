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

Các giải pháp dưới đây là đề xuất theo loại lỗi, chưa gán vào một ca hay bộ nhãn độc lập. Sau khi so nhãn, nhóm chọn số ca, sửa giải pháp cho đúng tình huống và chốt ngưỡng. Cách phát hiện phải đo được; người phụ trách là một vai trò.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| Chờ nhóm chọn ca | Do người dùng | Event input_validation_failed; đề xuất cảnh báo >2% yêu cầu/ngày | Kiểm đầu vào, chỉ rõ trường sai và hướng dẫn khách sửa | PM trợ lý hoàn phí |
| Chờ nhóm chọn ca | Hệ thống | Đối soát sổ cái mỗi giờ theo trace_id; đề xuất ngưỡng 0 ca thông báo hoàn khi chưa ghi sổ thành công | Chỉ xác nhận khi sổ cái trả ok, lỗi thì chuyển nhân viên và giữ khoá chống trùng | Kỹ sư trưởng agent |
| Chờ nhóm chọn ca | Ngữ cảnh | Theo dõi yêu cầu mở lại do không hiểu thông báo theo tuần; nhóm chốt ngưỡng | Giải thích cách tính, nơi nhận tiền hoặc thời điểm thông báo theo hoàn cảnh của ca được chọn | Trưởng nhóm CSKH |
| Chờ nhóm chọn ca | Giới hạn hệ thống | Event handoff_to_staff với reason theo loại yêu cầu; rà theo tuần | Nêu rõ giới hạn, chuyển kèm tóm tắt và loại phạm vi chưa hỗ trợ khỏi pilot | PM trợ lý hoàn phí |
| Chờ nhóm chọn ca | Ngầm | Đề xuất kiểm tra 100 đơn/tuần; cảnh báo từ 1% đơn sai giá/số tiền | Đối chiếu chính sách/bảng giá hiện hành và kiểm tra phiên bản dữ liệu | Kế toán trưởng |

## Kiểm tra và bàn giao


- [ ] Mỗi người có đủ 20 nhãn gốc và ghi thời điểm chốt trước khi so.
- [ ] Đồng thuận dùng nhãn gốc; ca bất đồng có nhãn thống nhất và một câu quy tắc.
- [ ] Nếu dưới 80%, đã ghi định nghĩa điều chỉnh và giữ kết quả ban đầu.
- [ ] Bảng khắc phục đủ năm loại; cách phát hiện có event/ngưỡng/tần suất và một vai trò phụ trách.
- [ ] Cả hai người xác nhận trước khi cập nhật mục 5 của hồ sơ launch.
