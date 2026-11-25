# Báo cáo cá nhân — Nguyễn Minh Quang - 2A202603791

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Quang
- MSSV: 2A202603791
- Email: 26ai.quangnm3@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số

## 2. Phần việc phụ trách

- Đọc hiểu bài toán, dữ liệu (`src/logix_runs.csv`, `src/logix_requests.csv`) và sáu công thức trong `docs/du_lieu_va_cong_thuc.md`.
- Thực hiện kiểm tra đối chiếu số liệu cho **CP1 (Nhiệm vụ A)** và **CP2 (Nhiệm vụ B)**; trực tiếp điền và hoàn thiện `report/team/bang_chi_phi.md`.
- Hỗ trợ đối chiếu số liệu cỡ mẫu **D1** (`pilot_plan.yaml`) và 3 chỉ số tính thử **E1** (`chi_so.md`).

## 3. Đóng góp cụ thể

- Viết script kiểm tra chéo độc lập để tự tính và đối chiếu toàn bộ số liệu từ 2 file CSV (bật `keep_default_na=False`), bảo đảm sai số ≤ 2% so với `src/lab13.py` và số đối chiếu.
- Kiểm tra và xác nhận phần **A1–A4**:
  - 3 phép thử A1 đạt (`1,20` · `1,25` · `1,25`).
  - Mô hình chi phí A2: tổng chi phí `4.373.585 đ` (có phần `simulated`), `978` việc thành công, chi phí mỗi việc thành công `4.472 đ` (`simulated`, gấp `16,3×` hoá đơn `274,7 đ/yêu cầu`); làm lại chiếm `51,8%` và xem lại chiếm `40,7%` (`simulated`).
  - Tách theo 4 loại A3 và chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` ở A4 (`4.599 đ = 0,38×` ở mức 45.000 yc/tháng, `5.784 đ = 0,48×` ở mức một nửa khối lượng, `simulated`).
- Tính và điền đầy đủ phần **B1–B4** vào `report/team/bang_chi_phi.md`:
  - Đủ 9 kịch bản B1, kịch bản đổi cặp B2 (`6.543 đ`, `+46,3%`, `simulated`), và xếp hạng 3 yếu tố mạnh nhất (`1. Số ca làm lại` · `2. Tỉ lệ xem lại` · `3. Lương nhân viên`).
  - Tính chi phí cả hệ thống B3 cho giới hạn 1, 2, 3 lần chạy (chỉ ra giới hạn **2 lần** rẻ nhất cho công ty ở mức `6.901.220 đ`, `simulated`, khác với giới hạn 1 lần tối ưu CPS).
  - Tính B4 xem lại 100% cho `noi_dia` + `hang_nang` ở cả hai mức làm lại: 9 phút/ca (`11.743 đ = 0,98×`, `simulated`) và trung bình thực tế `15,3 phút`/ca (`12.415 đ = 1,03×`, `simulated`), kèm ngưỡng hoà vốn xem lại (`≤ 5,1 phút` / `≤ 4,8 phút`).

## 4. Bằng chứng

- File hồ sơ nhóm đã hoàn thiện phần A và B: `report/team/bang_chi_phi.md`.
- Các con số đối chiếu chính đã kiểm chứng: `4.472 đ` (`simulated`), `5.865 đ` cả hệ thống/yêu cầu (`0,49×`), `4.599 đ` (`0,38×` sau cố định), `6.901.220 đ` (giới hạn 2 lần, B3), `11.743 đ` / `12.415 đ` (xem lại 100%, B4).
- Commit trên nhánh làm việc của nhóm: *(điền mã commit sau khi commit `report/team/bang_chi_phi.md` và báo cáo cá nhân)*.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI (Antigravity / Gemini) dùng để tóm tắt cấu trúc yêu cầu của lab, hỗ trợ viết script kiểm tra chéo từ dữ liệu CSV và trình bày bảng/câu trả lời đúng chuẩn trong `report/team/bang_chi_phi.md`.
- **Cách tự kiểm tra:**
  - Chạy trực tiếp script đọc `src/logix_runs.csv` và `src/logix_requests.csv` (có `keep_default_na=False`) và xác nhận 3 phép thử A1 đạt `1,20 · 1,25 · 1,25`.
  - Kiểm tra tính đối xứng ở B1 (mỗi kịch bản giảm một nửa giảm đúng bằng nửa mức tăng của kịch bản gấp đôi tương ứng).
  - Đối chiếu từng dòng số liệu với `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và kết quả chạy `src/lab13.py` của Người viết code (sai số ≤ 2%), đồng thời rà đủ nhãn `simulated` và giới hạn ≤ 3 dòng mỗi câu trả lời.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ vai trò **Người kiểm số** tại CP1 và CP2, giúp nhóm có số liệu sạch để làm CP4, CP5 mà không bị nghẽn cổ chai.
- Nắm chắc bản chất kinh tế học của agent: hoá đơn token chỉ chiếm phần nhỏ so với chi phí thời gian nhân viên xem lại/làm lại, và tối ưu CPS riêng lẻ có thể làm tăng tổng chi phí cả hệ thống nếu đẩy nhiều ca sang nhân viên tự xử lý.
