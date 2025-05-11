# Write a program which accept number from user and check whether that number is positive
# or negative or zero.

def checkNumber(num):
    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    number = int(input("Enter a number: "))
    checkNumber(number)

if __name__ == "__main__":
    main()