def checkPrime(num):
    if num == 0 or num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    return True