n = int(input("Nhập n (số lẻ: "))

while n % 2 == 0 or n < 1:
    print("Không hợp lệ! Vui lòng chỉ nhập số lẻ.")
    n = int(input("Nhập lại n (số lẻ): "))

size = 2 * n - 1
center = n - 1

i = 0
while i < size:
    j = 0
    while j < size:
        if abs(i - center) + abs(j - center) == center:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1