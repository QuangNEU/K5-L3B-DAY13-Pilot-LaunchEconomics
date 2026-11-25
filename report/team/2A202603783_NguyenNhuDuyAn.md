# Báo cáo cá nhân — NguyenNhuDuyAn-2A202603783

## 1. Thông tin thành viên

- Họ tên: Nguyễn Như Duy An
- MSSV: 2A202603783
- Email: 26ai.annnd@vinuni.edu.vn
- Vai trong nhóm: Người viết code (phụ trách chính CP1 · Nhiệm vụ A; tham gia tổng hợp CP5 và duyệt chéo Gate 2a cùng nhóm)

## 2. Phần việc phụ trách

- **CP1 · Nhiệm vụ A (Mô hình chi phí mỗi việc thành công):**
  - Thiết lập môi trường Python (`.venv`) và cài đặt các thư viện cần thiết trong `src/requirements.txt`.
  - Xây dựng 3 hàm kinh tế chạy lại (A1) và hàm mô hình chi phí từ trace `mo_hinh(...)` (A2) trong `src/lab13.py` với đầy đủ tham số (`gia_vao`, `gia_ra`, `gia_tool`, `luong_phut`, `he_so_xem_lai`, `he_so_lam_lai`, `max_lan_chay`) để thành viên CP2 tái sử dụng trực tiếp.
  - Tính toán phân tách chi phí theo 4 loại yêu cầu và tỉ lệ thành công theo từng lần chạy (A3), tính tác động chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (A4).
  - Hoàn thiện mục A1–A4 trong `report/team/bang_chi_phi.md` (gắn nhãn `simulated` đầy đủ cho mọi con số từ cột `_simulated`).
- **CP5 · Tổng hợp nhóm & duyệt chéo Gate 2a:** đóng góp phần số liệu mô hình chi phí, tham gia tổng hợp hồ sơ launch v0 và phản biện/bảo vệ số liệu kinh tế trước hội đồng.

## 3. Đóng góp cụ thể

- Viết và kiểm chứng 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) trong `src/lab13.py`: vượt qua 100% ba phép thử đáp án biết trước (`1,20` · `1,25` · `1,25`).
- Viết hàm `mo_hinh(runs, reqs, ...)` đọc `logix_requests.csv` với `keep_default_na=False`, cộng chi phí token + tool trên mọi lần chạy (kể cả lần lỗi), chỉ chia cho số yêu cầu `ket_qua == 'thanh_cong'`, đồng thời hỗ trợ sẵn tham số giới hạn số lần chạy (`max_lan_chay`) cho CP2.
- Tính toán đầy đủ và điền phần A1–A4 trong `report/team/bang_chi_phi.md`:
  - **A2:** Tổng chi phí `4.373.585 đ` (có phần `simulated`), `978` việc thành công, chi phí mỗi việc thành công **4.472 đ** (`simulated`) — gấp **16,3 lần** hoá đơn token + tool mỗi yêu cầu (`274,7 đ`). Giờ nhân viên chiếm **92,5%** tổng chi phí (làm lại `51,8%`, xem lại `40,7%`, `simulated`). Chi phí cả hệ thống (cộng 222 ca không thành công) là **5.865 đ/yêu cầu = 0,49×** so với nhân viên tự làm (`12.000 đ`, `simulated`).
  - **A3:** Chỉ ra `noi_dia` (`2.696 đ = 0,22×`, `simulated`) và `hang_nang` (`8.221 đ = 0,69×`, `simulated`) phù hợp đưa vào phạm vi pilot; loại `quoc_te` (`22.515 đ = 1,88×`, `simulated`, thành công `27,3%`, tỉ lệ `ok` qua 3 lần chạy tụt `30,0% → 11,4% → 2,2%`) và `doi_tac` (`10.215 đ = 0,85×`, `simulated`, có điều khoản riêng).
  - **A4:** Cộng chi phí cố định `40 triệu đ/tháng` cho phạm vi `noi_dia` + `hang_nang` (`900/1.200` yêu cầu thành công trong mẫu): ở quy mô `45.000 yc/tháng` là **4.599 đ = 0,38×** (`simulated`); ở một nửa khối lượng là **5.784 đ = 0,48×** (`simulated`).

## 4. Bằng chứng

- Nhánh Git thực hiện CP1: `cp1` (chỉ chỉnh sửa các file thuộc CP1, không gây xung đột phần việc của thành viên khác).
- Code đã viết và chạy thành công: `src/lab13.py` (in `Ba phép thử đáp án biết trước: ĐẠT` cùng đầy đủ bảng A1, A2, A3, tỉ lệ `ok` theo `loai × attempt`, và bảng A4).
- Báo cáo số liệu CP1: mục A1–A4 trong `report/team/bang_chi_phi.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI (Antigravity / Gemini) hỗ trợ đọc tài liệu dự án, lập kế hoạch phân chia công việc theo CP, gợi ý triển khai hàm `mo_hinh(...)` và rà soát quy tắc trình bày.
- **Cách tự kiểm tra:**
  - Chạy trực tiếp `python lab13.py` trong môi trường `.venv` (thư mục `src/`) trên 2 file dữ liệu gốc `logix_runs.csv` và `logix_requests.csv` (không sửa dữ liệu gốc và không sửa `lab13_starter.py`).
  - Xác nhận in ra `Ba phép thử đáp án biết trước: ĐẠT` (`1,20 · 1,25 · 1,25`).
  - Tự đối chiếu từng khoản chi phí A2, 4 dòng A3, tỉ lệ `ok` theo lần chạy và 2 mức khối lượng A4 với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai số 0%).
  - Rà soát thủ công và bằng lệnh tìm kiếm để đảm bảo mọi con số tính từ cột `_simulated` đều có nhãn `simulated`, câu trả lời ngắn ≤ 3 dòng có số liệu, và không chứa từ cấm trong hồ sơ.

## 6. Tự đánh giá

- **Hoàn thành:** Đạt 100% yêu cầu CP1 (Nhiệm vụ A) đúng tiến độ, code sạch và thiết kế sẵn tham số `mo_hinh(...)` giúp bạn làm CP2 triển khai bảng độ nhạy nhanh chóng, đồng thời cung cấp số liệu A3 rõ ràng cho bạn làm CP4 chốt phạm vi pilot.
- **Bài học rút ra:** Trong đánh giá kinh tế agent, hoá đơn token/tool chỉ là phần rất nhỏ (`274,7 đ/yêu cầu`), còn thời gian xem lại và làm lại của nhân viên mới quyết định chi phí thật (`92,5%` tổng chi phí, `simulated`). Khi so sánh với quy trình thủ công (`12.000 đ`), bắt buộc tính chi phí cả hệ thống (bao gồm các ca phải chuyển nhân viên) và tách theo từng phân khúc yêu cầu thay vì nhìn số trung bình chung.
- **Cần làm tiếp:** Merge nhánh `cp1` cùng nhóm sau khi các CP khác sẵn sàng, điền thông tin đóng góp vào `TEAM.md` và cùng 3 thành viên còn lại hoàn thiện CP5 + duyệt chéo Gate 2a.
