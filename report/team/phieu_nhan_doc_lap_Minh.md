# Phiếu nhãn người 2 và xác nhận của Nguyễn Nhật Minh

MSSV: **2A202603745**. Nguồn tình huống: [đề bài gốc](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), bảng Hai mươi ca lỗi. Nội dung 20 tình huống được trích nguyên văn; nhãn và lý do là bản gợi ý do Codex điền theo yêu cầu, chờ Minh kiểm tra và chốt. Các ô xác nhận và thời điểm chốt chưa được cập nhật bởi Codex.

Nhãn gợi ý của người 2 đã được đẩy vào [bảng chung](bang_loi.md) ở commit `21ec49a`. Minh đọc và xác nhận từng ca, giữ rõ hỗ trợ của Codex; ghi thời điểm thực tế khi chốt, chưa ghi thay một lần gắn nhãn độc lập chưa diễn ra.

- Thời điểm bắt đầu: Chưa ghi nhận.
- Thời điểm chốt đủ 20 nhãn: Chưa ghi nhận.
- Người gắn nhãn: Nguyễn Nhật Minh.

Nhãn dùng một trong năm tên: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn theo nguyên nhân gốc. Tick từng ca sau khi Minh đã tự đọc và xác nhận nhãn cùng lý do. Dấu tick ca 1 do Minh đánh trước đó được giữ lại; các ca khác chờ xác nhận.

## Ca 1

Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi.

- [x] Minh đã rà và xác nhận ca 1.
- **Nhãn của Minh:** Do người dùng
- **Lý do theo nguyên nhân gốc:** Khách nhập thiếu hai chữ số tài khoản; đầu vào sai khiến lệnh hoàn bị ngân hàng từ chối.

## Ca 2

Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày.

- [ ] Minh đã rà và xác nhận ca 2.
- **Nhãn của Minh:** Hệ thống
- **Lý do theo nguyên nhân gốc:** Trợ lý chọn sai tham số hàng thường cho kiện hàng nặng 28 kg, gây hoàn thiếu và khách đã phát hiện.

## Ca 3

Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo “chưa được hoàn”.

- [ ] Minh đã rà và xác nhận ca 3.
- **Nhãn của Minh:** Ngữ cảnh
- **Lý do theo nguyên nhân gốc:** Hoàn về ví đúng thiết kế nhưng không khớp kỳ vọng nhận tiền qua ngân hàng của khách.

## Ca 4

Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên.

- [ ] Minh đã rà và xác nhận ca 4.
- **Nhãn của Minh:** Giới hạn hệ thống
- **Lý do theo nguyên nhân gốc:** LogiX thiếu dữ liệu chặng do hãng nước ngoài giao nên trợ lý không đủ thông tin để xử lý.

## Ca 5

Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích.

- [ ] Minh đã rà và xác nhận ca 5.
- **Nhãn của Minh:** Ngầm
- **Lý do theo nguyên nhân gốc:** Hoàn thừa do bỏ qua mã giảm giá nhưng cả khách lẫn cảnh báo đều không phát hiện; chỉ lộ qua kiểm tra mẫu.

## Ca 6

Khách chọn mục “Hoàn phí giao trễ” nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn.

- [ ] Minh đã rà và xác nhận ca 6.
- **Nhãn của Minh:** Do người dùng
- **Lý do theo nguyên nhân gốc:** Khách chọn nhầm mục giao trễ cho vấn đề hàng vỡ, khiến yêu cầu đi vào sai luồng xử lý.

## Ca 7

API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách “đã hoàn tiền thành công”.

- [ ] Minh đã rà và xác nhận ca 7.
- **Nhãn của Minh:** Hệ thống
- **Lý do theo nguyên nhân gốc:** Bước ghi sổ cái vẫn lỗi 503 nhưng trợ lý báo thành công, trái với trạng thái thực tế của giao dịch.

## Ca 8

Trợ lý dẫn “Điều 7.2 chính sách hoàn phí” làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng.

- [ ] Minh đã rà và xác nhận ca 8.
- **Nhãn của Minh:** Hệ thống
- **Lý do theo nguyên nhân gốc:** Trợ lý viện dẫn điều khoản không tồn tại trong chính sách hiện hành; số tiền đúng không làm căn cứ sai trở thành đúng.

## Ca 9

Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo “mã không hợp lệ” rồi dừng, không gợi ý gì.

- [ ] Minh đã rà và xác nhận ca 9.
- **Nhãn của Minh:** Do người dùng
- **Lý do theo nguyên nhân gốc:** Khách nhập mã đơn của sàn thay cho mã vận đơn; nguyên nhân gốc là sai loại mã đầu vào.

## Ca 10

Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện “cam kết giao 24 giờ”.

- [ ] Minh đã rà và xác nhận ca 10.
- **Nhãn của Minh:** Ngữ cảnh
- **Lý do theo nguyên nhân gốc:** Từ chối đúng chính sách bất khả kháng nhưng mâu thuẫn với kỳ vọng do ứng dụng vẫn hiển thị cam kết giao 24 giờ.

## Ca 11

Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời “vui lòng nhập bằng chữ”.

- [ ] Minh đã rà và xác nhận ca 11.
- **Nhãn của Minh:** Giới hạn hệ thống
- **Lý do theo nguyên nhân gốc:** Trợ lý không có khả năng xử lý âm thanh nên không thể hiểu yêu cầu qua tin nhắn thoại.

## Ca 12

Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy.

- [ ] Minh đã rà và xác nhận ca 12.
- **Nhãn của Minh:** Ngầm
- **Lý do theo nguyên nhân gốc:** Tool thiếu trường làm phát sinh nhiều lần gọi và tăng chi phí kéo dài, nhưng kết quả vẫn đúng nên không ai nhận ra.

## Ca 13

Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được.

- [ ] Minh đã rà và xác nhận ca 13.
- **Nhãn của Minh:** Giới hạn hệ thống
- **Lý do theo nguyên nhân gốc:** Hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý; trả lời chung chung không giải quyết được giới hạn này.

## Ca 14

Khách bấm nhầm “Xác nhận đã nhận tiền” khi chưa nhận. Yêu cầu bị đóng.

- [ ] Minh đã rà và xác nhận ca 14.
- **Nhãn của Minh:** Do người dùng
- **Lý do theo nguyên nhân gốc:** Khách bấm nhầm xác nhận đã nhận tiền, cung cấp trạng thái sai khiến yêu cầu bị đóng.

## Ca 15

Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi.

- [ ] Minh đã rà và xác nhận ca 15.
- **Nhãn của Minh:** Hệ thống
- **Lý do theo nguyên nhân gốc:** Trợ lý áp dụng sai mức hoàn 100% thay vì 50% cho đơn trễ 26 giờ; lỗi đã được nhân viên phát hiện.

## Ca 16

Theo thiết kế “gửi ngay khi xong”, trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền.

- [ ] Minh đã rà và xác nhận ca 16.
- **Nhãn của Minh:** Ngữ cảnh
- **Lý do theo nguyên nhân gốc:** Gửi ngay khi xong đúng thiết kế nhưng thời điểm 2:14 sáng không phù hợp hoàn cảnh nghỉ ngơi của khách.

## Ca 17

Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại.

- [ ] Minh đã rà và xác nhận ca 17.
- **Nhãn của Minh:** Ngầm
- **Lý do theo nguyên nhân gốc:** Bộ nhớ đệm dùng bảng giá cũ gây lệch tiền lặp lại trên 212 đơn trong 9 ngày mà chưa có ai mở lại để báo lỗi.

## Ca 18

Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi “Đã hoàn 15.000 đ”, không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu.

- [ ] Minh đã rà và xác nhận ca 18.
- **Nhãn của Minh:** Ngữ cảnh
- **Lý do theo nguyên nhân gốc:** Số tiền hoàn đúng nhưng thông báo thiếu cách tính khiến khách không hiểu mức hoàn và cho rằng bị hoàn thiếu.

## Ca 19

Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt.

- [ ] Minh đã rà và xác nhận ca 19.
- **Nhãn của Minh:** Giới hạn hệ thống
- **Lý do theo nguyên nhân gốc:** Đơn từ 14 tháng trước vượt cửa sổ dữ liệu 12 tháng mà trợ lý truy cập được; cần chuyển nhân viên.

## Ca 20

Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng.

- [ ] Minh đã rà và xác nhận ca 20.
- **Nhãn của Minh:** Hệ thống
- **Lý do theo nguyên nhân gốc:** Hệ thống thiếu khoá chống trùng cho lệnh thứ hai nên hoàn tiền hai lần cho cùng đơn khi khách gửi lại yêu cầu.
