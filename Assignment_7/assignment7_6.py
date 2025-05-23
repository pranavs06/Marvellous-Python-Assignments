# Write a function that accepts a list of integers and returns a list of prime numbers using filter().
# Expected Input:
# Enter list: 10 11 12 13 14 15 16 17
# Expected Output:
# Prime numbers: [11, 13, 17]

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        print("Enter number of integers in the list:")
        n = int(input())
        if (n <= 0):
            raise ValueError("Number of integers must be positive.")
        
        numbers = []
        for i in range(n):
            print("Enter integer", (i + 1), ": ")
            num = int(input())
            if (num < 0):
                raise ValueError("Integer cannot be negative.")
            numbers.append(num)
        
        primeNumbers = list(filter(isPrime, numbers))
        print("Prime numbers: ", primeNumbers)
    except ValueError as ve:
        print("Invalid input. Please enter integers only.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if (__name__ == "__main__"):
    main()