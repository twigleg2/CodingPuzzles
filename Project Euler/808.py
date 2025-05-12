# Find the sum of the first 50 reversible prime squares.


from utils import isPrime, generateNextPrime, reverseNumber, isPalindromicNumber

MAX = 50

reversiblePrimeSquares = []

prime = 0
while len(reversiblePrimeSquares) < MAX:
    prime = generateNextPrime(prime)
    primeSquared = prime**2
    reversePrimeSquared = reverseNumber(primeSquared)
    rootReversePrimeSquared = reversePrimeSquared**0.5
    if reversePrimeSquared != primeSquared and isPrime(rootReversePrimeSquared):
        reversiblePrimeSquares.append(primeSquared)
        reversiblePrimeSquares.append(reversePrimeSquared)
        prime = int(rootReversePrimeSquared)


print("The answer is:", sum(reversiblePrimeSquares))