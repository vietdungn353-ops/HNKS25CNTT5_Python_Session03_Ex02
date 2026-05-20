# Hệ thống thông báo sai do đã đặt sai điều kiện khi lọc kết
# quả của các thông tin được nhận vào. Phần điều kiện của if 
# đang dùng toán tử or nên chỉ cần thoải mãn 1 trong 2 điều 
# đặt ra là đã đủ điều kiện hiến máu
# Sửa

print(" -- BLOOD DONOR SCREENING SYSTEM -- ")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra diều kiện hiến mu
if donor_age >18 and donor_weight > 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")