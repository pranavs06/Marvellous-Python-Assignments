# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction,
# Mult() for multiplication and Div() for division. All functions accept two parameters as number and perform
# the operation. Write on python program which call all the funtions from Arithmetic module by accepting the
# parameters from user.

from arithmetic import add, sub, mult, div

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    
    print("Addition is: ", add(num1, num2))
    print("Subtraction is: ", sub(num1, num2))
    print("Multiplication is: ", mult(num1, num2))
    print("Division: ", + div(num1, num2))

if (__name__ == "__main__"):
    main()