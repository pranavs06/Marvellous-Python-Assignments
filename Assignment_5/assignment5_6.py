# Celsius to Fahrenheit Converter
# Accept temperature in Celsius and convert it to Fahrenheit using the formula:
# F=(C × 9/5) + 32
# Expected Input:
# Enter temperature in Celsius: 25
# Expected Output:
# Temperature in Fahrenheit: 77.0°F

def celsiusToFahrenheit():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        if (celsius < -273.15):
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
        
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit is : " + str(fahrenheit) + "°F")
    except ValueError as ve:
        print(ve)
        return
    except Exception as e:
        print("An unexpected error occurred: ", e)
        return

def main():
    celsiusToFahrenheit()

if (__name__ == "__main__"):
    main()