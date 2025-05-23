# Accept a number and print its factorial using a for loop.
# Expected Input:
# Enter a number: 5
# Expected Output:
# Factorial of 5 is: 120

def displayFactorial():
    number = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    print("Factorial of ", number, " is: ", factorial)

def main():
    displayFactorial()

if (__name__ == "__main__"):
    main()