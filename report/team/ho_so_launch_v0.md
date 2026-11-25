# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: **Pilot** · Lớp: **L3B** · Repo: `K5-L3B-DAY13-Pilot-LaunchEconomics` · Giữ hồ sơ: Nguyễn Nhật Minh (`2A202603745`).

Nguồn: [bang_chi_phi.md](bang_chi_phi.md), [bang_loi.md](bang_loi.md), [pilot_plan.yaml](pilot_plan.yaml), [chi_so.md](chi_so.md), [src/lab13.py](../../src/lab13.py). Toàn bộ dữ liệu là giả lập; mọi số tính từ cột `_simulated` ghi nhãn `simulated`.

| Mục | Con số chính và cách xử lý | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu 4.472 đ/việc (gấp 16,3× hoá đơn token + tool 274,7 đ/yc; giờ NV chiếm 92,5%). Phạm vi `noi_dia` + `hang_nang`: 3.414 đ biến đổi; gồm cố định 40 triệu đ/tháng là 4.599 đ (45.000 yc/tháng) hoặc 5.784 đ (nửa khối lượng) (`simulated`). | Giả lập | Kế toán trưởng |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ×2: +51,8% (6.787 đ); 2. Tỉ lệ xem lại ×2: +40,7% (6.292 đ); 3. Lương NV +25%: +23,1% (5.506 đ) (`simulated`). Giới hạn 2 lần chạy rẻ nhất cả hệ thống (6.901.220 đ, `simulated`). | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống (cộng 222 ca không thành công): 5.865 đ/yêu cầu = 0,49× mốc 12.000 đ (`simulated`). Theo loại: `noi_dia` 0,22×, `hang_nang` 0,69× (đưa vào pilot); loại `quoc_te` 1,88× (ok tụt 30,0%→11,4%→2,2%) và `doi_tac` 0,85× (`simulated`). | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, dùng, an toàn | Đợt chạy thử (chưa có đối chứng): đóng 24h & không mở lại 7 ngày = 82,83% (994/1.200); bỏ qua gợi ý = 27,12% (48/177); mở lại 7 ngày = 4,25% (51/1.200). Đã đặc tả thêm 2 chỉ số (tiếp nhận công cụ, kiểm toán hoàn sai tiền) và 10 event có `trace_id` ánh xạ đầy đủ trong `chi_so.md`. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập 20 ca, đồng thuận 17/20 = 85%, chốt ca 9 (Do người dùng), 13 (Giới hạn hệ thống), 20 (Hệ thống). Đủ 5 ca khắc phục đại diện 5 loại (ca 6, 7, 16, 11, 5) có ngưỡng đo và vai trò phụ trách. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Phạm vi `noi_dia` + `hang_nang` (12 depot); chia ngẫu nhiên theo nhân viên 20+20 (phân tầng depot); MDE +6 điểm (`n=859`/nhóm, `m≥299` yc/NV, `DE=6,96`; đánh đổi: power ≈ 0,64 nếu tác động thật +5 điểm). Rollout 10%→25%→50%; 4 luật dừng đủ 4 vế (tách riêng 0 ca hoàn trùng tắt trong 30 phút); quyết định `2027-01-05`. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Xem lại 100% ở `noi_dia` + `hang_nang` đẩy CPS lên 11.743 đ (0,98×, 9 phút làm lại) đến 12.415 đ (1,03×, 15,3 phút thực tế — đắt hơn thủ công 12.000 đ; hoà vốn xem lại ≤ 4,8–5,1 phút/ca, `simulated`). Làm lại ×2 (+51,8%) và khối lượng giảm nửa (+2.370 đ cố định/việc, `simulated`) đã gắn ngưỡng dừng và hành động trong `chi_so.md`. | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: No-go** — Chưa mở pilot ở thời điểm hiện tại do 4 rủi ro cốt lõi bằng số chưa có bằng chứng kiểm soát trên hệ thống thực (92,5% chi phí đang là `simulated`; xem lại 100% có thể đắt hơn thủ công ở mức 12.415 đ = 1,03×; lỗi hoàn trùng/đối soát sổ cái ca 7 & 20 chưa kiểm chứng sửa; và đánh đổi power 0,64 ở mức +5 điểm chưa được phê duyệt). **Việc phải làm để quay lại Gate 2a:**

- **Kỹ sư trưởng agent:** hoàn tất khoá chống trùng (`idempotency_key`), đối soát sổ cái (`refund_ledger_write`) trước khi báo "đã hoàn" (ca 7, 20) và bật thực tế đủ 10 event có `trace_id` theo [chi_so.md](chi_so.md).
- **Trưởng nhóm CSKH:** xác nhận cơ chế đo `phut_xem_lai` và `phut_lam_lai` thật từ tuần 1 (thay dữ liệu `simulated`) và ban hành lộ trình giảm xem lại theo bậc dưới ngưỡng hoà vốn ≤ 4,8–5,1 phút/ca (tránh bẫy xem lại 100% ở B4).
- **Kế toán trưởng:** vận hành quy trình kiểm tra mẫu 100 đơn/tuần (`audit_sample_checked`, ngưỡng lệch 1%) để phát hiện sớm lỗi ngầm sai tiền hoàn (ca 5, 17).
- **Giám đốc vận hành LogiX-VN:** ký phê duyệt đánh đổi MDE +6 điểm (power ≈ 0,64 ở mức +5 điểm), kế hoạch thu đủ ≥ 299 yêu cầu/nhân viên và ngày quyết định `2027-01-05` trong [pilot_plan.yaml](pilot_plan.yaml).
