# Accept a list of integers from the user and use the map() function to double each value.
# Expected Input:
# Enter list: 1 2 3 4 5
# Expected Output:
# Doubled list: [2, 4, 6, 8, 10]

def double(x):
    return x * 2

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
        
        doubledNumbers = list(map(double, numbers))
        print("Doubled list: ", doubledNumbers)
    except ValueError as ve:
        print("Invalid input. Please enter integers only.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if (__name__ == "__main__"):
    main()