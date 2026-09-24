x = float(input("Nhập x: "))
n = int(input("Nhập n (n>0): "))

if n <= 0:
    print("Vui lòng nhập n > 0!")
else:
    S=0
    for i in range(1,n+1):
        giai_thua = 1
        for j in range(1,i+1):
            giai_thua *= j
        S += (x ** i) / giai_thua
print(f"Kết quả S({x},{n})={S}")