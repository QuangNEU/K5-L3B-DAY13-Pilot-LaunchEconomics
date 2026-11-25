# Team

## Thông tin nhóm

- Tên nhóm: Pilot
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Pilot-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/QuangNEU/K5-L3B-DAY13-Pilot-LaunchEconomics · Nhánh nộp: `main` · Commit chốt: cập nhật ở commit cuối trước 23:59 GMT+7
- Nhánh đóng góp của Minh: `NguyenNhatMinh`.

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Như Duy An | 2A202603783 | 26ai.annnd@vinuni.edu.vn | K0heii | Người viết code (CP1, bổ sung code CP2/CP4/CP5) |
|   2 | Nguyễn Minh Quang | 2A202603791 | 26ai.quangnm3@vinuni.edu.vn | QuangNEU | Người kiểm số (CP2) |
|   3 | Nguyễn Minh Quân | 2A202603747 | minhquannm0905@gmail.com | — | Người gắn nhãn 1 (CP3) |
|   4 | Nguyễn Nhật Minh | 2A202603745 | nnhatminh2610@gmail.com | NhMinh-2610 | Người gắn nhãn 2, kiêm giữ hồ sơ (CP3, tổng hợp hồ sơ) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Các thành viên ghi đóng góp chi tiết trong báo cáo cá nhân tương ứng.

## NguyenNhuDuyAn-2A202603783

### Phần việc phụ trách

- Người viết code chính cho `src/lab13.py` (CP1 · Nhiệm vụ A1–A4; bổ sung code CP2 · B1–B4, CP4 · D1 và CP5 · E1).
- Hoàn thiện phần A1–A4 trong `report/team/bang_chi_phi.md`, hoàn thiện `report/team/pilot_plan.yaml` (CP4) và `report/team/chi_so.md` (CP5), đồng bộ hồ sơ chung trước khi nộp.

### Đóng góp cụ thể

- Viết 3 hàm A1 đạt 100% (`1,20 · 1,25 · 1,25`), hàm `mo_hinh(...)` (A2), tách 4 loại yêu cầu + tỉ lệ `ok` theo lần thử (A3) và chi phí cố định 40 triệu đ/tháng (A4); điền phần A1–A4 của `bang_chi_phi.md` có đủ nhãn `simulated`.
- Bổ sung code B1–B4, tính cỡ mẫu D1 + power `statsmodels` (`~0,64`) và 3 chỉ số E1 vào `src/lab13.py`.
- Hoàn thiện `report/team/pilot_plan.yaml` (không còn dấu `?`, đủ D1/D2 và 4 luật dừng chuẩn 4 vế, tách riêng luật 0 ca hoàn trùng), `report/team/chi_so.md` (5 chỉ số, 10 event có `trace_id`, kiểm tra chéo, 3 dòng rủi ro kinh tế) và đồng bộ `ho_so_launch_v0.md`, `group_report.md`, `TEAM.md`.

### Bằng chứng

- [src/lab13.py](src/lab13.py), [report/team/bang_chi_phi.md](report/team/bang_chi_phi.md), [report/team/pilot_plan.yaml](report/team/pilot_plan.yaml), [report/team/chi_so.md](report/team/chi_so.md), [report/team/2A202603783_NguyenNhuDuyAn.md](report/team/2A202603783_NguyenNhuDuyAn.md).
- Commit chính: `6aa5a90` (PR #1 `cp1`), `f1104de` (CP2 & CP4), `8a6ad1c` (CP5 & đồng bộ hồ sơ).

## NguyenMinhQuang-2A202603791

### Phần việc phụ trách

- Người kiểm số; đối chiếu chéo số liệu CP1 (Nhiệm vụ A) và phụ trách phân tích độ nhạy CP2 (Nhiệm vụ B1–B4) trong `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- Kiểm tra độc lập toàn bộ số liệu A1–A4 từ 2 file CSV (`keep_default_na=False`) và xác nhận sai số trong ngưỡng ≤ 2%.
- Tính toán và hoàn thiện phần B1 (9 kịch bản đơn biến), B2 (đổi cặp + xếp hạng 3 yếu tố nhạy nhất), B3 (chi phí cả hệ thống cho giới hạn 1–3 lần chạy, chỉ ra 2 lần rẻ nhất `6.901.220 đ`), và B4 (xem lại 100% ở cả hai mức 9 phút = `11.743 đ` và 15,3 phút = `12.415 đ`, kèm ngưỡng hoà vốn xem lại) trong `report/team/bang_chi_phi.md`.

### Bằng chứng

- [report/team/bang_chi_phi.md](report/team/bang_chi_phi.md) (mục B1–B4), [report/team/2A202603791_NguyenMinhQuang.md](report/team/2A202603791_NguyenMinhQuang.md).
- Commit chính: `5094d57`, `c804a69` (PR #3 `3f69dbf`).

## NguyenMinhQuan-2A202603747

### Phần việc phụ trách

- Người gắn nhãn 1 trong CP3 (Nhiệm vụ C): gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, đối chiếu với Người gắn nhãn 2 và hoàn thiện bảng khắc phục 5 ca đại diện.

### Đóng góp cụ thể

- Hoàn thành và lưu riêng bộ 20 nhãn độc lập trước khi thảo luận để đảm bảo tính truy vết (`docs/labels/2A202603747_NguyenMinhQuan.md`).
- Đối chiếu với Nguyễn Nhật Minh đạt đồng thuận `17/20 = 85%`, thảo luận thống nhất 3 ca khác biệt (`9, 13, 20`) theo nguyên nhân gốc.
- Hoàn thiện bảng khắc phục cho 5 ca đại diện đủ 5 loại lỗi (`6, 7, 16, 11, 5`) với cách phát hiện đo được, biện pháp xử lý và vai trò phụ trách cụ thể trong `report/team/bang_loi.md`.

### Bằng chứng

- [docs/labels/2A202603747_NguyenMinhQuan.md](docs/labels/2A202603747_NguyenMinhQuan.md), [report/team/bang_loi.md](report/team/bang_loi.md), [report/team/2A202603747_NguyenMinhQuan.md](report/team/2A202603747_NguyenMinhQuan.md).
- Commit chính: `42385e0`, `ef75e90` (PR #4 `1c28d12`), `7752d2a` (PR #8 `ea2e38c`), `f7a9d4a`.

## Nguyễn Nhật Minh 2A202603745

### Phần việc phụ trách

Gắn nhãn người 2, đối chiếu CP3 cùng Nguyễn Minh Quân; nhận kết quả đã chốt từ các thành viên để tổng hợp hồ sơ launch, báo cáo và ghi phản hồi duyệt chéo.

### Đóng góp

- [x] Nhãn người 2, đồng thuận 17/20=85%, chốt ca 9,13,20.
- [x] Nhận bảng khắc phục 5 ca 6,7,16,11,5 do Quân hoàn thiện; cập nhật mục 5 hồ sơ.
- [x] Tổng hợp kết quả CP1 của An và CP2 của Quang vào hồ sơ, kèm nguồn và nhãn simulated.
- [x] Nhận bản CP4 tại f1104de, rà YAML/cỡ mẫu hiệu dụng và cập nhật mục 6 hồ sơ; phát hiện điểm cần tách luật hoàn trùng.
- [x] Chạy kiểm chứng độc lập `src/lab13.py` trên máy thứ hai của nhóm (ba phép thử A1 ĐẠT, A–B và D1 khớp hồ sơ).
- [x] Đối chiếu ba chỉ số nền từ CSV; hoàn thiện bảy mục hồ sơ launch, vai trò vận hành đề xuất và kết luận No-go kèm việc cần làm để quay lại Gate 2a.
- [x] Hoàn thiện báo cáo cá nhân và thông tin liên hệ của Minh.
- [x] Nhận bản CP4/CP5 hoàn thiện tại `8a6ad1c`: bốn luật dừng, năm chỉ số, mười event và ba rủi ro kinh tế.
- [x] Tổng hợp thông tin thành viên, giải quyết xung đột và đồng bộ hồ sơ, báo cáo cá nhân với main.
- [x] Cập nhật phiếu Pilot chấm G2026 từ `b4eb099`: 30/30, Go có điều kiện, có câu hỏi và trả lời.
- [x] Đối chiếu xác nhận mọi thành viên đã nộp LMS trong checklist nhóm tại `7e12e19` và `ab4ef82`.
- [ ] Bổ sung phản hồi hội đồng chấm Pilot khi nhận được; hiện repo chưa có biên bản này.

### Bằng chứng

[Bảng lỗi](report/team/bang_loi.md), [hồ sơ launch](report/team/ho_so_launch_v0.md), [báo cáo nhóm](report/team/group_report.md), [báo cáo cá nhân](report/team/2A202603745_NguyenNhatMinh.md) (PR #2, #7, #10, #11, #12).
