def do_math(a,b,op):
    match op:
        case "+":
            return f"{a} + {b} = {a+b}"
        case "-":
            return f"{a} - {b} = {a - b}"
        case "*":
            return f"{a} * {b} = {a * b}"
        case "/":
            if b == 0:
                return "can't dividde bt zero"
            return f"{a} / {b} = {a / b}"
        case _:
            return "can't do the math"
