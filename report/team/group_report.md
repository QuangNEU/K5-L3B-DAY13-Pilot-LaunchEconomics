# Báo cáo nhóm

Người tổng hợp: Nguyễn Nhật Minh · 2A202603745.

## 1. Thông tin nhóm

- Repo nhóm: `K5-L3B-DAY13-Pilot-LaunchEconomics`.
- Tên nhóm theo tên repo: Pilot.
- Lớp: L3B.
- Thành viên và đóng góp: [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Nhóm tính chi phí từ trace, phân loại lỗi và lập kế hoạch pilot để đề xuất quyết định tại Gate 2a. Minh tổng hợp kết quả được bàn giao, đối chiếu nguồn và cập nhật hồ sơ.

## 3. Kết quả đã nhận

- **CP1 — Nguyễn Như Duy An:** mô hình A1–A4. CPS toàn mẫu 4.472 đ/việc; toàn hệ thống 5.865 đ/yêu cầu, bằng 0,49 lần mốc thủ công (simulated).
- **CP2 — Nguyễn Minh Quang:** độ nhạy và kiểm số. Làm lại tăng gấp đôi làm CPS tăng 51,8%; xem lại 100% có CPS 11.743–12.415 đ theo thời gian làm lại (simulated).
- **CP3 — Quân và Minh:** đủ hai bộ nhãn, đồng thuận 85%, chốt ca 9,13,20. Quân hoàn thiện 5 ca khắc phục 6,7,16,11,5; người giữ hồ sơ đã nhận và cập nhật.
- **CP4:** nhóm đã báo chốt theo xác nhận của Minh. Bản trên main vẫn là `f1104de` của Nguyễn Như Duy An: chia theo nhân viên 20 + 20, MDE +6 điểm, 859 yêu cầu hiệu dụng/nhóm; tối thiểu 299 yêu cầu/nhân viên, DE=6,96; rollout 10%→25%→50%, ngày quyết định 2027-01-05. YAML đọc được, đủ ba luật dừng; điểm diễn đạt luật hoàn trùng còn được ghi để làm rõ trước khi mở pilot.
- **CP5:** Minh đã đối chiếu ba chỉ số từ CSV và điền đủ bảy mục hồ sơ: chỉ số chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200). Mục 7 có hai rủi ro và hướng xử lý từ bảng B. `chi_so.md` vẫn thiếu đặc tả E1–E2 đầy đủ.

Nguồn chi tiết: [chi phí](bang_chi_phi.md), [bảng lỗi](bang_loi.md), [pilot](pilot_plan.yaml), [chỉ số](chi_so.md).

## 4. Đề xuất và duyệt chéo

- Đề xuất trong hồ sơ: **No-go**, chưa mở pilot vì thiếu đặc tả đo lường và luật hoàn trùng chưa nhất quán. Đây là đề xuất trình Gate 2a, chưa có kết quả duyệt của hội đồng.
- Kết luận nhóm đã thống nhất:
- Việc để quay lại Gate 2a: PM hoàn thiện E1–E2; Kỹ sư trưởng agent kiểm chứng chống trùng, đối soát và sửa luật dừng; Giám đốc vận hành xác nhận MDE +6 điểm và lịch đủ mẫu, theo dõi 7 ngày. Ngày quyết định trong kế hoạch là 2027-01-05.
- Hội đồng chấm nhóm mình:
- Điểm và quyết định của hội đồng:
- Lý do, nhận xét:
- Câu hỏi và câu trả lời thực tế:
- Việc cần sửa sau duyệt:

[Phiếu chấm](phieu_cham.md) lưu phần nhóm mình chấm nhóm khác. Phản hồi dành cho nhóm mình ghi tại mục này.

Các dòng trống được điền sau khi nhận kết luận của nhóm và phản hồi hội đồng.

### Nội dung chuẩn bị giải trình

Các ý dưới đây được chuẩn bị từ hồ sơ, chưa phải hỏi–đáp đã diễn ra tại hội đồng.

- **Chi phí nào dùng để so với thủ công?** Dùng chi phí cả hệ thống 5.865 đ/yêu cầu (simulated), đã cộng 222 ca xử lý thủ công, chưa gồm cố định. CPS 4.472 đ chỉ chia cho 978 việc thành công nên có mẫu số khác.
- **Vì sao chọn MDE +6 điểm?** Với 20 cụm/nhóm và ICC=0,02, cỡ mẫu hiệu dụng luôn dưới 1.000, không đủ 1.251 cho +5 điểm. Với +6 điểm, 20×299/6,96≈859,20 đáp ứng mức 859; nếu tác động thật +5 điểm, power chỉ khoảng 0,64.
- **Vì sao đề xuất No-go dù chi phí có vẻ thấp?** Xem lại 100% có thể đưa CPS lên 12.415 đ/việc (simulated), vượt mốc 12.000 đ. Đặc tả E1–E2 còn thiếu; luật hoàn trùng cần làm rõ trước khi mở pilot.

## 5. Khó khăn và cách xử lý

Đã tổng hợp thông tin bốn thành viên trong TEAM.md từ báo cáo cá nhân; tài khoản GitHub của ba thành viên và người chủ trì đặc tả CP5 chưa được ghi rõ. Minh xác nhận nhóm đã chốt CP4; bản mới nhất vẫn là `f1104de`. Ghi chú trước khi mở pilot: chú thích yêu cầu 0 ca hoàn trùng nhưng luật dừng ghi “3 ngày liên tiếp”. Ba chỉ số nền đã được đối chiếu trực tiếp từ CSV; đặc tả event và E1–E2 trong `chi_so.md` vẫn cần người phụ trách hoàn thiện.

Kiểm tra trên máy Minh: `python lab13.py` ban đầu thiếu `statsmodels`; cài trong repo gặp lỗi đường dẫn OneDrive dài. Đã dùng môi trường riêng tại `%TEMP%\lab13-minh-venv`, cài `src/requirements.txt` và chạy Python với `-X utf8` từ `src/`: kết thúc không lỗi, ba phép thử A1 ĐẠT, A–B và D1 khớp số trong hồ sơ.

## 6. Tổng hợp đóng góp

Minh phụ trách nhãn người 2, nhận kết quả của các thành viên và cập nhật hồ sơ. Đóng góp chi tiết ghi trong TEAM.md và báo cáo cá nhân từng người.

## 7. Hạn chế và hướng cải thiện

Chi phí thời gian dùng giả lập; xem lại 100% có thể làm CPS lên 12.415 đ/việc (simulated), vượt mốc thủ công. Kế hoạch CP4 dùng MDE +6 điểm; nếu tác động thật chỉ +5 điểm, power khoảng 0,64. Hồ sơ đề xuất No-go cho đến khi có bằng chứng về đo lường và an toàn.

## 8. Tài liệu tham khảo

[Quy tắc](../../RULES.md), [checkpoint](../../CHECKPOINTS.md), [rubric](../../RUBRIC.md), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md).
