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

- **Chi phí (A & B):** Ba phép thử A1 đạt 100% (`1,20 · 1,25 · 1,25`). CPS toàn mẫu là **4.472 đ/việc** (`simulated`), gấp **16,3×** hoá đơn token + tool (`274,7 đ/yc`); giờ nhân viên chiếm **92,5%** (làm lại `51,8%`, xem lại `40,7%`, `simulated`). Chi phí cả hệ thống là **5.865 đ/yc = 0,49×** mốc thủ công 12.000 đ (`simulated`). Phạm vi khả thi gồm `noi_dia` (`2.696 đ = 0,22×`) và `hang_nang` (`8.221 đ = 0,69×`), CPS cộng cố định là **4.599 đ (0,38×)** ở 45.000 yc/tháng và **5.784 đ (0,48×)** ở nửa khối lượng (`simulated`); loại `quoc_te` (`22.515 đ = 1,88×`) và `doi_tac` (`10.215 đ = 0,85×`). Giới hạn **2 lần chạy** rẻ nhất cả hệ thống (**6.901.220 đ**, `simulated`). Nếu xem lại 100%, CPS vọt lên **11.743 đ (0,98×)** đến **12.415 đ (1,03×)** (`simulated`).
- **Lỗi (C):** Đồng thuận độc lập **17/20 = 85%**; chốt 3 ca khác biệt (`9: Do người dùng`, `13: Giới hạn hệ thống`, `20: Hệ thống`); bảng khắc phục đủ 5 loại qua ca `6, 7, 16, 11, 5`.
- **Pilot (D) & Chỉ số (E):** Chia ngẫu nhiên theo nhân viên **20 + 20** (phân tầng depot), MDE **+6 điểm** (`n = 859`/nhóm, `m ≥ 299` yc/NV, `DE = 6,96`, power thực tế ≈ **0,64** nếu tác động thật +5 điểm), 4 luật dừng (tách riêng 0 ca hoàn trùng tắt trong 30 phút), ngày quyết định `2027-01-05`. Chỉ số đợt chạy thử: đóng 24h & không mở lại 7 ngày **82,83%** (`994/1.200`), bỏ qua gợi ý **27,12%** (`48/177`), mở lại 7 ngày **4,25%** (`51/1.200`).
- **Đề xuất cuối tại [ho_so_launch_v0.md](ho_so_launch_v0.md):** **No-go** — chưa mở pilot cho tới khi hoàn tất 4 điều kiện quay lại Gate 2a (khoá chống trùng + đối soát sổ cái + bật 10 event `trace_id`; cơ chế đo phút thật & lộ trình giảm xem lại; kiểm toán mẫu 100 đơn/tuần; và phê duyệt đánh đổi MDE +6 điểm).
- **Duyệt chéo Gate 2a:** Nhóm Pilot đã hoàn tất chấm nhóm **G2026** trong vai trò hội đồng tại [phieu_cham.md](phieu_cham.md) (tổng điểm **30/30**, quyết định **Go có điều kiện**, kèm câu hỏi về power `0,64` ở mức +5 điểm và phần trả lời của đội trình). Kết quả hội đồng khác chấm nhóm Pilot được lưu theo phiếu của nhóm hội đồng.

## 5. Khó khăn và cách xử lý

Máy Minh thiếu `statsmodels`, cài thư viện trong repo gặp đường dẫn OneDrive dài. Đã dùng môi trường riêng tại `%TEMP%\lab13-minh-venv`, cài requirements và chạy Python với `-X utf8` từ `src/`.

Điểm gộp hoàn trùng vào cửa sổ ba ngày đã được An sửa ở `8a6ad1c`: phát hiện một ca hoàn trùng thì kích hoạt rollback trong 30 phút. Xung đột TEAM.md, báo cáo nhóm và phiếu chấm được gộp theo nội dung mới trên main, giữ kết quả duyệt chéo đã bàn giao.

## 6. Tổng hợp đóng góp và bàn giao

Chi tiết xem TEAM.md và bốn báo cáo cá nhân. Minh đã nhận CP4/CP5, đồng bộ hồ sơ, cập nhật phiếu chấm G2026 và giải quyết xung đột. Checklist nhóm tại `7e12e19`, `ab4ef82` xác nhận mọi thành viên đã nộp link LMS; người giữ hồ sơ ghi nhận theo nguồn này.

## 7. Hạn chế và hướng cải thiện

92,5% chi phí đến từ phút giả lập. Xem lại 100% có thể đẩy CPS lên 12.415 đ/việc = 1,03× thủ công (simulated); cần đo phút thực tế và giảm xem lại theo bậc. Cỡ mẫu và power phải được giải thích cùng kết quả. Phản hồi hội đồng chấm Pilot được bổ sung khi nhận biên bản.

## 8. Tài liệu tham khảo

[Quy tắc](../../RULES.md), [checkpoint](../../CHECKPOINTS.md), [rubric](../../RUBRIC.md), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md), [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
