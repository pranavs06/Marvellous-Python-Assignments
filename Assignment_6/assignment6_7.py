# Accept 5 numbers from the user. Find and print the largest number.
# Expected Input:
# Enter 5 numbers: 23 89 12 56 45
# Expected Output:
# Maximum number is: 89

def findLargestNumber():
    numbers = []
    print("Enter 5 numbers: ")
    for i in range(5):
        number = int(input("Enter a number: "))
        numbers.append(number)
    largestNumber = max(numbers)
    print("Maximum number is: ", largestNumber)

def main():
    findLargestNumber()

if (__name__ == "__main__"):
    main()