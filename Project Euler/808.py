# Find the sum of the first 50 reversible prime squares.

import math
from utils import isPrime, generatePrimesUnder, reverseNumber

PRIME_CEILING = 10**8
TARGET_NUMBER_OF_PRIMES = 50

primes = generatePrimesUnder(PRIME_CEILING)

reversiblePrimeSquares = []

primeIndex = 0
while len(reversiblePrimeSquares) < TARGET_NUMBER_OF_PRIMES:
    prime = primes[primeIndex]
    primeSquared = prime**2
    reversePrimeSquared = reverseNumber(primeSquared)
    rootReversePrimeSquared = math.sqrt(reversePrimeSquared)
    if not rootReversePrimeSquared.is_integer(): # if a perfect square
        continue
    if reversePrimeSquared != primeSquared and isPrime(rootReversePrimeSquared): # if not a palindrome and is prime
        reversiblePrimeSquares.append(primeSquared)
        reversiblePrimeSquares.append(reversePrimeSquared)
    primeIndex += 1

print("The first 50 reversible prime squares are: ", reversiblePrimeSquares)
print("The answer is:", sum(reversiblePrimeSquares))