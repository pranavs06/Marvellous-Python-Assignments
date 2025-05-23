# Arithmetic Operations on Two Numbers
# Write a program to accept two integers from the user and display their:
# -> Sum
# -> Difference
# -> Product
# -> Division
# Expected Input:
# Enter first number: 10
# Enter second number: 2
# Expected Output:
# Sum: 12
# Difference: 8
# Product: 20
# Division: 5.0

def arithmeticOperations():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        additionResult = num1 + num2
        subtractionResult = num1 - num2
        productResult = num1 * num2
        divisionResult = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return
    except ValueError:
        print("Error: Please enter valid integers.")
        return
    except Exception as e:
        print("An unexpected error occurred: ", e)
        return

    print("Sum: ", additionResult)
    print("Difference: ", subtractionResult)
    print("Product: ", productResult)
    print("Division: ", divisionResult)

def main():
    arithmeticOperations()

if (__name__ == "__main__"):
    main()