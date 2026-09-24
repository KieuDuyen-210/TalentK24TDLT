n = int(input("Nhập n:"))
tong = 0
i = 1
while i < n:
    if n % i == 0:
        tong = tong + i
    i = i + 1
if tong == n:
    print(f"{n} is a perfect number")
else:
    print (f"{n} is not a perfect number")
