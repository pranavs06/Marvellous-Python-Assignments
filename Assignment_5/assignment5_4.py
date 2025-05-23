# Find Largest Among Three Numbers
# Accept three numbers from the user and print the largest using nested if-else statements.
# Expected Input: Enter three numbers: 5 9 3
# Expected Output: Largest number is 9.

def findLargestNumber():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: "))
        
        largest = 0

        if (num1 >= num2):
            if (num1 >= num3):
                largest = num1
            else:
                largest = num3
        else:
            if (num2 >= num3):
                largest = num2
            else:
                largest = num3

        print("Largest number is: ", largest)
    except ValueError as ve:
        print(ve)
        return
    except Exception as e:
        print("An unexpected error occurred: ", e)
        return

def main():
    findLargestNumber()

if (__name__ == "__main__"):
    main()