# Simple Calculator

def calculator():
    print("Welcome to the Simple Calculator!")

    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Choose an operation: +, -, *, /")
    operation = input("Enter operation: ")

    # Perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    # Display result
    print("Result:", result)

# Run the calculator
calculator()
