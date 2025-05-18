# Write a program which accept one number from user and returns its factorial.

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        result = 1
        for i in range(n, 1, -1):
            result = result * i
    
    return result

def main():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    if (num < 0):
        print("Number must be a positive value other than 0.")
        return

    result = factorial(num)
    print("Factorial of ", num, " is ", result)

if (__name__ == "__main__"):
    main()