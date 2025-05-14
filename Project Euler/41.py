# What is the largest n-digit pandigital prime that exists?

from itertools import permutations
from utils import isPrime

pandigitalSet = [1,2,3,4,5,6,7,8,9]

largestPandigitalPrime = 0
for i in range(len(pandigitalSet)):
    pandigitalPermutations = permutations(pandigitalSet)
    for permutation in pandigitalPermutations:
        permutation = int(''.join(map(str, permutation)))
        if isPrime(permutation):
            largestPandigitalPrime = max(largestPandigitalPrime, permutation)
    pandigitalSet.pop()

print("The answer is: ", largestPandigitalPrime)