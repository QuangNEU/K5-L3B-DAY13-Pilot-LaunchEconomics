# Hồ sơ nhóm

| File | Nhiệm vụ | Ai điền | Ghi chú |
|---|---|---|---|
| `bang_chi_phi.md` | A, B | Người viết code, người kiểm số | Bảng A1, A2, A3, độ nhạy, trả lời B3 và B4 |
| `bang_loi.md` | C | Hai người gắn nhãn | Hai bộ nhãn độc lập, tỉ lệ đồng thuận, bảng khắc phục 5 ca |
| `pilot_plan.yaml` | D | Cả nhóm | Không còn dấu `?` ngoài dòng chú thích; đọc được bằng `yaml.safe_load` |
| `chi_so.md` | E | Cả nhóm | Đặc tả chỉ số, danh sách event, rủi ro kinh tế |
| `ho_so_launch_v0.md` | E | Người giữ hồ sơ | Một trang, bảy mục, dòng cuối là đề xuất |
| `phieu_cham.md` | Duyệt chéo | Cả nhóm (làm hội đồng) | Phiếu nhóm mình chấm nhóm n + 1 |
| `group_report.md` | | Cả nhóm | Báo cáo nhóm ngắn |
| `MSSV_HoTen.md` | | Từng thành viên | File mẫu. Mỗi người copy thành file riêng |

Giữ nguyên tên các file trên để trợ giảng đối chiếu được.

Mỗi thành viên tạo thêm một báo cáo cá nhân:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Đóng góp và bằng chứng của từng thành viên cũng phải được khai báo trong `TEAM.md`.

## Phần việc của Nguyễn Nhật Minh

### Đã hoàn thành

- [x] Đọc hiểu nhãn lỗi và số liệu; Minh đã xác nhận.
- [x] Hoàn thiện nhãn người 2, đồng thuận 17/20=85%, chốt ca 9,13,20 và tiếp nhận bảng khắc phục năm ca.
- [x] Tổng hợp CP1–CP2, giữ nguồn, đơn vị và nhãn `simulated`.
- [x] Nhận bản CP4/CP5 tại `8a6ad1c`: bốn luật dừng, năm chỉ số, mười event có `trace_id`, ánh xạ chỉ số và ba rủi ro.
- [x] Đối chiếu ba chỉ số: 82,83% chính, 27,12% bỏ qua gợi ý, 4,25% mở lại; cỡ mẫu hiệu dụng `20×299/6,96≈859,20`.
- [x] Đồng bộ bảy mục hồ sơ launch, báo cáo nhóm và báo cáo cá nhân theo đề xuất No-go trên main.
- [x] Nhận và cập nhật phiếu **Pilot chấm G2026** từ `b4eb099` (PR #15): 10+10+10=30/30, Go có điều kiện; có hỏi–đáp thực tế.
- [x] Cập nhật thông tin thành viên từ main, giữ đóng góp của các thành viên khác trong TEAM.md.
- [x] Xử lý xung đột TEAM.md, báo cáo nhóm và phiếu chấm; giữ bản CP4/CP5 mới và dữ liệu hai bộ nhãn.
- [x] Ghi nhận việc mọi thành viên đã nộp LMS theo checklist nhóm tại `7e12e19`, `ab4ef82`; đây là xác nhận từ hồ sơ nhóm.
- [x] Kiểm tra code, YAML, số liệu, liên kết và định dạng trước khi commit/push bản giải quyết xung đột.

### Bàn giao hồ sơ

Các đầu việc cá nhân trong checklist trên đã hoàn thành. Phiếu Pilot chấm G2026 đã có trong repo; kết quả hội đồng khác chấm Pilot được lưu theo phiếu của nhóm hội đồng đó.

Kế hoạch Pilot: quyết định **05/01/2027**, rollback **30 phút**. Mốc **15/01/2027** và **15 phút** trong phiếu chấm thuộc **G2026**. Kết luận Pilot vẫn là **No-go** theo hồ sơ nhóm; kết quả Pilot chấm G2026 là **Go có điều kiện**.

### Chạy lại kiểm tra

Từ thư mục gốc repo trong PowerShell:

```powershell
$labPython = Join-Path $env:TEMP 'lab13-minh-venv\Scripts\python.exe'
Push-Location src
try { & $labPython -X utf8 lab13.py } finally { Pop-Location }
```

Môi trường riêng ở Temp giúp tránh đường dẫn OneDrive dài. Nếu cần tạo lại, làm theo `src/README.md` với đường dẫn môi trường ngắn.
