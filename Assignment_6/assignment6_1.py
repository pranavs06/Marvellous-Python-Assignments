# Write a program using a while loop to print numbers from 1 to 50.
# Expected Output:
# 1 2 3 4 ... 50

def displayNmbers():
    i = 1
    while (i <= 50):
        print(i, end=" ")
        i += 1

def main():
    displayNmbers()

if (__name__ == "__main__"):
    main()