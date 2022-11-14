s_denominator = 0
s = 0
for i in range(100):
    if i == 1:
        continue
    
    if i % 2 == 0:
        continue
    
    s_denominator += 1/i
    
s = 1 / s_denominator
s = round(s,2)
print("S= " + str(s))
    
# devided: phép chia
# fraction : phân số
# numerator: tử số
# denominator: mẫu số 
# naming convention: thông tục người ta dùng để đặt tên
# sematic meaning: biến phải có tên có ý nghĩa 
# _: underscore
# module: phần dư