# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2,3,5,7 are not considered to be truncatable primes.

from utils import generateNextPrime
from utils import isPrime
from utils import extractDigits
from utils import reconstructFromDigits


def isTruncatable(n):
    digits = extractDigits(n)
    for i in range(1, len(digits)):
        if not isPrime(reconstructFromDigits(digits[i:])):
            return False
        if not isPrime(reconstructFromDigits(digits[:-i])):
            return False
    return True

specialPrimes = []
n = 7
while len(specialPrimes) < 11:
    n = generateNextPrime(n)
    if isTruncatable(n):
        specialPrimes.append(n)


print("The answer is: ", sum(specialPrimes))