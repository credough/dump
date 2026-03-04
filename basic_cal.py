def basic_cal(a, b, op):
    if op == "+": return a + b
    elif op == "-": return a - b
    elif op == "*": return a * b
    elif op == "/":
        if b == 0:
            return "Error! Division by zero"
        else: return a / b
    else:
        return "unknown operator"
    
print(basic_cal(10, 3, "/"))