def calculator():
    print("Welcome to Simple Calculator!")

    # Pehla number lo
    num1 = float(input("Enter first number: "))

    # Operator lo (+, -, *, /)
    operator = input("Enter operator (+, -, *, /): ")

    # Dusra number lo
    num2 = float(input("Enter second number: "))

    # Ab check karo operator kya hai
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Error: Cannot divide by 0"
        else:
            result = num1 / num2
    else:
        result = "Invalid operator"

    print("Result:", result)

# Function ko call karo
calculator()
