#ASSIGNMENT #02
# Simple Python Calculator

def calculator():
    print("'Simple Calculator By Rida Fatima'")
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        print("\nChoose an Operation:")
        print("1. Addition (+)")
        print("2. Subtracttion (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (+,-,*,/): ")

        if choice == '+':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '-':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '*':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("\nError: Cannot divide by zero.")
        else:
            print("\nInvalid input. Please choose a valid operation.")

    except ValueError:
        print("Invalid Value! Please enter numeric values only.")


calculator()
