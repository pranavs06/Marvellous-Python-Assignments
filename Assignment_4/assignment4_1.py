# Write a program which contains one lambda function which accepts one parameter and returns the power of two.
# Input: 4, Output: 16
# Input: 6, Output: 64

powerOfTwo = lambda x : 2 ** x

def main():
    print("Enter a number to find its power of two:")
    num = int(input())
    result = powerOfTwo(num)
    print("The power of two for ", num, " is: ", result)

if (__name__ == "__main__"):
    main()