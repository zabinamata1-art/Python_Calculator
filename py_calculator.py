# This is a simple calculator program in Python

def introduction():
    print("\t\t\tWelcome to the calculator!")
    print("\t\t--------------------------------------------")
    print("\tThis calculator can perform basic arithmetic operations.")
    print("\n")

def user_input():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("\nEnter the operation (1/2/3/4): ")
    return num1, num2, operation

    
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("\nError: Division by zero is not allowed.")
        return None

def main_work(num1, num2, operation):
    if operation == '1':
        result = addition(num1, num2)
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '2':
        result = subtraction(num1, num2)
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '3':
        result = multiplication(num1, num2)
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '4':
        result = division(num1, num2)
        if result is not None:
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid operation. Please select a valid option (1/2/3/4).")


def main():
    introduction()
    num1, num2, operation = user_input()
    main_work(num1, num2, operation)

if __name__ == "__main__":
    main()