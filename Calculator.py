print("=== Python Calculator ===")

num1 = float(input("Enter first number: "))
operator = input("Choose operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    if num1 >= num2:
        result = num1 - num2
        print("Result (num1 minus num2):", result)
    else:
        result = num2 - num1
        print("Result (num2 minus num1):", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Error: Invalid operator.")
