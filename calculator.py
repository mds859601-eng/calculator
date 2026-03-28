# ================= CALCULATOR PROGRAM =================

# This function performs addition
def add(a, b):
    return a + b


# This function performs subtraction
def subtract(a, b):
    return a - b


# This function performs multiplication
def multiply(a, b):
    return a * b


# This function performs division
def divide(a, b):
    # Check to avoid division by zero error
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# ================= MAIN PROGRAM =================

# Infinite loop so calculator keeps running until user exits
while True:

    # Display menu options to the user
    print("\n===== Simple Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    # Take user choice
    choice = input("Enter your choice (1-5): ")

    # If user wants to exit
    if choice == '5':
        print("Calculator closed. Thank you!")
        break

    # Take two numbers as input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    # Perform operation based on user choice
    if choice == '1':
        print("Result:", add(num1, num2))

    elif choice == '2':
        print("Result:", subtract(num1, num2))

    elif choice == '3':
        print("Result:", multiply(num1, num2))

    elif choice == '4':
        print("Result:", divide(num1, num2))

    else:
        print("Invalid choice! Please select from 1 to 5.")