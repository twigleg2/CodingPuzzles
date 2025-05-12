import math

# charToAlphabetValue = {chr(i): i - 64 for i in range(65, 91)}  # A=1, B=2, ..., Z=26
upperCharToAlphabetValue = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
# charToAlphabetValue = {chr(i): i - 96 for i in range(97, 123)}  # a=1, b=2, ..., z=26
lowerCharToAlphabetValue = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
charToAlphabetValue = {**upperCharToAlphabetValue, **lowerCharToAlphabetValue}

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

def generateNextPrime(number):
    while True:
        number += 1
        if isPrime(number):
            return number

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

def nthTriangleNumber(n):
    return 0.5 * n * (n+1)

def isTriangleNumber(num):
    n = (math.sqrt(8 * num + 1) - 1) / 2
    return n == int(n)

def wordValue(word):
    return sum([charToAlphabetValue[char] for char in word])