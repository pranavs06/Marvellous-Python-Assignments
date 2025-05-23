# Area and Perimeter of Rectangle
# Accept the length and width of a rectangle. Calculate and display the area and perimeter.
# Expected Input:
# Enter length: 5
# Enter width: 3
# Expected Output:
# Area: 15
# Perimeter: 16

def calculateAreaAndPerimeter():
    try:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        
        if (length <= 0 or width <= 0):
            raise ValueError("Length and width must be positive numbers.")
        
        area = length * width
        perimeter = 2 * (length + width)
        
        print("Area of rectangle is: ", area)
        print("Perimeter of rectangle is: ", perimeter)
    except ValueError as ve:
        print(ve)
        return
    except Exception as e:
        print("An unexpected error occurred: ", e)
        return

def main():
    calculateAreaAndPerimeter()

if (__name__ == "__main__"):
    main()