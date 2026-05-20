# Sai: do không có ràng buộc cho thông báo chúc mừng nhận lương,
# khiến dòng thông báo luôn được chạy kể cả khi người đó nhận được 
# 0 lương. 
# Cách sửa: đóng gói phần tính lương và thông báo vào bên trong 
# phần else của cái if 

print (" --- HỆ THỐNG GỬI EMAIL THƯỜNG TẾT --- ")

# Vòng Lặp chạy đúng 3 Lần cho 3 nhân viên
for employee_number in range(1, 4):
    print (" --- Đang xử lý nhân vien số", employee_number, " --- ")

    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input ("Nhập số ngày công trong thang: "))

    # Kiểm tra diều kiện
    if working_days == 0:
        print ("CẢNH BÁO: Nhân viên nghi ca thang. Khong xet duyet thưởng.")
    else:
        bonus_amount = working_days * 200000
        print("-> Đã gui Email: Chúc mung nhan dược", bonus_amount, "VNĐ tien thưởng!")
        print("----------------------------------------------\n")

print("Đa hoan tat qua trinh duyệt thưởng cho 3 nhân viên!")

