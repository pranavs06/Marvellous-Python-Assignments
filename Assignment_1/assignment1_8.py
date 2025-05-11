# Write a program which accept number from user and print that number of "*" on screen.

def displayStars(num):
    for i in range(num):
        print("*", end=" ")
    print()  # For a new line after printing stars

def main():
    number = int(input("Enter a number: "))
    displayStars(number)

if __name__ == "__main__":
    main()