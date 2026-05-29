# 1. Phân tích và thiết kế giải pháp
# Phân tích Input/Output
# Input: Một chuỗi thô (raw_data) chứa thông tin các nhân viên, phân cách bởi ký tự | và ;.

# Output: Một chương trình Console hiển thị menu tương tác, thực hiện chuẩn hóa dữ liệu theo quy tắc nghiệp vụ và xuất báo cáo dạng bảng được căn lề.

# Đề xuất giải pháp
# Xử lý chuỗi: Sử dụng các phương thức .split(), .strip(), .upper(), .title(), .replace() để làm sạch dữ liệu.

# Cấu trúc dữ liệu: Lưu trữ danh sách nhân viên đã chuẩn hóa dưới dạng list chứa các dict, giúp việc truy xuất và tìm kiếm theo ID dễ dàng hơn.

# Số điện thoại: Sử dụng .isdigit() để kiểm tra tính hợp lệ sau khi đã loại bỏ dấu -.

# Hiển thị: Sử dụng f-string với căn lề (ví dụ: {:^10}) để tạo bảng báo cáo đẹp mắt.

# Thiết kế thuật toán (Pseudocode)
# Khởi tạo raw_data.

# Viết hàm process_data():

# Tách chuỗi theo | để lấy danh sách nhân viên.

# Với mỗi nhân viên, tách tiếp theo ;.

# Chuẩn hóa từng trường (ID, Tên, SĐT, Phòng ban).

# Lưu vào danh sách processed_list.

# Trong hàm main():

# Hiển thị menu bằng while True.

# Sử dụng cấu trúc if-elif-else để xử lý lựa chọn người dùng.

# Nếu chọn tìm kiếm, chuẩn hóa đầu vào người dùng trước khi so sánh.

# 2. Triển khai Code (Python)

raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

def get_processed_data():
    """Tách và chuẩn hóa dữ liệu từ chuỗi thô."""
    employees = []
    items = raw_data.split('|')
    for item in items:
        fields = [f.strip() for f in item.split(';')]
        if len(fields) == 4:
            emp_id, name, phone, dept = fields
            
            # Chuẩn hóa
            emp_id = emp_id.upper()
            name = name.title()
            dept = dept.upper()
            
            # Xử lý SĐT
            clean_phone = phone.replace('-', '')
            if clean_phone.isdigit():
                formatted_phone = "******" + clean_phone[-4:]
            else:
                formatted_phone = "Invalid Format"
                
            employees.append({
                "id": emp_id,
                "name": name,
                "phone": formatted_phone,
                "dept": dept
            })
    return employees

def show_report(employees):
    """In báo cáo dạng bảng."""
    print(f"\n{'ID':<10} | {'HỌ TÊN':<15} | {'SĐT':<15} | {'PHÒNG BAN':<10}")
    print("-" * 60)
    for emp in employees:
        print(f"{emp['id']:<10} | {emp['name']:<15} | {emp['phone']:<15} | {emp['dept']:<10}")

def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
        print("1. Hiển thị chuỗi dữ liệu gốc")
        print("2. Chuẩn hóa dữ liệu và in báo cáo")
        print("3. Tìm kiếm nhân viên theo mã ID")
        print("4. Thoát chương trình")
        
        choice = input("Nhập lựa chọn (1-4): ")
        
        if choice == '1':
            print(f"\nDữ liệu gốc: {raw_data}")
        elif choice == '2':
            show_report(get_processed_data())
        elif choice == '3':
            search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()
            found = False
            for emp in get_processed_data():
                if emp['id'] == search_id:
                    print(f"Tìm thấy: {emp['name']} - SĐT: {emp['phone']} - Phòng: {emp['dept']}")
                    found = True
                    break
            if not found:
                print("Không tìm thấy nhân viên")
        elif choice == '4':
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

if __name__ == "__main__":
    main()