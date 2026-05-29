# 1. Phân tích và thiết kế giải pháp
# Phân tích Input/Output
# Input:

# Số lượng phiếu đăng ký (số nguyên n).

# Chuỗi ký tự cho mỗi phiếu theo format: Họ tên | Tên khóa học | Mã học viên | Email.

# Output:

# Thông tin đã chuẩn hóa (Họ tên Title Case, Khóa học Title Case, Mã ID Uppercase, Email Lowercase).

# Mã xác nhận (kết hợp Mã ID và Khóa học).

# Thông báo lỗi cụ thể cho các trường hợp dữ liệu không hợp lệ.

# Đề xuất giải pháp
# Tách dữ liệu: Sử dụng phương thức .split('|') để phân tách các trường, kết hợp với .strip() để loại bỏ khoảng trắng thừa.

# Chuẩn hóa:

# Họ tên & Khóa học: Sử dụng .title().

# Mã học viên: Sử dụng .upper().

# Email: Sử dụng .lower().

# Kiểm soát luồng: Sử dụng vòng lặp for theo số lượng phiếu đăng ký, kết hợp cấu trúc if-else và lệnh continue để bỏ qua các phiếu lỗi (Edge cases).

# Thiết kế thuật toán (Pseudocode)
# Nhập số lượng phiếu n.

# Nếu n <= 0, in "Số lượng phiếu đăng ký không hợp lệ" và dừng.

# Lặp lại n lần:
# a. Nhập chuỗi dữ liệu.
# b. Tách chuỗi bằng |. Nếu số phần tử != 4, in lỗi và continue.
# c. Làm sạch dữ liệu (strip).
# d. Kiểm tra Bẫy 3 (Email có chứa @) và Bẫy 4 (Độ dài mã >= 5). Nếu vi phạm, in lỗi và continue.
# e. In thông tin đã chuẩn hóa và mã xác nhận theo yêu cầu.

# 2. Triển khai Code

def process_registration():
    # Nhập số lượng phiếu
    try:
        n = int(input("Nhập số lượng phiếu đăng ký: "))
    except ValueError:
        print("Số lượng phiếu đăng ký không hợp lệ")
        return

    if n <= 0:
        print("Số lượng phiếu đăng ký không hợp lệ")
        return

    for i in range(1, n + 1):
        raw_input = input(f"Nhập dữ liệu phiếu thứ {i}: ")
        parts = [item.strip() for item in raw_input.split('|')]

        # Kiểm tra Bẫy 2: Đủ 4 phần
        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        full_name, course, student_id, email = parts

        # Chuẩn hóa dữ liệu
        full_name = full_name.title()
        course = course.title()
        student_id = student_id.upper()
        email = email.lower()

        # Kiểm tra Bẫy 3: Email chứa @
        if '@' not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        # Kiểm tra Bẫy 4: Mã học viên >= 5 ký tự
        if len(student_id) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        # Tạo mã xác nhận
        confirmation_code = f"{student_id}_{course.upper().replace(' ', '-')}"

        # In kết quả
        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {full_name}")
        print(f"Khóa học: {course}")
        print(f"Mã học viên: {student_id}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {confirmation_code}\n")

# Chạy chương trình
if __name__ == "__main__":
    process_registration()