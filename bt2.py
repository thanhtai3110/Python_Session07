# (1) Phân tích lỗi
# Vì sao transaction.strip() không làm thay đổi chuỗi ban đầu?
# Trong Python, chuỗi (string) là kiểu dữ liệu immutable (không thể thay đổi). Các phương thức như .strip(), .upper() không sửa trực tiếp trên biến cũ mà tạo ra một bản sao mới đã được xử lý. Nếu bạn gọi transaction.strip() mà không có lệnh gán transaction = ..., kết quả xử lý sẽ bị mất ngay sau khi dòng lệnh thực thi xong.

# Chuỗi giao dịch thực tế được phân tách bằng ký tự nào?
# Dựa vào ví dụ, ký tự phân tách thực tế là dấu gạch đứng |.

# Vì sao transaction.split("-") là sai?
# Vì chuỗi của bạn không chứa bất kỳ dấu gạch ngang nào. Khi split("-") được gọi, Python không tìm thấy ký tự đó và trả về một danh sách (list) duy nhất chứa toàn bộ chuỗi ban đầu: ['  nguyEN vAn a | PYTHON-01 | 15000000 | paid  '].

# Dữ liệu trong parts bị lệch như thế nào?
# Do split không tách được chuỗi, parts[0] sẽ chứa toàn bộ chuỗi, còn parts[1], parts[2],... sẽ gây ra lỗi IndexError: list index out of range khi chương trình cố gắng truy cập chúng.

# Vì sao cần .strip() lại từng phần sau khi split()?
# Mặc dù bạn đã strip() toàn bộ chuỗi, nhưng khi tách bằng dấu |, các khoảng trắng thừa quanh các phần tử (nếu có) vẫn sẽ bị dính lại (ví dụ: " PYTHON-01 "). Việc strip() từng phần đảm bảo dữ liệu sạch sẽ hoàn toàn trước khi đưa vào báo cáo.

# Vì sao cần chuyển amount từ chuỗi sang số trước khi định dạng?
# Các phương thức định dạng số như {:,} chỉ hoạt động với các kiểu dữ liệu số (int hoặc float). Nếu để dạng chuỗi, bạn không thể sử dụng các hàm toán học hoặc định dạng phân cách hàng nghìn.

# (2) Sửa lỗi và tối ưu mã nguồn
# Dưới đây là phiên bản code đã được chuẩn hóa, tuân thủ nguyên tắc xử lý dữ liệu đầu vào:
transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

# 1. Xóa khoảng trắng thừa và gán lại vào biến
transaction = transaction.strip()

# 2. Tách chuỗi theo dấu "|" (lưu ý khoảng trắng xung quanh dấu |)
parts = transaction.split(" | ")

# 3. Trích xuất và chuẩn hóa dữ liệu
student_name = parts[0].title()
course_code = parts[1]
# Chuyển số tiền sang kiểu int để định dạng dấu phẩy
amount = int(parts[2]) 
status = parts[3].upper()

# 4. Hiển thị kết quả
print("Học viên:", student_name)
print("Khóa học:", course_code)
# Sử dụng f-string với định dạng :, để thêm dấu phẩy phân cách hàng nghìn
print(f"Số tiền: {amount:,} VND")
print("Trạng thái:", status)