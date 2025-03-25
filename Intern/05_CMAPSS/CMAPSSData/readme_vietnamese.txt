Tập dữ liệu: FD001
Quỹ đạo tàu: 100
Quỹ đạo thử nghiệm: 100
Điều kiện: MỘT (Mực nước biển)
Chế độ lỗi: MỘT (Suy thoái HPC)

Tập dữ liệu: FD002
Quỹ đạo tàu: 260
Quỹ đạo thử nghiệm: 259
Điều kiện: SIX
Chế độ lỗi: MỘT (Suy thoái HPC)

Tập dữ liệu: FD003
Quỹ đạo tàu: 100
Quỹ đạo thử nghiệm: 100
Điều kiện: MỘT (Mực nước biển)
Chế độ lỗi: HAI (Suy thoái HPC, Suy thoái quạt)

Tập dữ liệu: FD004
Quỹ đạo tàu: 248
Quỹ đạo thử nghiệm: 249
Điều kiện: SIX
Chế độ lỗi: HAI (Suy thoái HPC, Suy thoái quạt)



Kịch bản thử nghiệm

Bộ dữ liệu bao gồm nhiều chuỗi thời gian đa biến. Mỗi tập dữ liệu được chia thành các tập con huấn luyện và kiểm tra. Mỗi chuỗi thời gian là từ một công cụ khác nhau - tức là dữ liệu có thể được coi là từ một nhóm động cơ cùng loại. Mỗi động cơ khởi động với mức độ hao mòn ban đầu và biến thể sản xuất khác nhau mà người dùng không xác định được. Sự hao mòn và biến đổi này được coi là bình thường, tức là nó không được coi là tình trạng lỗi. Có ba cài đặt vận hành có ảnh hưởng đáng kể đến hiệu suất động cơ. Các cài đặt này cũng được bao gồm trong dữ liệu. Dữ liệu bị nhiễm nhiễu cảm biến.

Động cơ hoạt động bình thường khi bắt đầu mỗi chuỗi thời gian và phát sinh lỗi tại một số điểm trong chuỗi. Trong tập huấn luyện, lỗi sẽ tăng dần về mức độ cho đến khi hệ thống bị lỗi. Trong tập kiểm tra, chuỗi thời gian kết thúc một thời gian trước khi hệ thống bị lỗi. Mục tiêu của cuộc thi là dự đoán số chu kỳ vận hành còn lại trước khi hỏng hóc trong bộ thử nghiệm, tức là số chu kỳ vận hành sau chu kỳ cuối cùng mà động cơ sẽ tiếp tục hoạt động. Đồng thời cung cấp vectơ giá trị Thời hạn sử dụng còn lại (RUL) thực cho dữ liệu thử nghiệm.

Dữ liệu được cung cấp dưới dạng tệp văn bản nén zip với 26 cột số, cách nhau bằng dấu cách. Mỗi hàng là một ảnh chụp nhanh dữ liệu được lấy trong một chu kỳ hoạt động, mỗi cột là một biến khác nhau. Các cột tương ứng với:
1) số đơn vị
2) thời gian, theo chu kỳ
3) cài đặt vận hành 1
4) cài đặt vận hành 2
5) cài đặt vận hành 3
6) đo cảm biến 1
7) đo cảm biến 2
...
26) đo cảm biến 26


Tài liệu tham khảo: A. Saxena, K. Goebel, D. Simon và N. Eklund, “Mô hình lan truyền thiệt hại cho mô phỏng hoạt động đến thất bại của động cơ máy bay”, trong Kỷ yếu của Hội nghị quốc tế lần thứ nhất về Tiên lượng và Quản lý sức khỏe (PHM08) , Denver CO, tháng 10 năm 2008.