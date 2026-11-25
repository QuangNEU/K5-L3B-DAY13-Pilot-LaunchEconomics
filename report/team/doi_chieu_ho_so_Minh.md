# Phiếu đối chiếu số liệu của người giữ hồ sơ

Người giữ hồ sơ: Nguyễn Nhật Minh · 2A202603745. Nguồn đã nhận: CP1–CP2 trên `main`, commit `3f69dbfa4377702edf36decfeec30ab552d33f96`. Các bảng nguồn [A–B](bang_chi_phi.md) được giữ nguyên. [Log kiểm chứng](kiem_chung_ho_so_Minh.txt) ghi lần chạy lại bằng công cụ; Minh cần ghi phần tự kiểm riêng trong báo cáo cá nhân.

## Kết quả đã đối chiếu

| Nội dung | Kết quả và cách kiểm | Mục hồ sơ |
| --- | --- | --- |
| A1 | 1,20; 1,25; 1,25, ba phép thử đạt | Nguồn tính |
| CPS toàn mẫu | 4.373.585,132 / 978 = 4.471,9684 đ/việc (simulated) | 1 |
| Chi phí phạm vi | noi_dia + hang_nang: 3.414 đ biến đổi/việc; 4.599 đ gồm cố định ở 45.000 yêu cầu/tháng (simulated) | 1 |
| So sánh thủ công | (4.373.585,132 + 222 × 12.000) / 1.200 = 5.864,6543 đ/yêu cầu, bằng 0,49 lần mốc 12.000 đ (simulated); chưa cộng cố định | 3 |
| Độ nhạy | Làm lại +51,8%; xem lại +40,7%; lương +23,1% khi đổi theo B1 (simulated) | 2 |
| Giới hạn lần chạy | 2 lần có tổng hệ thống 6.901.220 đ thấp nhất; 1 lần có CPS 4.111 đ thấp nhất (simulated) | 3 |
| Rủi ro xem lại 100% | B4: 11.743 đ với 9 phút làm lại; 12.415 đ với trung bình khoảng 15,3 phút (simulated) | 7 |
| Rủi ro giảm khối lượng | Cố định/việc tăng từ 1.185 lên 2.370 đ khi khối lượng giảm nửa (simulated) | 7 |

## Đối chiếu chuẩn bị nhận E1

Các số dưới đây đọc trực tiếp từ CSV để người giữ hồ sơ kiểm tra mẫu số, chưa thay cho việc bàn giao E1 và danh sách event của người phụ trách CP5.

| Chỉ số | Tử số và mẫu số | Kết quả |
| --- | --- | ---: |
| Chính | 994 yêu cầu có dong_trong_24h=1 và mo_lai_trong_7_ngay=0 / 1200 yêu cầu | 82,83% |
| Bỏ qua gợi ý | 48 quyết định sua/bo / 177 yêu cầu duoc_xem_lai=1 | 27,12% |
| Mở lại | 51 yêu cầu mo_lai_trong_7_ngay=1 / 1200 yêu cầu | 4,25% |

Chỉ số quan sát chưa chứng minh tác động vì đợt chạy thử không có đối chứng. Các phép đếm E1 không dùng cột phút `_simulated`.

## Việc Minh xác nhận

- [ ] Tự tính một phép chia trên, đối chiếu nguồn và ghi cách làm vào mục 4 báo cáo cá nhân.
- [ ] Nhận xác nhận của người kiểm số: tên, thời điểm, bảng và số đã chốt; thêm vào nhật ký bàn giao.
- [ ] Khi CP4/E1–E2 được người phụ trách bàn giao, cập nhật hồ sơ từ đúng bản nhóm chốt.
