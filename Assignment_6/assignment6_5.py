# Accept a number from the user and check whether it is prime or not.
# Expected Input:
# Enter a number: 11
# Expected Output:
# 11 is a prime number.

def isPrime(number):
    if (number <= 1):
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if (number % i == 0):
            return False
    return True

def main():
    number = int(input("Enter a number: "))
    if isPrime(number):
        print(number, " is a prime number.")
    else:
        print(number, " is not a prime number.")

if __name__ == "__main__":
    main()