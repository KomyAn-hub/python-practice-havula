num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /, //, %, **): ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
    print(f"{num1} {op} {num2} = {result:.4f}")
elif op == "-":
    result = num1 - num2
    print(f"{num1} {op} {num2} = {result:.4f}")
elif op == "*":
    result = num1 * num2
    print(f"{num1} {op} {num2} = {result:.4f}")
elif op == "/":
    if num2 == 0:
        print("Error: division by zero is not possible")
    else:
        result = num1 / num2
        print(f"{num1} {op} {num2} = {result:.4f}")
elif op == "//":
    if num2 == 0:
        print("Error: division by zero is not possible")
    else:
        result = num1 // num2
        print(f"{num1} {op} {num2} = {result:.4f}")
elif op == "%":
    if num2 == 0:
        print("Error: division by zero is not possible")
    else:
        result = num1 % num2
        print(f"{num1} {op} {num2} = {result:.4f}")
elif op == "**":
    result = num1 ** num2
    print(f"{num1} {op} {num2} = {result:.4f}")
else:
    print("Error: unknown operation symbol")