# Even or Odd Number Check
# Write a program to check whether the entered number is even or odd.
# Expected Input:
# Enter a number: 17
# Expected Output:
# 17 is an odd number.

def checkEvenOrOdd():
    try:
        num = int(input("Enter a number: "))
        if (num % 2 == 0):
            print(num, "is an even number.")
        else:
            print(num, "is an odd number.")
    except ValueError as ve:
        print(ve)
        return
    except Exception as e:
        print("An unexpected error occurred: ", e)
        return

def main():
    checkEvenOrOdd()

if (__name__ == "__main__"):
    main()