# Write a program which accept N numbers from user and store it into list. Return minimum number from that list.
# Input: Number of elements: 4
# Input Elements: 13 5 45 7
# Output: 5

def main():
    print("Enter number of elements: ")
    n = int(input())
    numbers = []

    print("Input elements: ")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    result = min(numbers)
    print("Result: ", result)
    
if (__name__ == "__main__"):
    main()