def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Undefined (division by zero)"
    return x / y

while True:
    # User input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    # Operation input
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("\nEnter choice (1/2/3/4): ")
    
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
    
    next_calculation = input("\nDo another calculation? (yes/no): ")
    
    if next_calculation.lower() != 'yes':
        break
