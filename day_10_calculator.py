from day_10_art import logo
import os

print(logo)
print("Welcome to the calculator")

# Operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

def mod(n1, n2):
    return n1 % n2

# Dictionary to map symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": mod
}

def calculator():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    
    number1 = float(input("What's the first number?: "))

    while True:
        operation = input("Pick an operation: + \n - \n * \n / \n % \n ")
        if operation not in operations:
            print("Invalid operation. Try again.")
            continue
        
        number2 = float(input("What's the next number?: "))
        result=0
        if operation == '+':
            result = add(number1, number2)
        elif operation == '-':
            result = subtract(number1, number2)
        elif operation == '*':
            result = multiply(number1, number2)
        elif operation == '/':
            result = divide(number1, number2)
        elif operation == '%':
            result = mod(number1, number2)
        print(f"{number1} {operation} {number2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if choice == 'y':
            number1 = result
        elif choice == 'n':
            calculator()  # Restart the calculator
            break
        else:
            print("Invalid choice. Exiting program.")
            break

calculator()
