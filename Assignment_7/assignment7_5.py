# Write a function that accepts a string and checks whether it is a palindrome.
# Expected Input:
# Enter a string: radar
# Expected Output:
# radar is a palindrome.

def isPalindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    
    n = len(s)
    for i in range(len(s) // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

def main():
    try:
        print("Enter a string:")
        s = input()
        
        if isPalindrome(s):
            print(s, "is a palindrome.")
        else:
            print(s, "is not a palindrome.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if (__name__ == "__main__"):
    main()