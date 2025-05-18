# Write a program which accept one number and display below pattern.
# Input: 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

def displayPattern(num):
    for i in range(num, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
    return

def main():
    num = int(input("Enter a number: "))
    if (num < 0):
        print("Number must be a positive value other than 0.")
        return
    
    displayPattern(num)

if (__name__ == "__main__"):
    main()