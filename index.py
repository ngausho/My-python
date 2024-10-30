def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def calcutor():
    print("Welcome to the simple calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtration")
    print("3. Multiplication")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'exit' to quite: ")

        if choice == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        if choice in ['1', '2', '3', '4']:
            try:
                num1 =float(input("Enter first number: "))
                num2 =float(input("Enter second number: "))
            except ValueError:
                print("Invalid")