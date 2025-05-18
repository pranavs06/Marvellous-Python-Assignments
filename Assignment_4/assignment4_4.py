# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# The list contains the numbers which are accepted from the user. Filter should filter out all such numbers which are even.
# Map function will calculate its square. Reduce will return the addition of all those numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

checkNumberEven = lambda x : x % 2 == 0
squareOfNumber = lambda x : x ** 2
additionOfTwoNumbers = lambda x, y : x + y

def main():
    print("Enter numbers of elements to accept: ")
    num = int(input())

    numList = []
    print("Enter the numbers: ")
    for i in range(num):
        print("Enter number ", (i + 1), ": ")        
        numList.append(int(input()))

    print("List of numbers: ", numList)

    # even numbers
    filteredList = list(filter(checkNumberEven, numList))
    print("List after filter: ", filteredList)

    # square of each number
    mappedList = list(map(squareOfNumber, filteredList))
    print("List after map:", mappedList)

    # sum of all numbers
    result = reduce(additionOfTwoNumbers, mappedList)
    print("Output of reduce:", result)

if (__name__ == "__main__"):
    main()