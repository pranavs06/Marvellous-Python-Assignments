# Write a program which contains one function named as ChkNum() which accept one paramter as number.
# If number is even then it should display "Even number" otherwise display "Odd number" on console.

def checkNumber(no):
    if no % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def main():
    checkNumber(11)
    checkNumber(8)

if __name__ == "__main__":
    main()