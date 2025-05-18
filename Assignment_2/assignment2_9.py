# Write a program which accept one number from user and return number of digits in that number.
# Input: 5187934
# Output: 7

def countDigits(num):
    if (num == 0):
        return 1
    
    count = 0

    while (num > 0):
        num = num // 10
        count = count + 1
    
    return count

def main():
    print("Enter a number: ")
    num = float(input())
    result = countDigits(num)
    print(result)

if (__name__ == "__main__"):
    main()