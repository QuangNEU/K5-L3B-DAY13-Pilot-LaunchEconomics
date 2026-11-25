# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Số tính thử bằng `src/lab13.py` trên mẫu 1.200 yêu cầu của đợt chạy thử (không có nhóm đối chứng, chưa suy ra tác động của trợ lý).

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu có `duoc_xem_lai == 1` | Chỉ số trong đợt chạy thử là **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (51/1.200) |
| Dùng (nhóm tự đề xuất) | Tỉ lệ tiếp nhận công cụ (% yêu cầu nhóm can thiệp có mở gợi ý trợ lý) | Số yêu cầu có event `agent_suggestion_shown` trong nhóm `arm == 'treatment'`, chia tổng số yêu cầu thuộc phạm vi của nhóm `arm == 'treatment'` | Không cần tính |
| An toàn (nhóm tự đề xuất) | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm ca 5, 17) | Số đơn có `so_tien_da_hoan != so_tien_dung` trong event `audit_sample_checked`, chia tổng số đơn kiểm tra mẫu (100 đơn/tuần) | Không cần tính |

*Lưu ý diễn đạt:* Các con số 82,83%, 27,12% và 4,25% là **chỉ số trong đợt chạy thử**, không kết luận trợ lý đã nâng chỉ số so với baseline 70% vì đợt chạy thử không có nhóm đối chứng song song.

## Danh sách event

Mười event bắt buộc khi triển khai pilot, **mọi event đều mang `trace_id`** để nối xuyên suốt từ yêu cầu khách hàng đến các lần chạy của agent, sổ cái hoàn tiền và kiểm toán.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / cổng CSKH | `request_id`, `depot`, `loai`, `so_tien_vnd`, `arm`, `created_at`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Dịch vụ agent | `run_id`, `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `shown_at`, `trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Giao diện nhân viên | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Hệ thống CSKH | `request_id`, `staff_id`, `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại một ca lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien_da_hoan`, `ket_qua` (`ok`/`loi`), `trace_id` | Khi ghi nhận giao dịch hoàn tiền vào sổ cái |
| `handoff_to_staff` | Dịch vụ agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu sang nhân viên xử lý |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `ket_qua`, `trace_id` | Khi đóng yêu cầu hoàn phí |
| `ticket_reopened` | App khách / CSKH | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu sau khi đóng |
| `audit_sample_checked` | Hệ thống kiểm toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `lech_tien`, `checked_at`, `trace_id` | Hằng tuần khi Kế toán kiểm tra mẫu 100 đơn |

**Kiểm tra chéo (ánh xạ event → chỉ số ở bảng E1):** mọi chỉ số ở bảng E1 đều đo được trực tiếp từ danh sách event trên, nối theo `trace_id`:

- **Chỉ số chính (% đóng trong 24h và không mở lại trong 7 ngày):** `refund_request_created` (`created_at`) + `ticket_closed` (`closed_at - created_at <= 24h`) + kiểm tra không có `ticket_reopened` trong 7 ngày sau `closed_at`.
- **Chỉ số dùng — Tỉ lệ bỏ qua gợi ý:** `staff_review_decision` (đếm `quyet_dinh` là `sua` hoặc `bo` chia tổng số bản ghi `staff_review_decision`).
- **Chỉ số an toàn — Tỉ lệ lỗi lọt đến khách:** `ticket_reopened` (trong vòng 7 ngày kể từ `ticket_closed.closed_at`) chia tổng số `refund_request_created`.
- **Chỉ số dùng tự đề xuất — Tỉ lệ tiếp nhận công cụ:** `agent_suggestion_shown` (`staff_id` thuộc nhóm `treatment`) chia tổng `refund_request_created` (`arm == 'treatment'`).
- **Chỉ số an toàn tự đề xuất — Tỉ lệ đơn hoàn sai tiền (lỗi ngầm):** `audit_sample_checked` (đếm `so_tien_da_hoan != so_tien_dung` chia tổng số bản ghi kiểm tra mẫu trong tuần).
- **Đối soát chi phí & an toàn hoàn trùng bổ sung:** `agent_run_completed` + `staff_review_decision` (`phut_xem_lai` thật) + `staff_rework_completed` (`phut_lam_lai` thật) để thay toàn bộ số `simulated`; `refund_ledger_write` (`idempotency_key`, `ket_qua`) để phát hiện ngay ca hoàn trùng (0 ca) hoặc báo sai trạng thái (ca 7, 20).

## E2 · Rủi ro kinh tế

Số liệu lấy trực tiếp từ bảng độ nhạy và chi phí cố định trong [bang_chi_phi.md](bang_chi_phi.md); mọi con số dùng cột `_simulated` đều gắn nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy nhất, hạng 1) | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ/việc** (`simulated`) | Tỉ lệ ca `lam_lai` theo tuần vượt **7%** (mẫu chạy thử trong phạm vi `noi_dia + hang_nang` là `48/982 = 4,9%`) hoặc CPS đo thật > 8.000 đ trong 2 tuần liên tiếp | Thu hẹp phạm vi về chỉ `noi_dia`, giới hạn tối đa 2 lần chạy và rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài ở phạm vi pilot (`noi_dia` + `hang_nang`) | CPS tăng lên **11.743 đ = 0,98×** (với 9 phút làm lại) hoặc **12.415 đ = 1,03×** (với 15,3 phút làm lại thực tế trong dữ liệu), đắt hơn nhân viên tự làm (`12.000 đ`, `simulated`) | Tỉ lệ yêu cầu được xem lại vẫn **> 50%** vào cuối bước rollout `0.25`, hoặc thời gian xem lại trung bình vượt ngưỡng hoà vốn (**> 4,8–5,1 phút/ca**) | Xây dựng lộ trình giảm xem lại theo bậc khi tỉ lệ `sua + bo < 15%` và cải thiện giao diện để rút thời gian xem lại dưới 5 phút; giữ bước rollout nếu chưa đạt | Trưởng nhóm CSKH |
| Khối lượng thực tế thấp hơn dự kiến làm đội chi phí cố định | Chi phí cố định 40 triệu đ/tháng tăng từ **+1.185 đ/việc** (45.000 yc/tháng → CPS 4.599 đ = 0,38×) lên **+2.370 đ/việc** khi khối lượng còn một nửa (→ CPS **5.784 đ = 0,48×**, `simulated`) | Số việc thành công mỗi tuần thấp hơn **50%** kế hoạch hoặc số yêu cầu/NV không kịp đạt ngưỡng `m >= 299` trước `decision_date` | Tạm dừng kế hoạch mở rộng pilot, rà soát lại hợp đồng chi phí cố định hạ tầng/vận hành với nhà cung cấp trước khi quyết định bước tiếp theo | PM trợ lý hoàn phí |
