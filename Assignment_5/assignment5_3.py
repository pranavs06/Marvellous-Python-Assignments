# Voting Eligibility Checker
# Accept age from the user and check whether the person is eligible to vote. (Age should be 18 or above.)
# Expected Input: Enter age: 19
# Expected Output: Eligible to vote.

def checkVotingEligibility():
    try:
        age = int(input("Enter age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if age >= 18:
            print("Eligible to vote.")
        else:
            print("Not eligible to vote.")
    except ValueError as ve:
        print(ve)
        return
    except Exception as e:
        print("An unexpected error occurred: ", e)
        return

def main():
    checkVotingEligibility()

if (__name__ == "__main__"):
    main()