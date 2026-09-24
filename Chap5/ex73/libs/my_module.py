from math import sqrt


def quadratic_solver(a, b, c):
    if a == 0:
        # bx + c = 0
        if b == 0:
            return "Infinite solutions" if c == 0 else "No solutions"
        else:
            x = -c / b
            return f"Solution x = {x}"
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            return "No solutions"
        elif delta == 0:
            x = -b / (2 * a)
            return f"Double solutions x1 = x2 = {x}"
        else:
            x1 = (-b - sqrt(delta)) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            return f"x1 = {x1}, x2 = {x2}"