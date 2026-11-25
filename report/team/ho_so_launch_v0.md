# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Repo: `K5-L3B-DAY13-Pilot-LaunchEconomics` · Lớp: L3B · Giữ hồ sơ: Nguyễn Nhật Minh — 2A202603745.

Nguồn: [chi phí A–B](bang_chi_phi.md), [lỗi C](bang_loi.md), [pilot D](pilot_plan.yaml), [CSV yêu cầu](../../src/logix_requests.csv). Dữ liệu của lab là giả lập; số dùng phút giả lập ghi `simulated`. Vai trò vận hành dưới đây là phân công đề xuất cho pilot.

| Mục | Con số chính và cách xử lý | Trạng thái | Vai trò phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu 4.472 đ/việc. Phạm vi noi_dia + hang_nang: 3.414 đ biến đổi, 4.599 đ gồm cố định ở 45.000 yêu cầu/tháng (simulated). | Giả lập | Kế toán trưởng |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi: +51,8%; xem lại gấp đôi: +40,7%; lương tăng 25%: +23,1% (simulated). Ưu tiên đo phút làm lại và xem lại. | Giả lập | PM trợ lý hoàn phí |
| 3 · So với thủ công | Toàn hệ thống: (4.373.585 + 222×12.000)/1.200 ≈ 5.865 đ/yêu cầu = 0,49× mốc thủ công 12.000 đ; chưa gồm cố định (simulated). | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, dùng, an toàn | Trong mẫu: đóng 24h và không mở lại 7 ngày = 994/1.200 = 82,83%; sửa hoặc bỏ gợi ý = 48/177 lượt được xem lại = 27,12%; mở lại 7 ngày = 51/1.200 = 4,25%. E1 còn thiếu đặc tả event. | Chưa | Trưởng nhóm CSKH |
| 5 · Lỗi và khắc phục | Hai bộ nhãn đủ 20 ca, đồng thuận 17/20=85%; chốt ca 9: Do người dùng, 13: Giới hạn hệ thống, 20: Hệ thống. Bảng khắc phục đủ năm loại qua ca 6,7,16,11,5. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chỉ noi_dia + hang_nang; chia ngẫu nhiên theo nhân viên 20+20; MDE +6 điểm, 859 yêu cầu hiệu dụng/nhóm, ≥299 yêu cầu/NV, DE=6,96. Rollout 10%→25%→50%; ngày quyết định 2027-01-05. Power ≈0,64 nếu tác động thật +5 điểm. Luật hoàn trùng chưa nhất quán. | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Xem lại 100%: CPS 11.743–12.415 đ/việc (simulated); giữ bước rollout nếu xem lại còn >50% cuối bước 0.25. Khối lượng giảm nửa: CPS gồm cố định tăng 4.599→5.784 đ/việc (simulated); rà hợp đồng cố định trước khi mở rộng. | Giả lập | PM trợ lý hoàn phí |

**Đối chiếu:** chỉ số chính đếm đồng thời `dong_trong_24h=1` và `mo_lai_trong_7_ngay=0`; chỉ số dùng lọc `duoc_xem_lai=1` rồi đếm `sua/bo`; an toàn đếm `mo_lai_trong_7_ngay=1`. Mẫu không có đối chứng, chưa suy ra tác động của trợ lý. Cỡ mẫu hiệu dụng: `20×299/6,96≈859,20`.

**Việc phải làm để quay lại Gate 2a:**

- PM trợ lý hoàn phí hoàn thiện [E1–E2](chi_so.md): chỉ số bổ sung, ít nhất sáu event có `trace_id`, ánh xạ event–chỉ số và hai rủi ro có hành động; Trưởng nhóm CSKH tổ chức đo phút thực tế từ tuần 1.
- Kỹ sư trưởng agent kiểm chứng khóa chống trùng, đối soát sổ cái và sửa luật dừng “3 ngày liên tiếp” để đáp ứng yêu cầu 0 ca hoàn trùng: xử lý ngay khi phát hiện, quyền rollback trong 30 phút.
- Giám đốc vận hành xác nhận MDE +6 điểm, lịch đủ mẫu và theo dõi mở lại 7 ngày, ngày quyết định 2027-01-05; chỉ mở pilot khi hai việc trên có bằng chứng.

**Đề xuất: No-go** — chưa mở pilot; quay lại Gate 2a sau khi hoàn tất đặc tả đo lường và khắc phục điều kiện an toàn nêu trên.
