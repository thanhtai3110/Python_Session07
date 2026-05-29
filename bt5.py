# 1. Phân tích và thiết kế giải pháp
# Phân tích Input/Output
# Input: Chuỗi raw_batch (string) chứa các mã sản phẩm ngăn cách bởi dấu ;. Các lựa chọn menu từ người dùng (input từ console).

# Output: * Báo cáo kiểm kê dạng bảng căn lề.

# Kết quả tra cứu theo Serial.

# Thông báo lỗi/thông báo hệ thống.

# Đề xuất giải pháp
# Cấu trúc dữ liệu: Sử dụng một danh sách các dictionary [{"id": "...", "type": "...", "country": "...", "year": "...", "serial": "...", "status": "..."}] để dễ dàng quản lý và truy xuất.

# Xử lý chuỗi: Sử dụng .split(';'), .strip(), .upper().

# Kiểm tra Serial: Sử dụng phương thức .isdigit() để kiểm tra xem chuỗi serial có hoàn toàn là chữ số hay không.

# Menu: Sử dụng vòng lặp while True kết hợp với if-elif-else để quản lý các chức năng.

# Thiết kế thuật toán (Pseudocode)
# Khai báo raw_batch.

# Tạo hàm process_batch() để tách chuỗi, làm sạch và lưu vào danh sách.

# Trong hàm main():

# Hiển thị menu.

# Nhập lựa chọn.

# Nếu chọn 2: Duyệt danh sách, in bảng, đếm số sản phẩm "Pass".

# Nếu chọn 3: Nhập search_key, lặp qua danh sách, nếu serial[-2:] == search_key, in thông tin.

# 2. Triển khai Code

raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

def get_processed_data():
    """Tách và chuẩn hóa dữ liệu từ chuỗi thô."""
    products = []
    # Tách theo ; và loại bỏ khoảng trắng thừa
    raw_list = [item.strip() for item in raw_batch.split(';') if item.strip()]
    
    for item in raw_list:
        parts = item.upper().split('-')
        if len(parts) == 4:
            sp_type, country, year, serial = parts
            full_year = "20" + year
            
            # Kiểm tra Bẫy 1: Serial có là số không?
            if serial.isdigit():
                status = "Pass"
            else:
                status = "Lỗi Serial - Reject"
                
            products.append({
                "sp_type": sp_type,
                "country": country,
                "year": full_year,
                "serial": serial,
                "status": status
            })
    return products

def main():
    while True:
        print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
        print("1. Hiển thị chuỗi mã vạch gốc")
        print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
        print("3. Tra cứu nhanh theo đuôi Serial")
        print("4. Thoát chương trình")
        
        choice = input("Nhập lựa chọn của bạn (1-4): ")
        
        if choice == '1':
            print(f"\nDữ liệu gốc: {raw_batch}")
            
        elif choice == '2':
            products = get_processed_data()
            print(f"\n{'MÃ SP':<10} | {'XUẤT XỨ':<8} | {'NĂM SX':<8} | {'SERIAL':<10} | {'TRẠNG THÁI'}")
            print("-" * 65)
            
            count_pass = 0
            for p in products:
                print(f"{p['sp_type']:<10} | {p['country']:<8} | {p['year']:<8} | {p['serial']:<10} | {p['status']}")
                if p['status'] == "Pass":
                    count_pass += 1
            
            print(f"\nĐã giải mã thành công {count_pass} sản phẩm hợp lệ / Tổng số {len(products)} sản phẩm.")
            
        elif choice == '3':
            search_key = input("Nhập 2 số cuối của Serial cần tìm: ").strip()
            products = get_processed_data()
            found = False
            for p in products:
                # So sánh 2 ký tự cuối
                if p['serial'][-2:] == search_key:
                    print(f"Tìm thấy: {p['sp_type']}-{p['country']}-{p['year']}-{p['serial']} (Status: {p['status']})")
                    found = True
            if not found:
                print("Không tìm thấy sản phẩm phù hợp")
                
        elif choice == '4':
            print("Đóng ca kiểm kho. Chào tạm biệt!")
            break
            
        else:
            print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")

if __name__ == "__main__":
    main()