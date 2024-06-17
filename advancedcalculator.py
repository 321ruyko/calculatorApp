import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

# Function to calculate exponentiation
def power(x, y):
    return x ** y

# Function to calculate square root
def square_root(x):
    if x < 0:
        return "Invalid input: cannot compute square root of a negative number"
    else:
        return math.sqrt(x)

# Function to calculate modulus
def modulus(x, y):
    if y == 0:
        return "Cannot compute modulus with zero divisor!"
    else:
        return x % y

# Main calculator function
def calculator():
    print("Welcome to the Advanced Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Modulus")
    print("0. Exit")

    while True:
        choice = input("Enter choice (0-7): ")

        if choice == '0':
            print("Exiting calculator. Goodbye!")
            break

        elif choice in ['1', '2', '3', '4', '5', '7']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '7':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            print(f"√{num} = {square_root(num)}")

        else:
            print("Invalid input. Please enter a number between 0 and 7.")

        print()  # Print a blank line for better readability

# Run the calculator function
calculator()
