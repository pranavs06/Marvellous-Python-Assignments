# Write a program which accept name from user and display length of its name.

def displayNameLength(name):
    length = len(name)
    print("The length of the name ", name, " is: ", length)

def main():
    name = input("Enter your name: ")
    displayNameLength(name)

if __name__ == "__main__":
    main()