def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers."""
    if y == 0:
        return "Error: Division by zero"
    return x / y

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation")
            continue

        if operation == '+':
            print("Result:", add(num1, num2))
        elif operation == '-':
            print("Result:", subtract(num1, num2))
        elif operation == '*':
            print("Result:", multiply(num1, num2))
        elif operation == '/':
            print("Result:", divide(num1, num2))

        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            break

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")