# Write two lambda functions:
# -> One to calculate square of a number.
# -> Another to calculate cube of a number.
# Expected Input:
# Enter a number: 3
# Expected Output:
# Square: 9
# Cube: 27

square = lambda x: x ** 2
cube = lambda x: x ** 3

def main():
    try:
        number = int(input("Enter a number: "))
        if (number < 0):
            raise ValueError("Number cannot be negative.")
                
        print("Square: ", square(number))
        print("Cube: ", cube(number))
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An unexpected error occurred: ", e)

if (__name__ == "__main__"):
    main()