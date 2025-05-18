# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# The list contains the numbers which are accepted from the user. Filter should filter out all such numbers which are greater
# than or equal to 70 and less than or equal to 90. The map function will increase each number by 10. Reduce will return the
# product of all those numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

checkNumberInRange = lambda x : 70 <= x <= 90
increaseByTen = lambda x : x + 10
multiplicationOfTwoNumbers = lambda x, y : x * y

def main():
    print("Enter numbers of elements to accept: ")
    num = int(input())

    # Accepting a list of numbers from the user
    numList = []
    print("Enter the numbers: ")
    for i in range(num):
        print("Enter number ", (i + 1), ": ")        
        numList.append(int(input()))

    print("List of numbers: ", numList)

    # Numbers greater than or equal to 70 and less than or equal to 90
    filteredList = list(filter(checkNumberInRange, numList))
    print("List after filter: ", filteredList)

    # Increasing each number by 10
    mappedList = list(map(increaseByTen, filteredList))
    print("List after map:", mappedList)

    # Product of all numbers
    result = reduce(multiplicationOfTwoNumbers, mappedList)
    print("Output of reduce:", result)

if (__name__ == "__main__"):
    main()