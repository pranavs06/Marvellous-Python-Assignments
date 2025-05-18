# Write a program which accept number from user and return addition of all digits in that number.
# Input: 5187934
# Output: 37

def sumDigits(num):
    if (num == 0):
        return 0
    
    sum = 0

    while (num > 0):
        digit = num % 10
        sum = sum + digit
        num = num // 10
    
    return sum

def main():
    print("Enter a number: ")
    num = int(input())
    result = sumDigits(num)
    print(result)

if (__name__ == "__main__"):
    main()