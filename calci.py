num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %, ^): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("Error: cannot divide by zero.")
    else:
        print(f"Result: {num1 / num2}")
elif operator == "%":
    if num2 == 0:
        print("Error: cannot find remainder when dividing by zero.")
    else:
        print(f"Result: {num1 % num2}%")
elif operator == "^":
    print(f"Result: {num1 ** num2}")
else:
    print("Invalid operator. Please use +, -, *, /, %, or ^.")