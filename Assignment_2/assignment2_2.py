# Write a program which accept one number and display below pattern.
# Input: 5
# Output:
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

def displayPattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def main():
    num = int(input("Enter a number: "))
    if (num <= 0):
        print("Number must be a positive value other than 0.")
        return

    displayPattern(num)

if (__name__ == "__main__"):
    main()