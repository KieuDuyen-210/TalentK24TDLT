def fibonacci(n):
    a, b = 1, 1
    i = 3
    while i <= n:
        c = a + b
        a = b
        b = c
        i += 1
    return b


def listfibo(n):
    result = []
    a, b = 1, 1
    i = 1
    while i <= n:
        result.append(a)
        c = a + b
        a = b
        b = c
        i += 1
    return result


n1 = int(input("Nhập vị trí n cần tìm số Fibonacci: "))
while n1 < 1:
    print("n phải >= 1, vui lòng nhập lại!")
    n1 = int(input("Nhập vị trí n cần tìm số Fibonacci: "))

print(f"-> Số Fibonacci ở vị trí thứ {n1} là:", fibonacci(n1))

n2 = int(input("Nhập số N để xuất danh sách N số Fibonacci : "))
while n2 < 1:
    print("N phải >= 1, vui lòng nhập lại!")
    n2 = int(input("Nhập số N để xuất danh sách N số Fibonacci: "))

print(f"-> Dãy {n2} số Fibonacci đầu tiên là:", ", ".join(map(str, listfibo(n2))))