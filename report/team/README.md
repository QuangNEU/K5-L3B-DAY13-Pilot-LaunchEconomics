# Báo cáo nhóm

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

### Đã có kết quả

- [x] Nhãn người 2, đồng thuận 85% và nhãn chốt ca 9,13,20.
- [x] CP1 của Nguyễn Như Duy An, CP2/kiểm số của Nguyễn Minh Quang đã có nguồn để tổng hợp.
- [x] Nguyễn Minh Quân đã hoàn thiện bảng khắc phục 5 ca, merge tại 7752d2a/ea2e38c; cập nhật mục 5 hồ sơ launch.

### Làm được ngay

- [ ] Kiểm tra email/GitHub của Minh, tên nhóm và phân công còn thiếu trong TEAM.md; xác nhận thông tin trong báo cáo cá nhân.
- [ ] Đọc lại lý do ba ca bất đồng và bảng khắc phục của Quân để giải thích được phần CP3.
- [ ] Kiểm tra số tổng hợp ở mục 1,2,3 của hồ sơ với bảng chi phí đã được An/Quang bàn giao; ghi việc đã tự kiểm trong báo cáo cá nhân.
- [ ] Hoàn thiện phần đóng góp và bằng chứng cá nhân; giữ mục công cụ AI theo RULES.md.
- [ ] Nhờ nhóm ghi tên người chủ trì CP4 và CP5 vào phân công: repo hiện chưa chỉ rõ hai đầu mối này.

### Đợi bàn giao

| Cần nhận | Đợi ai | Minh làm sau khi nhận |
| --- | --- | --- |
| D1–D2, YAML pilot, luật dừng, ngày quyết định | Người chủ trì CP4 chưa được ghi tên; An hỗ trợ code, Quang kiểm số theo vai đã khai báo | Rà bản chốt, cập nhật mục 6 hồ sơ; không tự đặt cấu hình/lịch thay nhóm |
| E1, event và E2 | Người chủ trì CP5 chưa được ghi tên; Quang hỗ trợ đối chiếu E1, An cung cấp số chi phí | Cập nhật mục 4,7; kiểm nguồn, đơn vị và nhãn simulated |
| Go/Go có điều kiện/No-go, vai trò và ngày kiểm tra | Cả nhóm | Ghi kết luận cuối và điều kiện vào hồ sơ |
| Điểm, câu hỏi, trả lời và phản hồi duyệt | Hội đồng được lớp phân công và nhóm mình | Điền phiếu chấm, mục 4 báo cáo nhóm |
| Commit nộp cuối và LMS | Nhóm trưởng chốt bản chung; Minh tự nộp LMS | Kiểm repo truy cập được, nộp link bằng tài khoản cá nhân |

Phần của Minh không bao gồm viết/sửa code tính A–B–D1–E1, tự hoàn thiện YAML CP4 hoặc tự chốt đặc tả CP5 thay người phụ trách.
