# Hồ sơ launch v0 Trợ lý hoàn phí LogiX-VN Gate 2a

Nhóm: [nhóm điền] · Lớp: L3B · Giữ hồ sơ: Nguyễn Nhật Minh · 2A202603745.

Nguồn: [bảng chi phí](bang_chi_phi.md), [bảng lỗi](bang_loi.md) và [kế hoạch pilot](pilot_plan.yaml), CP4 tại commit `f1104de`. Phạm vi pilot: `noi_dia + hang_nang`.

| Mục | Con số chính | Trạng thái | Vai trò vận hành phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí | Toàn mẫu 4.472 đ/việc; noi_dia + hang_nang 3.414 đ biến đổi, 4.599 đ gồm cố định ở 45.000 yêu cầu/tháng (simulated) | Giả lập | Chờ nhóm chốt |
| 2 · Độ nhạy | Làm lại +51,8%; xem lại +40,7%; lương +23,1% theo B1 (simulated) | Giả lập | Chờ nhóm chốt |
| 3 · So với thủ công | Chi phí toàn hệ thống 5.865 đ/yêu cầu = 0,49 lần mốc 12.000 đ, gồm 222 ca nhân viên xử lý; chưa gồm cố định (simulated) | Giả lập | Chờ nhóm chốt |
| 4 · Chỉ số | Chờ E1, event và định nghĩa đo lường từ người phụ trách CP5 | Chưa | Chờ nhóm chốt |
| 5 · Lỗi và khắc phục | Hai bộ nhãn, 17/20=85%, chốt ca 9,13,20; đủ 5 ca khắc phục 6,7,16,11,5, có phát hiện đo được và vai trò | Xong, có bằng chứng | Vai trò theo bảng lỗi |
| 6 · Pilot | Chia ngẫu nhiên theo nhân viên 20 + 20, MDE +6 điểm, 859 yêu cầu hiệu dụng/nhóm; ≥299 yêu cầu/NV, DE=6,96; rollout 10%→25%→50%; 3 luật dừng, rollback ≤30 phút; ngày quyết định 2027-01-05 | Chưa | Giám đốc vận hành LogiX-VN, theo YAML |
| 7 · Rủi ro | B4 có CPS 11.743–12.415 đ khi xem lại 100%; cố định/việc tăng 1.185 lên 2.370 đ khi khối lượng giảm nửa (simulated); chờ E2 chốt hành động | Chưa | Chờ nhóm chốt |

CP4: YAML đọc được, không còn dấu hỏi ngoài chú thích; `20×299/6,96 ≈ 859,20` yêu cầu hiệu dụng/nhóm. Kế hoạch dùng MDE +6 điểm vì trần 1.000 không đủ 1.251 cho +5 điểm. Còn cần xác nhận luật hoàn trùng: chú thích yêu cầu 0 ca nhưng luật dừng ghi “3 ngày liên tiếp”.

Nhóm cần xác nhận ngày 2027-01-05, điều kiện của đề xuất và các vai trò vận hành còn thiếu.

**Đề xuất:** Chưa chốt — chờ xác nhận CP4, bàn giao E1–E2 và quyết định Go / Go có điều kiện / No-go của nhóm.
