# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply
# each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda
# functions).
# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def checkPrime(num):
    if num == 0 or num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    return True

def multiplicationByTwo(num):
    return num * 2

def findMaximum(x, y):
    if (x > y):
        return x 
    else:
        return y

def main():
    print("Enter numbers of elements to accept: ")
    num = int(input())

    numList = []
    print("Enter the numbers: ")
    for i in range(num):
        print("Enter number ", (i + 1), ": ")        
        numList.append(int(input()))

    print("List of numbers: ", numList)

    # Filter prime numbers
    filteredList = list(filter(checkPrime, numList))
    print("List after filter: ", filteredList)

    # Multiply each number by 2
    mappedList = list(map(multiplicationByTwo, filteredList))
    print("List after map:", mappedList)

    # Find maximum number
    result = reduce(findMaximum, mappedList)
    print("Output of reduce:", result)

if (__name__ == "__main__"):
    main()