# Báo cáo cá nhân — Nguyễn Nhật Minh — 2A202603745

## 1. Thông tin thành viên

- Họ tên: Nguyễn Nhật Minh.
- MSSV: 2A202603745.
- Email: nnhatminh2610@gmail.com.
- GitHub: [NhMinh-2610](https://github.com/NhMinh-2610).
- Vai trò: Người gắn nhãn 2, kiêm giữ hồ sơ.
- Nhánh đóng góp: `NguyenNhatMinh`.

## 2. Phần việc phụ trách

Tôi gắn nhãn 20 ca ở cột người 2 của CP3, so sánh với bộ nhãn của Nguyễn Minh Quân và ghi nhãn thống nhất cho các ca khác nhau. Tôi cũng nhận kết quả của các thành viên để điền hồ sơ launch và báo cáo nhóm.

## 3. Đóng góp cụ thể

- [x] Hoàn thiện 20 nhãn ở cột người 2 trong [bảng lỗi](bang_loi.md); giữ riêng hai bộ nhãn ban đầu khi so sánh.
- [x] Đối chiếu hai cột nhãn: có 17 ca trùng trên 20 ca, đạt **85%**; ba ca khác nhau là **9, 13 và 20**.
- [x] Chốt ba nhãn và ghi lý do phân biệt theo nguyên nhân gốc:

| Ca | Nhãn thống nhất | Lý do |
| ---: | --- | --- |
| 9 | Do người dùng | Khách nhập mã đơn của sàn thay vì mã vận đơn. |
| 13 | Giới hạn hệ thống | Hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi hỗ trợ. |
| 20 | Hệ thống | Thiếu khóa chống trùng dẫn đến hoàn tiền hai lần. |

- [x] Tiếp nhận bảng khắc phục năm ca **6, 7, 16, 11, 5** do Quân hoàn thiện; tổng hợp vào mục 5 của hồ sơ launch.
- [x] Tổng hợp kết quả CP1–CP2 do An và Quang bàn giao vào hồ sơ và báo cáo nhóm. Tôi ghi rõ nhãn `simulated` cho các kết quả có sử dụng thời gian giả lập.
- [x] Nhận bản CP4 đã có trên main, rà cấu trúc YAML và cỡ mẫu hiệu dụng; cập nhật mục 6 hồ sơ và ghi điểm cần người phụ trách xác nhận.
- [x] Đọc hiểu nhãn lỗi và số liệu trong hồ sơ; nhận thông báo nhóm đã chốt CP4 và đối chiếu với bản mới nhất trên main.
- [x] Đối chiếu ba chỉ số nền từ CSV, bổ sung mục 4 và 7; hoàn thiện bảy mục hồ sơ cùng đề xuất No-go và việc cần làm để quay lại Gate 2a.
- [x] Hoàn thiện báo cáo cá nhân và thông tin liên hệ trong TEAM.md.
- [x] Tổng hợp thông tin bốn thành viên từ báo cáo cá nhân; chuẩn bị phiếu chấm và ba ý giải trình về chi phí, cỡ mẫu, đề xuất No-go.
- [x] Nhận bản CP4/CP5 hoàn thiện, cập nhật phiếu Pilot chấm G2026 đạt 30/30 và giải quyết xung đột khi gộp main.

## 4. Bằng chứng và cách đối chiếu

- [Bảng lỗi CP3](bang_loi.md): hai cột nhãn gốc, phép tính `17 / 20 × 100 = 85%` và lý do chốt ba ca. Tỉ lệ đồng thuận được tính trước khi thống nhất nhãn.
- [Bộ nhãn của Quân](../../docs/labels/2A202603747_NguyenMinhQuan.md): nguồn đối chiếu cho cột người 1.
- [Bảng chi phí](bang_chi_phi.md): nguồn của các số tôi đưa vào [hồ sơ launch](ho_so_launch_v0.md) và [báo cáo nhóm](group_report.md).

Khi tổng hợp, tôi phân biệt **4.472 đ/việc thành công** với **5.865 đ/yêu cầu của toàn hệ thống** (`simulated`). Số thứ hai đã cộng chi phí xử lý thủ công cho 222 ca không thành công, chưa gồm chi phí cố định. Ở phạm vi `noi_dia + hang_nang`, số **4.599 đ/việc** đã gồm cố định tại 45.000 yêu cầu/tháng (`simulated`).

Tôi đối chiếu ba mức tăng chi phí ở bảng B1 với hồ sơ: làm lại **51,8%**, xem lại **40,7%**, lương **23,1%** (`simulated`). Phần viết code và tính bảng nguồn do thành viên phụ trách thực hiện.

Tôi đối chiếu [CP4](pilot_plan.yaml) tại commit `f1104de`: 20 nhân viên/nhóm, MDE +6 điểm, tối thiểu 299 yêu cầu/nhân viên. Phép tính `20 × 299 / 6,96 ≈ 859,20` đáp ứng mức 859 yêu cầu hiệu dụng/nhóm. YAML đọc được và không còn dấu hỏi ngoài chú thích. Tôi đã ghi lại điểm cần xác nhận về luật dừng khi có hoàn tiền trùng.

Tôi đã nhận bản cập nhật `8a6ad1c` của An: luật hoàn trùng tách riêng, kích hoạt rollback trong 30 phút; CP5 có năm chỉ số, mười event có `trace_id`, ánh xạ chỉ số và ba rủi ro kinh tế. Tôi đối chiếu các phần này với hồ sơ trước khi đồng bộ báo cáo.

Kết quả kiểm tra `src/lab13.py` trên máy tôi: chương trình chạy hết, ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25); các bảng A–B và D1 khớp số trong hồ sơ. Cách chạy bằng môi trường riêng ghi trong [README](README.md).

Tôi đối chiếu ba chỉ số trên 1.200 yêu cầu: 994 ca đóng trong 24 giờ và không mở lại đạt 82,83%; 48 lượt sửa/bỏ trong 177 lượt được xem lại đạt 27,12%; 51 ca mở lại trong 7 ngày chiếm 4,25%. Cách đếm và nguồn CSV được ghi trong hồ sơ. Đây là kết quả trong mẫu của lab, chưa chứng minh tác động so với nhóm đối chứng.

## 5. Phối hợp và bàn giao

- [x] Nhận CP4 đã sửa và CP5 hoàn chỉnh tại `8a6ad1c`; đối chiếu mục 4,6,7 của hồ sơ.
- [x] Đồng bộ đề xuất No-go với bản hồ sơ nhóm trên main, giữ rõ các việc để quay lại Gate 2a.
- [x] Cập nhật [phiếu Pilot chấm G2026](phieu_cham.md) từ `b4eb099`: 30/30, Go có điều kiện; có câu hỏi về power và trả lời của đội trình.
- [x] Ghi nhận xác nhận mọi thành viên đã nộp LMS trong checklist nhóm tại `7e12e19`, `ab4ef82`.
- [ ] Ghi lại phản hồi hội đồng dành cho Pilot vào mục 4 báo cáo nhóm sau khi được bàn giao biên bản. Tôi phụ trách tổng hợp; điểm và nhận xét do hội đồng cung cấp. Hiện chưa có nguồn xác định phản hồi dành cho Pilot.

## 6. Tự đánh giá

Tôi đã hoàn thiện bộ nhãn người 2, ghi lý do chốt ba ca khác nhau và tổng hợp các kết quả đã có vào hồ sơ. Phần so nhãn giúp tôi phân biệt rõ hơn giữa nguyên nhân lỗi và cách khắc phục, nhất là ở ca 9, 13 và 20.

Hồ sơ đã đủ bảy mục, CP4/CP5 và phiếu chấm G2026 đã được bàn giao. Tôi đã gộp các cập nhật mới và xử lý xung đột để tài liệu thống nhất. Phần tổng hợp phản hồi dành cho Pilot cần biên bản từ hội đồng; tôi chưa ghi điểm hoặc nhận xét khi chưa có nguồn.
