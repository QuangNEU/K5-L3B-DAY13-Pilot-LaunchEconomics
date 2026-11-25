# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): **Pilot**
- Nhóm được chấm: **G2026**

Nguồn ghi chép: commit `b4eb099` (PR #15) do Quân bàn giao. Đây là kết quả **Pilot chấm G2026**; ngày 15/01/2027 và rollback 15 phút bên dưới thuộc kế hoạch của G2026. Kế hoạch của Pilot tại `pilot_plan.yaml` dùng ngày 05/01/2027 và rollback 30 phút.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp với bằng chứng. Nhóm nêu lợi ích chi phí của `noi_dia` (0,22×) và `hang_nang` (0,69×), đồng thời không bỏ qua các số bất lợi như `quoc_te` (1,88×), power khoảng 0,64 nếu tác động thật chỉ tăng 5 điểm và một số đầu vào vẫn là simulated. Nhóm xử lý bằng cách thu hẹp phạm vi pilot, giữ nhóm đối chứng, áp dụng luật dừng và thay số simulated bằng số đo thật sau tuần 1. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Các số chi phí đều có nhãn `simulated` hoặc trạng thái `Giả lập`. Pilot chỉ gồm `noi_dia` (0,22×) và `hang_nang` (0,69×); loại `quoc_te` (1,88×) và `doi_tac` (0,85×) khỏi phạm vi dựa trên số liệu. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Có nhóm đối chứng đồng thời, chia ngẫu nhiên theo nhân viên và phân tầng theo depot; 20 nhân viên và 859 yêu cầu hiệu dụng mỗi nhóm cho MDE 6 điểm. Luật dừng có ngưỡng, thời hạn và người có quyền dừng; ngày quyết định là 15/01/2027 và thời gian rollback là 15 phút. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Cho phép pilot có điều kiện vì phạm vi `noi_dia` và `hang_nang` có chi phí simulated lần lượt bằng 0,22× và 0,69× mức nhân viên tự làm; kế hoạch có nhóm đối chứng, 20 nhân viên mỗi nhóm và luật dừng cụ thể. Nhóm phải giữ `quoc_te` và `doi_tac` ngoài phạm vi, đồng thời thay số phút simulated bằng số đo thật sau tuần 1 trước khi xem xét mở rộng.

**Một câu hỏi cho đội trình:** Nếu tác động thật chỉ tăng 5 điểm thì nhóm tự tính power còn khoảng 0,64. Tại ngày quyết định 15/01/2027, nhóm sẽ xử lý thế nào nếu kết quả không có ý nghĩa thống kê: kết luận trợ lý không hiệu quả hay kết luận pilot chưa đủ lực thống kê, và ai có quyền quyết định?

**Câu trả lời của đội trình :** Nhóm không kết luận trợ lý không hiệu quả chỉ vì p-value không đạt, vì pilot chỉ có power khoảng 0,64 nếu tác động thật là 5 điểm. Nhóm sẽ xem khoảng tin cậy: nếu khoảng tin cậy vẫn chứa mức cải thiện có ý nghĩa 5–6 điểm thì kết quả được coi là chưa đủ lực thống kê, không mở rộng pilot và phải tăng cỡ mẫu hoặc kéo dài thời gian đo. Nếu cận trên của khoảng tin cậy cũng thấp hơn mức cải thiện tối thiểu đã chốt thì kết luận chưa đạt hiệu quả và No-go. Giám đốc vận hành LogiX-VN là người có quyền quyết định cuối cùng tại ngày 15/01/2027, dựa trên kết quả và ý kiến của PM cùng Giám đốc tài chính.
