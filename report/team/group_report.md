# Báo cáo nhóm

## 1. Thông tin nhóm

- Nhóm: **Pilot** · Lớp: **L3B**.
- Repo: `K5-L3B-DAY13-Pilot-LaunchEconomics`.
- Thành viên và đóng góp: [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Nhóm dùng mẫu giả lập 1.200 yêu cầu, 1.624 lần chạy để tính chi phí, phân loại lỗi và thiết kế pilot tại Gate 2a. Minh phụ trách nhãn người 2 và tổng hợp hồ sơ; kết quả nguồn được đối chiếu với code và dữ liệu.

## 3. Giải pháp

- **A–B:** tính chi phí mọi lần chạy, kể cả lỗi; mẫu số CPS chỉ đếm việc thành công. Kiểm tra độ nhạy, giới hạn chạy lại và chi phí cố định trong [bảng chi phí](bang_chi_phi.md).
- **C:** hai bộ nhãn độc lập, so nhãn và khắc phục năm loại lỗi trong [bảng lỗi](bang_loi.md).
- **D–E:** kế hoạch pilot có đối chứng, cỡ mẫu và bốn luật dừng; đặc tả năm chỉ số, mười event có `trace_id` và ba rủi ro kinh tế. Nguồn: [pilot](pilot_plan.yaml), [chỉ số](chi_so.md), cập nhật `8a6ad1c`.

## 4. Kết quả và duyệt chéo

- **Chi phí:** A1 ĐẠT (1,20 · 1,25 · 1,25). CPS toàn mẫu 4.472 đ/việc; cả hệ thống 5.865 đ/yêu cầu = 0,49× mốc thủ công 12.000 đ. Phạm vi noi_dia + hang_nang có CPS gồm cố định 4.599 đ ở 45.000 yêu cầu/tháng, 5.784 đ khi khối lượng giảm nửa (simulated). Làm lại và xem lại chiếm 51,8% và 40,7% chi phí (simulated).
- **Lỗi:** đồng thuận 17/20=85%; chốt ca 9: Do người dùng, 13: Giới hạn hệ thống, 20: Hệ thống; đủ năm ca khắc phục 6,7,16,11,5.
- **Pilot:** 20 nhân viên/nhóm, MDE +6 điểm; 299 yêu cầu/NV, DE=6,96 cho khoảng 859 yêu cầu hiệu dụng/nhóm. Power còn khoảng 0,64 nếu tác động thật +5 điểm. Luật hoàn trùng đã tách riêng, rollback trong 30 phút; ngày quyết định của Pilot là 05/01/2027.
- **Chỉ số trong đợt chạy thử:** chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200). Mẫu chưa có đối chứng, không kết luận tác động của trợ lý.
- **Đề xuất chốt trong hồ sơ nhóm:** **No-go**, theo [hồ sơ launch](ho_so_launch_v0.md). Quay lại Gate 2a sau khi có bằng chứng chống trùng, đối soát, event, đo phút thật, kiểm toán và phê duyệt đánh đổi MDE.
- **Pilot chấm G2026:** 10+10+10=30/30, **Go có điều kiện**, có hỏi–đáp tại [phiếu chấm](phieu_cham.md), nguồn `b4eb099` (PR #15). Mốc 15/01/2027 và rollback 15 phút trong phiếu thuộc G2026.

**Phản hồi hội đồng dành cho Pilot** (chưa có biên bản trong repo):

- Nhóm hội đồng:
- Điểm và quyết định:
- Nhận xét:
- Câu hỏi và trả lời:
- Việc sửa sau duyệt:

## 5. Khó khăn và cách xử lý

Máy Minh thiếu `statsmodels`, cài thư viện trong repo gặp đường dẫn OneDrive dài. Đã dùng môi trường riêng tại `%TEMP%\lab13-minh-venv`, cài requirements và chạy Python với `-X utf8` từ `src/`.

Điểm gộp hoàn trùng vào cửa sổ ba ngày đã được An sửa ở `8a6ad1c`: phát hiện một ca hoàn trùng thì kích hoạt rollback trong 30 phút. Xung đột TEAM.md, báo cáo nhóm và phiếu chấm được gộp theo nội dung mới trên main, giữ kết quả duyệt chéo đã bàn giao.

## 6. Tổng hợp đóng góp và bàn giao

Chi tiết xem TEAM.md và bốn báo cáo cá nhân. Minh đã nhận CP4/CP5, đồng bộ hồ sơ, cập nhật phiếu chấm G2026 và giải quyết xung đột. Checklist nhóm tại `7e12e19`, `ab4ef82` xác nhận mọi thành viên đã nộp link LMS; người giữ hồ sơ ghi nhận theo nguồn này.

## 7. Hạn chế và hướng cải thiện

92,5% chi phí đến từ phút giả lập. Xem lại 100% có thể đẩy CPS lên 12.415 đ/việc = 1,03× thủ công (simulated); cần đo phút thực tế và giảm xem lại theo bậc. Cỡ mẫu và power phải được giải thích cùng kết quả. Phản hồi hội đồng chấm Pilot được bổ sung khi nhận biên bản.

## 8. Tài liệu tham khảo

[Quy tắc](../../RULES.md), [checkpoint](../../CHECKPOINTS.md), [rubric](../../RUBRIC.md), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md), [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
