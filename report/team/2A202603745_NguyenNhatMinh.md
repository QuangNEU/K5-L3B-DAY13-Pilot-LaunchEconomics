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
- [x] Đối chiếu ba chỉ số nền từ CSV, bổ sung mục 4 và 7; hoàn thiện bảy mục hồ sơ cùng đề xuất No-go và việc cần làm để quay lại Gate 2a.
- [x] Hoàn thiện báo cáo cá nhân và thông tin liên hệ trong TEAM.md.

## 4. Bằng chứng và cách đối chiếu

- [Bảng lỗi CP3](bang_loi.md): hai cột nhãn gốc, phép tính `17 / 20 × 100 = 85%` và lý do chốt ba ca. Tỉ lệ đồng thuận được tính trước khi thống nhất nhãn.
- [Bộ nhãn của Quân](../../docs/labels/2A202603747_NguyenMinhQuan.md): nguồn đối chiếu cho cột người 1.
- [Bảng chi phí](bang_chi_phi.md): nguồn của các số tôi đưa vào [hồ sơ launch](ho_so_launch_v0.md) và [báo cáo nhóm](group_report.md).

Khi tổng hợp, tôi phân biệt **4.472 đ/việc thành công** với **5.865 đ/yêu cầu của toàn hệ thống** (`simulated`). Số thứ hai đã cộng chi phí xử lý thủ công cho 222 ca không thành công, chưa gồm chi phí cố định. Ở phạm vi `noi_dia + hang_nang`, số **4.599 đ/việc** đã gồm cố định tại 45.000 yêu cầu/tháng (`simulated`).

Tôi đối chiếu ba mức tăng chi phí ở bảng B1 với hồ sơ: làm lại **51,8%**, xem lại **40,7%**, lương **23,1%** (`simulated`). Phần viết code và tính bảng nguồn do thành viên phụ trách thực hiện.

Tôi đối chiếu [CP4](pilot_plan.yaml) tại commit `f1104de`: 20 nhân viên/nhóm, MDE +6 điểm, tối thiểu 299 yêu cầu/nhân viên. Phép tính `20 × 299 / 6,96 ≈ 859,20` đáp ứng mức 859 yêu cầu hiệu dụng/nhóm. YAML đọc được và không còn dấu hỏi ngoài chú thích. Tôi đã ghi lại điểm cần xác nhận về luật dừng khi có hoàn tiền trùng.

Kết quả kiểm tra `src/lab13.py` trên máy tôi: chương trình chạy hết, ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25); các bảng A–B và D1 khớp số trong hồ sơ. Cách chạy bằng môi trường riêng ghi trong [README](README.md).

Tôi đối chiếu ba chỉ số trên 1.200 yêu cầu: 994 ca đóng trong 24 giờ và không mở lại đạt 82,83%; 48 lượt sửa/bỏ trong 177 lượt được xem lại đạt 27,12%; 51 ca mở lại trong 7 ngày chiếm 4,25%. Cách đếm và nguồn CSV được ghi trong hồ sơ. Đây là kết quả trong mẫu của lab, chưa chứng minh tác động so với nhóm đối chứng.

## 5. Phần việc tiếp theo và phối hợp

- [ ] Nhờ người phụ trách CP4 và Quang xác nhận luật hoàn trùng (0 ca so với điều kiện “3 ngày liên tiếp”), lịch và vai trò vận hành; sau đó cập nhật trạng thái mục 6 hồ sơ theo bản chốt.
- [ ] Nhận đặc tả E1–E2 đầy đủ từ người phụ trách CP5; kiểm tra event tính được các chỉ số trong hồ sơ và cập nhật theo bản chốt.
- [ ] Trình đề xuất No-go cho nhóm/hội đồng; ghi kết quả thực tế và cập nhật hồ sơ sau duyệt.
- [ ] Ghi câu hỏi, câu trả lời và phản hồi duyệt chéo thực tế vào mục 4 báo cáo nhóm; điền [phiếu chấm](phieu_cham.md) khi nhóm làm hội đồng.
- [ ] Sau khi nhóm chốt bản nộp, kiểm tra quyền truy cập repo và tự nộp link trên LMS bằng tài khoản cá nhân.

## 6. Tự đánh giá

Tôi đã hoàn thiện bộ nhãn người 2, ghi lý do chốt ba ca khác nhau và tổng hợp các kết quả đã có vào hồ sơ. Phần so nhãn giúp tôi phân biệt rõ hơn giữa nguyên nhân lỗi và cách khắc phục, nhất là ở ca 9, 13 và 20.

Hồ sơ đã đủ bảy mục, có số liệu đối chiếu, vai trò vận hành đề xuất và kết luận No-go. Tôi còn cần nhận bản sửa CP4, đặc tả E1–E2 đầy đủ và ghi phản hồi sau duyệt chéo.
