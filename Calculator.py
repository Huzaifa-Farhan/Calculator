# Define the function for addition
def add(x, y):
    return x + y

# Define the function for subtraction
def subtract(x, y):
    return x - y

# Define the function for multiplication
def multiply(x, y):
    return x * y

# Define the function for division
def divide(x, y):
    # Check if the divisor is zero to avoid division by zero
    if y == 0:
        return "Undefined (division by zero)"
    return x / y

# Infinite loop to continue calculations until the user decides to stop
while True:
    # Get user input for the numbers, with error handling for invalid input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    # Display the available operations to the user
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Get the user's choice of operation
    choice = input("\nEnter choice (1/2/3/4): ")
    
    # Perform the selected operation and display the result
    if choice == '1':
        print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"\nResult: {num1} x {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"\nResult: {num1} ÷ {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input")
    
    # Ask if the user wants to perform another calculation
    next_calculation = input("\nDo another calculation? (yes/no): ")
    
    # Break the loop if the user does not want to continue
    if next_calculation.lower() != 'yes':
        break