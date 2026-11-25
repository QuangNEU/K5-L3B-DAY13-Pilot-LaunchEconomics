# Báo cáo nhóm

Báo cáo ngắn (≤ 2 trang). Số liệu chi tiết nằm trong các file hồ sơ; báo cáo này dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: **Pilot**
- Lớp: **L3B**
- Repo nhóm: `K5-L3B-DAY13-Pilot-LaunchEconomics`
- Thành viên và đóng góp chi tiết: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN tại cổng **Gate 2a** từ mẫu giả lập 1.200 yêu cầu (1.624 lần chạy) nhằm trả lời bốn câu hỏi: chi phí thật mỗi việc thành công, mức độ sử dụng và sự sẵn sàng đo lường, phân loại và khắc phục lỗi, và thiết kế pilot đủ bằng chứng ra quyết định. Nhóm phân công mỗi thành viên phụ trách chính một checkpoint (CP1–CP4), kiểm tra chéo mã nguồn trên hai máy độc lập và cùng tổng hợp CP5.

## 3. Giải pháp

- **Nhiệm vụ A (CP1 — Mô hình chi phí):** Viết 3 hàm A1 và hàm `mo_hinh(...)` trong [src/lab13.py](../../src/lab13.py) (đọc CSV với `keep_default_na=False`, cộng mọi lần chạy kể cả lỗi, chia cho số ca `thanh_cong`), tách theo 4 loại yêu cầu (A3) và cộng chi phí cố định 40 triệu đ/tháng (A4). Chi tiết: [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (CP2 — Bảng độ nhạy):** Chạy 9 kịch bản đơn biến (B1), kịch bản đổi cặp (B2), chi phí cả hệ thống cho giới hạn 1–3 lần chạy (B3) và kịch bản xem lại 100% theo cả hai mức thời gian làm lại 9 phút và 15,3 phút (B4) trong [src/lab13.py](../../src/lab13.py) và [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (CP3 — Bảng lỗi & khắc phục):** Hai thành viên (Nguyễn Minh Quân và Nguyễn Nhật Minh) gắn nhãn độc lập 20 ca lỗi theo 5 nhóm Google PAIR trước khi so sánh, thống nhất 3 ca khác biệt theo nguyên nhân gốc và xây bảng khắc phục cho 5 ca đại diện đủ 5 loại lỗi trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (CP4 — Kế hoạch pilot):** Tính 5 câu cỡ mẫu D1 và power thực tế bằng `statsmodels` trong [src/lab13.py](../../src/lab13.py), trả lời 5 câu kiểm tra tách tác động D2 và chốt 4 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (CP5 — Chỉ số, rủi ro & hồ sơ launch v0):** Tính thử 3 chỉ số trên 1.200 yêu cầu, đề xuất 2 chỉ số mới, thiết kế 10 event mang `trace_id` có ánh xạ chéo và 3 dòng rủi ro kinh tế trong [chi_so.md](chi_so.md); tổng hợp thành hồ sơ một trang 7 mục tại [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí (A & B):** Ba phép thử A1 đạt 100% (`1,20 · 1,25 · 1,25`). CPS toàn mẫu là **4.472 đ/việc** (`simulated`), gấp **16,3×** hoá đơn token + tool (`274,7 đ/yc`); giờ nhân viên chiếm **92,5%** (làm lại `51,8%`, xem lại `40,7%`, `simulated`). Chi phí cả hệ thống là **5.865 đ/yc = 0,49×** mốc thủ công 12.000 đ (`simulated`). Phạm vi khả thi gồm `noi_dia` (`2.696 đ = 0,22×`) và `hang_nang` (`8.221 đ = 0,69×`), CPS cộng cố định là **4.599 đ (0,38×)** ở 45.000 yc/tháng và **5.784 đ (0,48×)** ở nửa khối lượng (`simulated`); loại `quoc_te` (`22.515 đ = 1,88×`) và `doi_tac` (`10.215 đ = 0,85×`). Giới hạn **2 lần chạy** rẻ nhất cả hệ thống (**6.901.220 đ**, `simulated`). Nếu xem lại 100%, CPS vọt lên **11.743 đ (0,98×)** đến **12.415 đ (1,03×)** (`simulated`).
- **Lỗi (C):** Đồng thuận độc lập **17/20 = 85%**; chốt 3 ca khác biệt (`9: Do người dùng`, `13: Giới hạn hệ thống`, `20: Hệ thống`); bảng khắc phục đủ 5 loại qua ca `6, 7, 16, 11, 5`.
- **Pilot (D) & Chỉ số (E):** Chia ngẫu nhiên theo nhân viên **20 + 20** (phân tầng depot), MDE **+6 điểm** (`n = 859`/nhóm, `m ≥ 299` yc/NV, `DE = 6,96`, power thực tế ≈ **0,64** nếu tác động thật +5 điểm), 4 luật dừng (tách riêng 0 ca hoàn trùng tắt trong 30 phút), ngày quyết định `2027-01-05`. Chỉ số đợt chạy thử: đóng 24h & không mở lại 7 ngày **82,83%** (`994/1.200`), bỏ qua gợi ý **27,12%** (`48/177`), mở lại 7 ngày **4,25%** (`51/1.200`).
- **Đề xuất cuối tại [ho_so_launch_v0.md](ho_so_launch_v0.md):** **No-go** — chưa mở pilot cho tới khi hoàn tất 4 điều kiện quay lại Gate 2a (khoá chống trùng + đối soát sổ cái + bật 10 event `trace_id`; cơ chế đo phút thật & lộ trình giảm xem lại; kiểm toán mẫu 100 đơn/tuần; và phê duyệt đánh đổi MDE +6 điểm).
- **Duyệt chéo Gate 2a:** Nhóm Pilot đã hoàn tất chấm nhóm **G2026** trong vai trò hội đồng tại [phieu_cham.md](phieu_cham.md) (tổng điểm **30/30**, quyết định **Go có điều kiện**, kèm câu hỏi về power `0,64` ở mức +5 điểm và phần trả lời của đội trình). Kết quả hội đồng khác chấm nhóm Pilot được lưu theo phiếu của nhóm hội đồng.

## 5. Khó khăn và cách xử lý

- **Môi trường Python khác nhau giữa các máy:** Máy của Nguyễn Nhật Minh gặp lỗi thiếu `statsmodels` và đường dẫn OneDrive quá dài khi tạo `.venv` trong repo; nhóm xử lý bằng cách tạo môi trường ảo riêng tại `%TEMP%\lab13-minh-venv`, cài đủ `src/requirements.txt` và chạy `python -X utf8 lab13.py` trong `src/` — kết quả khớp 100% trên cả máy An và máy Minh.
- **Mâu thuẫn diễn đạt trong luật dừng CP4:** Khi tổng hợp hồ sơ, người giữ hồ sơ phát hiện luật dừng đầu tiên gộp điều kiện `>= 1 ca hoàn trùng` chung với cửa sổ `3 ngày liên tiếp`. Nhóm đã tách thành 2 luật dừng riêng trong [pilot_plan.yaml](pilot_plan.yaml) để đảm bảo 0 ca hoàn trùng kích hoạt rollback trong 30 phút ngay khi phát hiện.

## 6. Tổng hợp đóng góp

Chi tiết vai trò, phần việc, đóng góp và bằng chứng của từng thành viên (Nguyễn Như Duy An, Nguyễn Minh Quang, Nguyễn Minh Quân, Nguyễn Nhật Minh) được ghi đầy đủ trong [TEAM.md](../../TEAM.md) và 4 báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- **Phụ thuộc dữ liệu giả lập:** 92,5% tổng chi phí (`4.044.000 / 4.373.585 đ`) đến từ hai cột `_simulated`; cần đo trực tiếp `phut_xem_lai` và `phut_lam_lai` qua event ngay từ tuần 1 của pilot.
- **Độ nhạy lớn với tỉ lệ xem lại & giới hạn cỡ mẫu:** Xem lại 100% làm mất hoàn toàn lợi ích chi phí (`12.415 đ = 1,03×`, `simulated`), và với 40 nhân viên, power giảm còn ~0,64 ở mức chênh +5 điểm. Hướng cải thiện là xây dựng quy tắc giảm xem lại theo bậc dựa trên độ tin cậy từng phân khúc và kéo dài thời gian thu mẫu nếu cần tăng power.

## 8. Tài liệu tham khảo

- Đề bài và quy định repo: [README.md](../../README.md), [RULES.md](../../RULES.md), [CHECKPOINTS.md](../../CHECKPOINTS.md), [RUBRIC.md](../../RUBRIC.md), [docs/du_lieu_va_cong_thuc.md](../../docs/du_lieu_va_cong_thuc.md).
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com.
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`).
