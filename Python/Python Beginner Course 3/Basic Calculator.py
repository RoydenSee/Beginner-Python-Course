#Normal Calculator
num1 = float(input("Enter first number: "))
op = input("Type an Operator (+, -, *, /): ")
num2 = float(input("Enter Second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator!")
