# Write a program which contains one lambda function which accepts two parameters and returns their multiplication.
# Input: 4 3, Output: 12
# Input: 6 3, Output: 18

multiply = lambda x, y : x * y

def main():
    print("Enter first number: ")
    num1 = int(input())
    print("Enter second number: ")
    num2 = int(input())
    
    result = multiply(num1, num2)
    print("The multiplication of ", num1, " and ", num2, " is: ", result)

if (__name__ == "__main__"):
    main()