# Vowel or Consonant Check
# Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not, print it's a consonant.
# Expected Input:
# Enter a character: e
# Expected Output:
# 'e' is a vowel.

def checkVowelOrConsonant():
    try:
        char = input("Enter a character: ")
        if ((len(char) != 1) or (not char.isalpha())):
            raise ValueError("Please enter a single alphabetic character.")
        
        if char in 'aeiou':
            print(char, " is a vowel.")
        else:
            print(char, " is a consonant.")
    except ValueError as ve:
        print(ve)
        return
    except Exception as e:
        print("An unexpected error occurred: ", e)
        return

def main():
    checkVowelOrConsonant()

if (__name__ == "__main__"):
    main()