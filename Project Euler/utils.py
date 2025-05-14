import math

# All methods were originally written by me unless otherwise noted.
# Some methods have been enhanced with the help of GitHub Copilot.

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
    
    for r in range(2, int(math.sqrt(num)) + 1):
        if num % r == 0:
            return False
    return True

# My original implementation of this method was very slow.  
# When I asked GitHub Copilot to help optimize it, it taught me about the Sieve of Eratosthenes
def generatePrimesUnder(max):
    """Generate all prime numbers less than max using the Sieve of Eratosthenes."""
    if max < 2:
        return []
    
    # Create a boolean array where True indicates a prime number
    is_prime = [True] * max
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(math.sqrt(max)) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for multiple in range(i * i, max, i):
                is_prime[multiple] = False

    # Extract prime numbers from the boolean array
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

def generateNextPrime(number):
    while True:
        number += 1
        if isPrime(number):
            return number
        
def primeFactorsOf(num):
    factors = []
    for r in range(2, int(math.sqrt(num)) + 1):
        if num % r == 0:
            factors.append(r)
            while num % r == 0:
                num //= r
    if num > 1:
        factors.append(num)
    return factors

# this returns a list of the digits in the given number in reverse order
# for example, 1234 returns [4,3,2,1]
def extractDigits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits

# this accepts a list of digits in reverse order and reconstructs the number
# for example, [4,3,2,1] returns 1234
def reconstructFromDigits(digits):
    number = 0
    for i in range(len(digits)):
        number += digits[i] * 10**i
    return number

def reverseNumber(num):
    digits = extractDigits(num)
    digits.reverse()
    return reconstructFromDigits(digits)

def isPalindromicNumber(num):
    digits = extractDigits(num)
    for r in range(len(digits)):
        if digits[r] != digits[-r-1]:
            return False
    return True

def nthTriangleNumber(n):
    return n*(n+1) // 2

def isTriangleNumber(num):
    n = (math.sqrt(8 * num + 1) - 1) / 2
    return n == int(n)

def nthPentagonalNumber(n):
    return (3 * n**2 - n) // 2

def isPentagonalNumber(num):
    n = (math.sqrt(24 * num + 1) + 1) / 6
    return n == int(n)

def nthHexagonalNumber(n):
    return n*(2*n - 1)

def isHexagonalNumber(num):
    n = (math.sqrt(8 * num + 1) + 1) / 4
    return n == int(n)

def wordValue(word):
    return sum([charToAlphabetValue[char] for char in word])

def nCr(n, r): # AI generated
    """Calculate n choose r (nCr) using a more efficient method."""
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    r = min(r, n - r)  # Take advantage of symmetry
    c = 1
    for i in range(r):
        c = c * (n - i) // (i + 1)
    return c
