# Write a program which accept N numbers from user and store it into list. Accept one another number from user and return
# frequency of that number from that list.
# Input: Number of elements: 11
# Input Elements: 13 5 45 7 4 56 5 34 2 5 65
# Element to search: 5
# Output: 3

def main():
    print("Enter number of elements: ")
    n = int(input())
    numbers = []

    print("Input elements: ")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    print("Element to search: ")
    elementToSearch = int(input())

    frequency = numbers.count(elementToSearch)
    print("Frequency of", elementToSearch, "is:", frequency)

if (__name__ == "__main__"):
    main()