def calculate():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")
    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        print(f"Result: {num1 / num2 if num2 != 0 else 'Error: Division by zero'}")
    else:
        print("Invalid operation")

calculate()
