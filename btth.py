raw_input = "   nGuyen vaN aN  ;  2004   "

while True:
    print("\n" + "="*5 + " HỆ THỐNG XỬ LÝ THÀNH VIÊN " + "="*5)
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("="*37)
    
    choice = input("Nhập lựa chọn của bạn (1-4): ")

    # Chức năng 1
    if choice == '1':
        print(f"\nDữ liệu gốc: '{raw_input}'")

    # Chức năng 2
    elif choice == '2':
        data = raw_input.split(';')
        ho_ten = data[0].strip().title()
        nam_sinh = int(data[1].strip())
        tuoi = 2026 - nam_sinh
        print(f"\nHọ tên: {ho_ten} | Tuổi: {tuoi}")

    # Chức năng 3
    elif choice == '3':
        data = raw_input.split(';')
        ten_parts = data[0].strip().lower().split() # ['nguyen', 'van', 'an']
        nam_sinh = data[1].strip()
        
        # Tạo Email: chữ cái đầu Họ + đầu tên đệm + tên chính
        email = f"{ten_parts[0][0]}{ten_parts[1][0]}{ten_parts[2]}@company.com"
        
        # Tạo ID: Tên chính viết hoa + 2 số cuối năm sinh
        ma_id = f"{ten_parts[2].upper()}{nam_sinh[2:]}"
        
        print("\n" + "*"*20)
        print(f"{'THẺ THÀNH VIÊN':^20}")
        print("*"*20)
        print(f"{'Họ tên:':<10} {data[0].strip().title()}")
        print(f"{'Email:':<10} {email}")
        print(f"{'ID:':<10} {ma_id}")
        print("*"*20)

    # Chức năng 4
    elif choice == '4':
        print("Tạm biệt! Hẹn gặp lại bạn.")
        break

    # Xử lý ngoại lệ
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
