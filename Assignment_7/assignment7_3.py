# Accept a list of numbers and use the filter() function to keep only even numbers.
# Expected Input:
# Enter List: 1 2 3 4 5 6.
# Expected Output:
# Even numbers: [2, 4, 6]

def isEven(x):
    return (x % 2 == 0)

def main():
    try:
        print("Enter number of integers in the list:")
        n = int(input())
        if (n <= 0):
            raise ValueError("Number of integers must be positive.")
        
        numbers = []
        for i in range(n):
            print("Enter integer", (i + 1), ": ")
            num = int(input())
            if (num < 0):
                raise ValueError("Integer cannot be negative.")
            numbers.append(num)
        
        evenNumbers = list(filter(isEven, numbers))
        print("Even numbers: ", evenNumbers)
    except ValueError as ve:
        print("Invalid input. Please enter integers only.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if (__name__ == "__main__"):
    main()