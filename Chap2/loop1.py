x = float(input("Nhập x: "))
n = int(input("Nhập n (n>0): "))

if n <= 0:
    print("Vui lòng nhập n > 0!")
else:
    S = 0
    for i in range(1,n+ +1):
        S += x ** i
print(f"Kết quả S({x},{n})={S}")