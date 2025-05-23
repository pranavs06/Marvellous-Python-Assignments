# Print Triangle Pattern using Nested Loops
# Expected Output:
# *
# * *
# * * *
# * * * *

def displayTrianglePattern():
    rows = 4
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()  # Move to the next line after each row

def main():
    displayTrianglePattern()

if (__name__ == "__main__"):
    main()