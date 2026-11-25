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

## Người gắn nhãn 2, kiêm giữ hồ sơ

**Nguyễn Nhật Minh · 2A202603745 · Nhánh NguyenNhatMinh.** Xem [hướng dẫn từng bước](../../docs/huong_dan_nguoi_gan_nhan_2.md). Tick bằng `- [x]` sau khi có bằng chứng; các ô còn lại là việc Minh/nhóm cần thực hiện.

### Việc đã làm được

- [x] Điền họ tên, MSSV, vai, lớp L3B, repo và email từ cấu hình Git; tạo báo cáo cá nhân.
- [x] Điền 20 nhãn người 2, đã đẩy commit `21ec49a`; cột người 1 và các cột kết quả chưa được điền thay.
- [x] Chuẩn bị phiếu 20 tình huống kèm lý do gợi ý, giữ dấu xác nhận của Minh và chuẩn hoá `[v]` thành `[x]`.
- [x] Đối chiếu với bản Nguyễn Minh Quân đã commit: **17/20=85%**, khác ca 9,13,20; có [bảng và lý do trao đổi](doi_chieu_nhan_Minh.md).
- [x] Nhận CP1–CP2 đã merge tại `3f69dbf`; đối chiếu lại số từ chương trình và CSV, lưu log.
- [x] Cập nhật mục 1, 2, 3, 7 hồ sơ launch từ nguồn chi phí; ghi số CSV đối chiếu để chờ nhận E1.
- [x] Tổng hợp báo cáo nhóm và báo cáo cá nhân, để đúng các phần chờ duyệt thực tế.
- [x] Ghi hướng dẫn từng việc còn lại theo file, mục/cột cần điền và tiêu chí hoàn thành.

### Việc Minh cần thực hiện

- [ ] Kiểm tra email, điền GitHub, tên nhóm và xác nhận phân công tại TEAM.md; đồng bộ thông tin vào báo cáo cá nhân/nhóm và đầu hồ sơ.
- [ ] Rà nhãn/lý do của ca 2–20 trên phiếu riêng; tick sau khi xác nhận, sửa nhãn người 2 nếu cần và ghi giờ chốt thực tế.
- [ ] Cùng Quân xác nhận hai bản cuối, thảo luận ca 9,13,20 và chốt năm ca/giải pháp; nhờ người 1 tự cập nhật cột của mình. Tính lại nếu bộ nhãn thay đổi.
- [ ] Tự kiểm một phép tính và ghi nguồn/kết quả tại mục 4, 5 báo cáo cá nhân; thêm xác nhận vào nhật ký bên dưới.
- [ ] Nhận D1–D2, YAML hoàn chỉnh và lịch từ người phụ trách CP4; nhận E1/event/rủi ro E2 từ người phụ trách CP5.
- [ ] Cập nhật mục 4–6 hồ sơ launch, cùng nhóm chốt vai trò, quyết định, điều kiện và ngày kiểm tra.
- [ ] Ghi phần nhóm mình chấm nhóm khác vào phiếu chấm; ghi phản hồi dành cho nhóm mình vào mục 4 báo cáo nhóm.
- [ ] Cập nhật đóng góp/tự đánh giá, nhờ chạy trên máy khác, phối hợp nhóm trưởng chốt commit nộp và tự nộp LMS.

## Bảng theo dõi bàn giao vào hồ sơ launch

Nguồn cập nhật theo commit `3f69dbf` đã nhận. Các ô trạng thái mô tả bằng chứng hiện có; không thay xác nhận cá nhân hay quyết định nhóm. Số dùng `_simulated` có nhãn simulated và trạng thái Giả lập.

| Mục | Nguồn đã có hoặc cần nhận | Tình trạng | Đầu mối cần xác nhận tiếp |
| --- | --- | --- | --- |
| 1 · Chi phí | A2–A4: CPS toàn mẫu 4.472 đ; phạm vi 4.599 đ gồm cố định (simulated) | Giả lập | Người kiểm số |
| 2 · Độ nhạy | B1–B2: làm lại, xem lại, lương là ba yếu tố mạnh nhất (simulated) | Giả lập | Người kiểm số |
| 3 · So với thủ công | Chi phí hệ thống 5.865 đ/yêu cầu = 0,49 lần mốc 12.000 đ (simulated) | Giả lập | Người kiểm số |
| 4 · Chỉ số | Đã đối chiếu CSV; chờ bàn giao E1 và event nhóm chốt | Chưa | Người phụ trách CP5 |
| 5 · Lỗi | Hai bản đã commit trùng 17/20=85%; khác 9,13,20, chờ xác nhận/thảo luận và năm ca | Chưa | Minh, Nguyễn Minh Quân |
| 6 · Pilot | Người phụ trách CP4 cần bàn giao D1–D2, YAML và lịch | Chưa | Người phụ trách CP4 |
| 7 · Rủi ro | Có số tác động B4/cố định; chờ E2 và ngưỡng/hành động nhóm chốt | Giả lập | Người phụ trách CP5, PM |

### Nhật ký nhận và cập nhật số liệu

Các dòng Codex là kiểm tra bằng công cụ. Minh/người kiểm số thêm dòng xác nhận riêng sau khi thực sự kiểm chứng.

| Ngày/lần nhận | Nội dung | Nguồn | Người/cách xác nhận | Hồ sơ đã cập nhật |
| --- | --- | --- | --- | --- |
| 25/11/2026 · nhận nguồn | CP1–CP2 đã merge | main, 3f69dbf; bang_chi_phi.md | Nguồn Git của nhóm | Mục 1,2,3,7 |
| 25/11/2026 · kiểm tra công cụ | A1 đạt, chi phí và số CSV khớp | kiem_chung_ho_so_Minh.txt; doi_chieu_ho_so_Minh.md | Codex chạy chương trình/đối chiếu | Số liệu tổng hợp và phần chờ E1 |
| 25/11/2026 · đối chiếu nhãn | 17/20=85%; khác ca 9,13,20 | commit 42385e0 và 21ec49a; doi_chieu_nhan_Minh.md | Codex so hai bản; chưa thay xác nhận hai người | Mục 5, báo cáo nhóm |
| Chờ Minh điền | [phép tính/kết quả đã tự kiểm] | [file/bảng, đơn vị, phạm vi] | [tên và cách kiểm thực tế] | [mục đã xác nhận] |

## Điều kiện để chốt hồ sơ

- [ ] Hai bộ nhãn và cách thực hiện được ghi đúng; mức đồng thuận, quy tắc bất đồng và năm ca khắc phục có bằng chứng.
- [ ] CP4 và E1–E2 được người phụ trách bàn giao, các trường và luật dừng đầy đủ.
- [ ] Hồ sơ đủ bảy mục, đúng trạng thái/nhãn simulated, một trang khi trình bày, có đề xuất nhóm chốt.
- [ ] Báo cáo nhóm tối đa hai trang; phản hồi hội đồng và đóng góp cá nhân dựa trên việc thực tế.
- [ ] Nhóm chốt bản nộp trên GitHub; từng thành viên tự nộp LMS trước 23:59 GMT+7 ngày lab, trừ khi coach gia hạn.
