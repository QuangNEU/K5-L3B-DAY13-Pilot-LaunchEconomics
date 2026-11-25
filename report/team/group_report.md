# Báo cáo nhóm

Người tổng hợp: Nguyễn Nhật Minh · 2A202603745.

## 1. Thông tin nhóm

- Tên nhóm: [nhóm điền].
- Lớp: L3B.
- Thành viên và đóng góp: [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Nhóm tính chi phí từ trace, phân loại lỗi và lập kế hoạch pilot để đề xuất quyết định tại Gate 2a. Minh tổng hợp kết quả được bàn giao, đối chiếu nguồn và cập nhật hồ sơ.

## 3. Kết quả đã nhận

- **CP1 — Nguyễn Như Duy An:** mô hình A1–A4. CPS toàn mẫu 4.472 đ/việc; toàn hệ thống 5.865 đ/yêu cầu, bằng 0,49 lần mốc thủ công (simulated).
- **CP2 — Nguyễn Minh Quang:** độ nhạy và kiểm số. Làm lại tăng gấp đôi làm CPS tăng 51,8%; xem lại 100% có CPS 11.743–12.415 đ theo thời gian làm lại (simulated).
- **CP3 — Quân và Minh:** đủ hai bộ nhãn, đồng thuận 85%, chốt ca 9,13,20. Quân hoàn thiện 5 ca khắc phục 6,7,16,11,5; người giữ hồ sơ đã nhận và cập nhật.
- **CP4:** đã nhận bản D1–D2 và YAML tại `f1104de` của Nguyễn Như Duy An. Chia theo nhân viên 20 + 20, MDE +6 điểm, 859 yêu cầu hiệu dụng/nhóm; tối thiểu 299 yêu cầu/nhân viên, DE=6,96; rollout 10%→25%→50%, ngày quyết định trong bản kế hoạch là 2027-01-05. Người giữ hồ sơ đã rà cấu trúc YAML và cập nhật mục 6; còn cần xác nhận cách xử lý ca hoàn trùng.
- **CP5/E1–E2:** chờ người được phân công bàn giao chỉ số, event và rủi ro kinh tế đã chốt.

Nguồn chi tiết: [chi phí](bang_chi_phi.md), [bảng lỗi](bang_loi.md), [pilot](pilot_plan.yaml), [chỉ số](chi_so.md).

## 4. Đề xuất và duyệt chéo

- Kết luận cuối: Chờ nhóm xác nhận CP4 và nhận đủ bằng chứng E1–E2.
- Điều kiện, vai trò, ngày kiểm tra: Chờ nhóm chốt.
- Hội đồng chấm nhóm mình: Chưa ghi nhận.
- Điểm/quyết định/lý do, câu hỏi và câu trả lời thực tế: Chưa ghi nhận.
- Việc cần sửa sau duyệt: Chưa ghi nhận.

[Phiếu chấm](phieu_cham.md) lưu phần nhóm mình chấm nhóm khác. Phản hồi dành cho nhóm mình ghi tại mục này.

## 5. Khó khăn và cách xử lý

TEAM.md còn thiếu người chủ trì CP4 và CP5. An đã cập nhật CP4; cần xác nhận luật hoàn trùng vì chú thích yêu cầu 0 ca nhưng luật dừng ghi “3 ngày liên tiếp”. CP5 vẫn là mẫu, chưa có chỉ số, event và hành động E2 để tổng hợp.

Kiểm tra trên máy Minh: `python lab13.py` ban đầu thiếu `statsmodels`; cài trong repo gặp lỗi đường dẫn OneDrive dài. Đã dùng môi trường riêng tại `%TEMP%\lab13-minh-venv`, cài `src/requirements.txt` và chạy Python với `-X utf8` từ `src/`: kết thúc không lỗi, ba phép thử A1 ĐẠT, A–B và D1 khớp số trong hồ sơ.

## 6. Tổng hợp đóng góp

Minh phụ trách nhãn người 2, nhận kết quả của các thành viên và cập nhật hồ sơ. Đóng góp chi tiết ghi trong TEAM.md và báo cáo cá nhân từng người.

## 7. Hạn chế và hướng cải thiện

Chi phí thời gian dùng giả lập; xem lại và khối lượng có thể làm thay đổi kết luận kinh tế. Kế hoạch CP4 chấp nhận MDE +6 điểm; nếu tác động thật chỉ +5 điểm, power khoảng 0,64 theo bản kế hoạch. Cần xác nhận CP4, bàn giao E1–E2 và quyết định nhóm trước khi chốt hồ sơ.

## 8. Tài liệu tham khảo

[Quy tắc](../../RULES.md), [checkpoint](../../CHECKPOINTS.md), [rubric](../../RUBRIC.md), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md).
