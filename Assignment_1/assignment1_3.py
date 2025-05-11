# Write a program which contains one function named as Add() which accept two numbers from user and
# return addition of that two numbers.

def add(num1, num2):
    return num1 + num2

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    
    result = add(number1, number2)
    print("The addition of ", number1, " and ", number2, " is: ", result)

if __name__ == "__main__":
    main()