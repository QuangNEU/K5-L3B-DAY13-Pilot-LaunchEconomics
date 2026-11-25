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

### Việc đã xong

- [x] Nhãn người 2, đồng thuận 85% và nhãn chốt ca 9,13,20.
- [x] Tổng hợp CP1 của Nguyễn Như Duy An và CP2 của Nguyễn Minh Quang vào hồ sơ.
- [x] Nhận bảng khắc phục 5 ca của Quân tại 7752d2a/ea2e38c; cập nhật mục 5 hồ sơ launch.
- [x] Báo cáo cá nhân đã hoàn thiện; PR #10 đã được merge vào main tại `0b1006c`.
- [x] Nhận bản CP4 của An tại `f1104de`, đọc YAML, kiểm tra không còn dấu hỏi ngoài chú thích; đối chiếu `20×299/6,96≈859,20` yêu cầu hiệu dụng/nhóm.
- [x] Cập nhật mục 6 hồ sơ launch, báo cáo nhóm và báo cáo cá nhân theo bản CP4 hiện có; ghi điểm cần xác nhận về luật hoàn trùng.
- [x] Đối chiếu nhãn và số tổng hợp CP1–CP2 với nguồn; giữ nhãn `simulated`, đơn vị và phạm vi.
- [x] Kiểm tra `src/lab13.py` trên máy Minh: chương trình chạy hết, ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25), A–B và D1 khớp hồ sơ.
- [x] Tính và đối chiếu ba chỉ số nền từ CSV: 82,83% chính, 27,12% bỏ qua gợi ý, 4,25% mở lại; ghi cách đếm trong hồ sơ.
- [x] Hoàn thiện bảy mục `ho_so_launch_v0.md`, bổ sung vai trò vận hành đề xuất, hai rủi ro kinh tế và kết luận No-go kèm việc để quay lại Gate 2a.
- [x] Tổng hợp họ tên, MSSV, email và vai trò của đủ bốn thành viên từ báo cáo cá nhân vào TEAM.md.
- [x] Chuẩn bị ba ý giải trình bằng số ở mục 4 báo cáo nhóm và câu hỏi dự kiến trong phiếu chấm. Các ô kết quả thực tế được để trống.

### Việc Minh cần làm ngay

- [x] **Đọc hiểu CP3 và số liệu:** Minh đã xác nhận đọc hiểu các nhãn, lý do phân biệt và số trong hồ sơ.
- [ ] **Bổ sung thông tin còn thiếu:** nhận GitHub của An, Quang, Quân; tên người chủ trì đặc tả CP5 và commit nộp cuối. Điền các ô trống tương ứng trong `../../TEAM.md`.
- [x] **Nhận xác nhận CP4 đã chốt:** Minh xác nhận nhóm đã chốt. Đã fetch và đối chiếu main: bản mới nhất vẫn là `f1104de`, trùng bản đang dùng. Điểm diễn đạt luật hoàn trùng được giữ trong hồ sơ để làm rõ trước khi mở pilot.

### Việc cần bàn giao hoặc thống nhất

- [x] **CP4:** đã nhận bản chốt theo xác nhận của Minh; cập nhật mục 6 hồ sơ và mục 3,5 báo cáo nhóm. Chưa có commit sửa luật hoàn trùng trên các nhánh đã fetch.
- [ ] **E1–E2 — nhóm cần chỉ định người chủ trì CP5:** nhận `chi_so.md` có ba chỉ số tính thử, thêm một chỉ số dùng và một an toàn, ít nhất sáu event có `trace_id`, ánh xạ event–chỉ số và hai rủi ro kinh tế. Ba số nền và hai rủi ro đã có trong hồ sơ; Minh đối chiếu lại với bản đặc tả được bàn giao, Quang hỗ trợ kiểm số.
- [ ] **Trình đề xuất — cùng nhóm và hội đồng:** dùng hồ sơ No-go hiện tại, nêu rõ các việc cần làm để quay lại Gate 2a. Ghi quyết định thực tế tại mục 4 báo cáo nhóm và cập nhật hồ sơ nếu có thay đổi; các vai trò vận hành hiện là phân công đề xuất.
- [ ] **Duyệt chéo — theo phân công của lớp:** khi nhóm chấm nhóm khác, điền tên hai nhóm, điểm ba tiêu chí, tổng /30, quyết định, lý do và hỏi–đáp trong `phieu_cham.md`. Phản hồi dành cho nhóm mình ghi vào mục 4 `group_report.md`, kèm việc cần sửa.

Các ô hiện để trống: nhóm được chấm, điểm và tổng điểm, quyết định hội đồng, nhận xét, hỏi–đáp thực tế, kết luận nhóm đã thống nhất và việc sửa sau duyệt. Câu hỏi dự kiến và phần chuẩn bị giải trình chỉ dùng để chuẩn bị buổi duyệt.
- [ ] **LMS — Minh tự nộp sau khi nhóm trưởng chốt commit:** mở repo kiểm tra truy cập được, đăng nhập LMS, vào bài Lab 13, dán link repo nhóm và bấm nộp. Kiểm tra trạng thái nộp thành công rồi cập nhật báo cáo cá nhân.

### Kiểm tra lại trước khi chốt hồ sơ

- [x] `ho_so_launch_v0.md` đủ bảy mục; mỗi mục có số chính, trạng thái và vai trò cụ thể; dòng cuối có đề xuất.
- [x] Đối chiếu số với bảng A–B, bảng lỗi, YAML và CSV; các mục 1,2,3,7 ghi Giả lập và có nhãn `simulated`.
- [ ] Đối chiếu lại mục 4,7 với đặc tả `chi_so.md` khi người phụ trách hoàn thiện.
- [ ] Kiểm tra liên kết, quyết định cuối, phản hồi duyệt chéo và thông tin nhóm trước khi chốt bản nộp.

Để chạy lại trên máy Minh bằng môi trường riêng (từ thư mục gốc repo, PowerShell):

```powershell
$labPython = Join-Path $env:TEMP 'lab13-minh-venv\Scripts\python.exe'
Push-Location src
try { & $labPython -X utf8 lab13.py } finally { Pop-Location }
```

Môi trường đặt ở đường dẫn ngắn trong Temp để tránh lỗi cài thư viện do đường dẫn OneDrive dài. Nếu Temp đã bị dọn, tạo lại bằng `python -m venv --system-site-packages "$env:TEMP\lab13-minh-venv"` và cài bằng `& $labPython -m pip install -r src/requirements.txt` từ gốc repo.
