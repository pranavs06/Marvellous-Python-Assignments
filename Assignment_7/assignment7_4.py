# Accept a list of numbers and use reduce() (from functools) to find the product of all numbers.
# Expected Input:
# Enter list: 2 3 4
# Expected Output:
# Product: 24

from functools import reduce

def product(x, y):
    return (x * y)

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
        
        productOfNumbers = reduce(product, numbers)
        print("Product: ", productOfNumbers)
    except ValueError as ve:
        print("Invalid input. Please enter integers only.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if (__name__ == "__main__"):
    main()