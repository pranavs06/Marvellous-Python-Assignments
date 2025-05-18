# Write a program which accept N numbers from user and store it into list. Return maximum number from that list.
# Input: Number of elements: 7
# Input Elements: 13 5 45 7 4 56 34
# Output: 56

def main():
    print("Enter number of elements: ")
    n = int(input())
    numbers = []

    print("Input elements: ")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    result = max(numbers)
    print("Result: ", result)

if (__name__ == "__main__"):
    main()