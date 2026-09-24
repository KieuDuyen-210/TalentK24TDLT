def chuM(n):
    i = 0
    while i <= n:
        j = 0
        while j <= n:
            if j == 0 or j == n - 1 or (i==j and i<=n//2) or (i+j==n-1 and i<=n//2):
                print("*", end=' ')
            else:
                print(" ", end=' ')
            j = j + 1
        print(" ")
        i = i + 1
chuM(5)

from math import sqrt, pow
def calculate(m, n, a, b):
    s1 = s2 = 0
    for i in range(m, n+1):
        c = True if sqrt(i) % 1 == 0 else False
        if c:
            if a <= i <= b and i % 2 == 0:
                continue
            else:
                s1 += i
        else:
            for j in range(1, i):
                if i % j == 0 and j % 2 == 0:
                    s2 += j
    return s1, s2

m = 2
n = m**3*3 + 2
a = int(sqrt(n)) - 2
b = pow(a, 2) + 1
print(f"m = {m}, n = {n}, a = {a}, b = {b}")
x, y = calculate(m, n, a, b)
print("x = {}, y = {}".format(x, y))