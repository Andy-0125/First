operate = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operate == '+':
    print(round(num1 + num2, 3))
elif operate == '-':
    print(round(num1 - num2, 3))
elif operate == '*':
    print(round(num1 * num2, 3))
elif operate == '/':
    if num2 != 0:
        print(round(num1 / num2, 3))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")