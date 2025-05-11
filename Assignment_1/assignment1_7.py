# Write a program which contains one function that accept one number from user
# and returns true if that number is divisible by 5 otherwise return false.

def isDivisibleByFive(num):
    if num % 5 == 0:
        return True
    else:
        return False

def main():
    number = int(input("Enter a number: "))
    result = isDivisibleByFive(number)
    print("Result: ", result)

if __name__ == "__main__":
    main()