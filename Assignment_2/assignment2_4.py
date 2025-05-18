# Write a program which accept one number from user and and returns addition of its factors.

def factorsSum(n):
    result = 0
    for i in range(1, n):
        if (n % i == 0):
            result = result + i
    return result

def main():
    num = int(input("Enter a number: "))
    if (num < 0):
        print("Number must be a positive value other than 0.")
        return
    
    result = factorsSum(num)
    print("Sum of factors of ", num, " is ", result)

if (__name__ == "__main__"):
    main()