# Báo cáo nhóm

Báo cáo tổng hợp, tối đa hai trang khi trình bày. Người giữ hồ sơ: Nguyễn Nhật Minh · 2A202603745. Bản này nhận CP1–CP2 đã được nhóm merge; các phần còn lại được ghi rõ trạng thái.

## 1. Thông tin nhóm

- Tên nhóm: [nhóm điền].
- Lớp: L3B.
- Repo: https://github.com/QuangNEU/K5-L3B-DAY13-Pilot-LaunchEconomics
- Thành viên và đóng góp: [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Đánh giá kinh tế và chuẩn bị hồ sơ Gate 2a cho pilot trợ lý hoàn phí LogiX-VN. Người giữ hồ sơ thu nhận kết quả đã có, đối chiếu nguồn, ghi đúng số giả lập và tổng hợp đề xuất để nhóm chốt.

## 3. Giải pháp và nguồn bàn giao

- A–B: [bảng chi phí](bang_chi_phi.md), nguồn `main` tại commit `3f69dbf`; tính mọi lần chạy và so sánh bằng chi phí cả hệ thống/yêu cầu.
- C: [bảng lỗi](bang_loi.md) đã có cột người 2; [phiếu Minh](phieu_nhan_doc_lap_Minh.md) ghi nhãn gợi ý và lý do, [đối chiếu hai bản](doi_chieu_nhan_Minh.md) cho 17/20=85%, khác ca 9,13,20; chờ hai người xác nhận/thảo luận.
- D: chờ người phụ trách hoàn thiện [kế hoạch pilot](pilot_plan.yaml); người giữ hồ sơ nhận và rà D1–D2, luật dừng, lịch và rollback.
- E: chờ [chỉ số/event/rủi ro](chi_so.md) nhóm chốt; các số CSV đối chiếu nằm trong [phiếu kiểm chứng](doi_chieu_ho_so_Minh.md).

## 4. Kết quả và phản hồi hội đồng

Toàn mẫu có CPS **4.472 đ/việc**; chi phí cả hệ thống **5.865 đ/yêu cầu**, bằng **0,49 lần** mốc thủ công (simulated). Phạm vi noi_dia + hang_nang có CPS **4.599 đ** gồm cố định ở 45.000 yêu cầu/tháng (simulated). Làm lại gấp đôi làm CPS tăng **51,8%**; xem lại 100% có CPS **11.743–12.415 đ** theo giả định thời gian (simulated).

CSV đối chiếu cho chỉ số chính **82,83%**, bỏ qua **27,12%**, mở lại **4,25%**; chưa có đối chứng nên chưa chứng minh mức cải thiện. [Hồ sơ launch](ho_so_launch_v0.md) đang để đề xuất Go có điều kiện chờ nhóm chốt.

**Hội đồng chấm nhóm mình — điền sau buổi duyệt:**

- Nhóm hội đồng: Chưa ghi nhận.
- Quyết định, điểm/lý do có số: Chưa ghi nhận.
- Câu hỏi và câu trả lời thực tế: Chưa ghi nhận.
- Việc cần sửa, vai trò phụ trách, ngày kiểm tra: Chưa ghi nhận.

[Phiếu chấm](phieu_cham.md) lưu đánh giá nhóm mình dành cho nhóm khác; phản hồi dành cho nhóm mình ghi ở bốn dòng trên.

## 5. Khó khăn và cách xử lý

Đã tìm thấy bản người 1 ở nhánh feature/quan-label-1 và đối chiếu hai bản; còn chờ hai người xác nhận/thảo luận CP3 và bàn giao CP4/E1–E2. Các mục thiếu vẫn giữ trạng thái Chưa. Nếu phát sinh lỗi kỹ thuật tại lớp, người thực hiện ghi lệnh, output và cách xử lý thực tế tại đây.

## 6. Tổng hợp đóng góp

Minh phụ trách nhãn người 2 và giữ hồ sơ; [báo cáo cá nhân](2A202603745_NguyenNhatMinh.md) phân biệt hỗ trợ của Codex với việc Minh tự xác nhận. Đóng góp thành viên khác do từng người ghi trong TEAM.md.

## 7. Hạn chế và hướng cải thiện

Chi phí thời gian dùng giả lập, ảnh hưởng khối lượng và xem lại có thể làm mất lợi ích kinh tế. Cần hoàn thiện CP3, nhận kế hoạch đủ mẫu, chốt giám sát/luật dừng và đo phút thật trước khi duyệt pilot.

## 8. Tài liệu tham khảo

[Quy tắc](../../RULES.md), [checkpoint](../../CHECKPOINTS.md), [rubric](../../RUBRIC.md), [đề bài](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), [log kiểm chứng](kiem_chung_ho_so_Minh.txt).
