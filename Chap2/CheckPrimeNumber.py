n = int(input("Nhập n:"))
count = 0
i = 1
while i<=n:
    if n % i == 0:
        count += 1
    i = i + 1
if count == 2:
    print (f"{n} is a prime number")
else:
    print (f"{n} is not a prime number")