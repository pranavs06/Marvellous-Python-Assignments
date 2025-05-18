# Write a program which accept one number from user and check whether number is prime or not.
# Input: 5
# Output: It is Prime Number.

def checkPrime(num):
    if (num < 2):
        return False
    for i in range(2, num):
        if (num % i == 0):
            print("Found a factor: ", i)
            return False
    return True

def main():
    num = int(input("Enter a number: "))
    if (num < 0):
        print("Number must be a positive value other than 0.")
        return
    
    if (checkPrime(num)):
        print("It is Prime Number.")
    else:
        print("It is not Prime Number.")

if (__name__ == "__main__"):
    main()