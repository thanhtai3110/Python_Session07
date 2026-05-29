# 1. Phân tích lỗi
# Nguyên nhân cốt lõi của tất cả các vấn đề bạn nêu ra nằm ở tính chất bất biến (immutable) của kiểu dữ liệu chuỗi (string) trong Python.

# Vì sao strip(), title(), upper(), lower() không làm thay đổi trực tiếp biến?
# Trong Python, chuỗi là kiểu dữ liệu không thể thay đổi sau khi đã được tạo ra. Khi bạn gọi student_name.strip(), Python không sửa nội dung của student_name mà nó tạo ra một chuỗi mới đã được loại bỏ khoảng trắng rồi trả về kết quả đó. Vì bạn không gán kết quả đó cho bất kỳ biến nào, chuỗi mới này sẽ bị bỏ đi ngay lập tức.

# Kết quả hiển thị vẫn như cũ: Do bạn chỉ gọi phương thức (như student_name.title()) mà không cập nhật lại giá trị cho biến gốc (ví dụ: student_name = student_name.title()), nên biến student_name vẫn lưu trữ giá trị thô ban đầu.

# Muốn các phương thức có hiệu lực, cần làm gì?
# Bạn cần phải gán lại giá trị trả về của các phương thức xử lý chuỗi đó cho biến cũ hoặc cho một biến mới.

# 2. Sửa lỗi (Source Code chuẩn hóa)
# Để đạt được kết quả chính xác, chúng ta cần gán lại giá trị sau khi xử lý. Bạn có thể thực hiện theo cách dưới đây:


# Dữ liệu đầu vào
student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

# Thực hiện chuẩn hóa bằng cách gán lại kết quả vào chính biến đó
# Lưu ý: Có thể kết hợp phương thức (method chaining) để xử lý gọn hơn
student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

# In kết quả kiểm tra
print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)