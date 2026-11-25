# Báo cáo cá nhân — NguyenNhuDuyAn-2A202603783

## 1. Thông tin thành viên

- Họ tên: Nguyễn Như Duy An
- MSSV: 2A202603783
- Email: 26ai.annnd@vinuni.edu.vn
- GitHub: `K0heii`
- Vai trong nhóm: Người viết code (phụ trách chính CP1 · Nhiệm vụ A; hỗ trợ hoàn thiện code CP2, toàn bộ CP4 và tổng hợp CP5 cùng nhóm)

## 2. Phần việc phụ trách

- **CP1 · Nhiệm vụ A (Mô hình chi phí mỗi việc thành công):**
  - Thiết lập môi trường Python (`.venv`) và cài đặt các thư viện trong `src/requirements.txt`.
  - Viết 3 hàm kinh tế chạy lại (A1) và hàm mô hình chi phí từ trace `mo_hinh(...)` (A2) trong `src/lab13.py` với đầy đủ tham số (`gia_vao`, `gia_ra`, `gia_tool`, `luong_phut`, `he_so_xem_lai`, `he_so_lam_lai`, `max_lan_chay`).
  - Phân tách chi phí theo 4 loại yêu cầu + tỉ lệ `ok` theo từng lần chạy (A3), tính tác động chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (A4), và điền đầy đủ phần A1–A4 trong `report/team/bang_chi_phi.md`.
- **Hỗ trợ hoàn thiện code CP2 (Nhiệm vụ B) & toàn bộ CP4 (Nhiệm vụ D):**
  - Bổ sung hàm `in_ket_qua_cp2` (B1–B4) và `co_mau`, `in_ket_qua_cp4` (5 câu cỡ mẫu D1, power `statsmodels`, tỉ lệ `mo_lai_trong_7_ngay`) vào `src/lab13.py`.
  - Hoàn thiện toàn bộ `report/team/pilot_plan.yaml` (chú thích D1/D2, đánh đổi MDE +6 điểm, đủ 11 trường YAML, không còn dấu `?`, 4 luật dừng chuẩn 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` và tách riêng luật 0 ca hoàn tiền trùng tắt trong 30 phút).
- **CP5 · Tổng hợp nhóm & rà soát chất lượng cuối buổi:**
  - Bổ sung `in_ket_qua_cp5` tính 3 chỉ số E1 trong `src/lab13.py`.
  - Hoàn thiện `report/team/chi_so.md` (5 chỉ số E1, 10 event có `trace_id`, ánh xạ chéo event–chỉ số, 3 dòng rủi ro kinh tế E2).
  - Đồng bộ `report/team/ho_so_launch_v0.md` (giữ đề xuất `No-go` nhất quán với bằng chứng), `report/team/group_report.md`, `TEAM.md` và rà soát toàn bộ checklist nộp bài trước deadline.

## 3. Đóng góp cụ thể

- **CP1 (A1–A4):**
  - Ba hàm A1 vượt qua 100% ba phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`).
  - Hàm `mo_hinh(...)` đọc `logix_requests.csv` với `keep_default_na=False`, tính mọi lần chạy kể cả lần lỗi ở tử số và chỉ chia cho `978` việc `thanh_cong`: tổng chi phí `4.373.585 đ` (có phần `simulated`), **CPS = `4.472 đ`** (`simulated`, gấp **16,3×** hoá đơn token + tool `274,7 đ/yc`), giờ nhân viên chiếm **92,5%** (làm lại `51,8%`, xem lại `40,7%`, `simulated`). Chi phí cả hệ thống (cộng 222 ca không thành công) là **`5.865 đ/yc = 0,49×`** so với `12.000 đ` (`simulated`).
  - A3 chỉ ra `noi_dia` (`2.696 đ = 0,22×`) và `hang_nang` (`8.221 đ = 0,69×`) phù hợp pilot; loại `quoc_te` (`22.515 đ = 1,88×`, tỉ lệ `ok` tụt `30,0% → 11,4% → 2,2%`) và `doi_tac` (`10.215 đ = 0,85×`) (`simulated`).
  - A4 cộng cố định `40 triệu đ/tháng` cho `noi_dia` + `hang_nang`: **`4.599 đ = 0,38×`** ở `45.000 yc/tháng` và **`5.784 đ = 0,48×`** ở một nửa khối lượng (`simulated`).
- **CP2 (code B1–B4) & CP4 (code D1 + `pilot_plan.yaml`):**
  - Xác nhận trong code `src/lab13.py` toàn bộ 9 kịch bản B1, đổi cặp B2 (`6.543 đ`, `+46,3%`), B3 (giới hạn **2 lần** rẻ nhất cả hệ thống: `6.901.220 đ`), B4 xem lại 100% (`11.743 đ = 0,98×` ở 9 phút làm lại và `12.415 đ = 1,03×` ở trung bình thực tế `15,3` phút/ca, hoà vốn `≤ 4,8–5,1 phút`, `simulated`).
  - Tính đủ 5 câu D1 (`1.251`, `3.103 / 42 NV`, trần `1.000`, trần `300`, MDE 6 điểm `n = 859` → `m ≥ 299` yc/NV, `DE = 6,96`), power thực tế `~0,64` ở mức +5 điểm (`NormalIndPower`), và tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu, `3,97%` phạm vi pilot); hoàn thiện `pilot_plan.yaml` đọc sạch bằng `yaml.safe_load`.
- **CP5 (`chi_so.md` & đồng bộ hồ sơ):**
  - Tính 3 chỉ số đợt chạy thử (`82,83%`, `27,12%`, `4,25%`), thiết kế 2 chỉ số bổ sung, 10 event mang `trace_id`, ánh xạ chéo và 3 dòng rủi ro kinh tế trong `report/team/chi_so.md`.
  - Tách riêng luật dừng 0 ca hoàn tiền trùng (tắt trong 30 phút) trong `pilot_plan.yaml` và đồng bộ `ho_so_launch_v0.md`, `group_report.md`, `TEAM.md`.

## 4. Bằng chứng

- **Commit CP1 (nhánh `cp1`, merge PR #1 `46d4d02`):** `6aa5a90` — `src/lab13.py` (A1–A4), `report/team/bang_chi_phi.md` (A1–A4), `report/team/2A202603783_NguyenNhuDuyAn.md`.
- **Commit bổ sung code CP2 & hoàn thiện CP4 trên `main`:** `f1104de` — `src/lab13.py` (B1–B4, D1), `report/team/pilot_plan.yaml`.
- **Commit hoàn thiện CP5 & đồng bộ hồ sơ trên `main`:** `8a6ad1c` — `src/lab13.py` (E1), `report/team/chi_so.md`, `report/team/pilot_plan.yaml` (tách luật hoàn trùng), `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md`.
- **Kiểm chứng độc lập:** `src/lab13.py` đã chạy trọn vẹn không lỗi và cho kết quả khớp 100% trên cả máy của An và máy của Nguyễn Nhật Minh.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI (Antigravity / Gemini) dùng để đọc cấu trúc repo, lập kế hoạch chia việc theo CP, gợi ý triển khai hàm trong `src/lab13.py`, trình bày bảng Markdown/YAML và rà soát checklist trước khi nộp.
- **Cách tự kiểm tra:**
  - Chạy trực tiếp `python lab13.py` trong môi trường `.venv` tại `src/` trên 2 file CSV gốc (không sửa dữ liệu gốc và không sửa `lab13_starter.py`), xác nhận in `Ba phép thử đáp án biết trước: ĐẠT` (`1,20 · 1,25 · 1,25`) và đủ bảng A, B, D1, E1.
  - Tự đối chiếu từng con số với `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai số 0%) và đối chiếu chéo với bảng độ nhạy do Nguyễn Minh Quang thực hiện.
  - Kiểm tra tự động bằng `yaml.safe_load` trên `report/team/pilot_plan.yaml`, rà 0 dấu `?` ngoài chú thích, 0 từ cấm trong `report/team/`, và kiểm tra đầy đủ nhãn `simulated` trên mọi số dùng cột `_simulated`.

## 6. Tự đánh giá

- **Kết quả đạt được:** Hoàn thành trọn vẹn 100% phần việc được giao ở CP1, đồng thời chủ động hỗ trợ hoàn thiện code CP2, toàn bộ CP4, đặc tả `chi_so.md` và rà soát đồng bộ hồ sơ CP5 giúp nhóm chốt đủ 6/6 file hồ sơ nhóm và 4/4 báo cáo cá nhân đúng hạn.
- **Bài học rút ra:** Kinh tế vận hành agent không thể nhìn vào hoá đơn token (`274,7 đ/yc`) mà phải tính cả giờ nhân viên xem lại và làm lại (`92,5%` tổng chi phí, `simulated`) cùng chi phí các ca chuyển nhân viên (`5.865 đ/yc`). Về thiết kế thử nghiệm, số cụm nhân viên (`20 + 20`) đặt trần cỡ mẫu hiệu dụng (`c / ICC = 1.000`), đòi hỏi minh bạch đánh đổi power (`0,64` ở mức +5 điểm) và luật dừng an toàn tách bạch (0 ca hoàn trùng phải dừng ngay, không gộp vào cửa sổ 3 ngày).
