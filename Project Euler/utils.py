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

def generatePrimesUnder(max):
    primes = []
    for n in range(max):
        if isPrime(n):
            primes.append(n)
    return primes


def extractDigits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits

def reconstructFromDigits(digits):
    number = 0
    for i in range(len(digits)):
        number += digits[i] * 10**i
    return number

def isPalindromicNumber(num):
    digits = extractDigits(num)
    for r in range(len(digits)):
        if digits[r] != digits[-r-1]:
            return False
    return True