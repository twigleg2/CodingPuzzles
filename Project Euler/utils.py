import math

def helloWorld():
    print("Hello World!")

def isPrime(num):
    if num < 2:
        return False
    
    for r in range(2, math.floor(math.sqrt(num)) + 1):
        if num % r == 0:
            return False
    return True


def extractDigits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits.reverse()
    return digits
