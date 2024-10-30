print("Welcome to my calculator")

user_input = float(input("Enter first number:\n"))

operation_type = input("Enter the operation type:\n")

user_input_second = float(input("Enter the second number:\n"))

result = 0
if operation_type == "+":
    result = user_input + user_input_second
elif operation_type == "-":
    result = user_input - user_input_second
elif operation_type == "*":
    result = user_input * user_input_second
elif operation_type == "/":
    result = user_input / user_input_second
print("Your result is: ", result)