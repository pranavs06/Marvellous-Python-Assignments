# Write a program which accept N numbers from user and store it into list. Return addition of all prime numbers from that list.
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined
# module named as MarvellousNum.
# Name of the function from main python file should be ListPrime().
# Input: Number of elements: 11
# Input Elements: 13 5 45 7 4 56 10 34 2 5 8
# Output: 54 (13 + 5 + 7 + 2 + 5)

from marvellousNum import checkPrime

def ListPrime(numbers):
    primeSum = 0
    for num in numbers:
        if checkPrime(num):
            primeSum = primeSum + num
    return primeSum

def main():
    print("Enter number of elements: ")
    n = int(input())
    numbers = []

    print("Input elements: ")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    result = ListPrime(numbers)
    print("Result: ", result)

if (__name__ == "__main__"):
    main()