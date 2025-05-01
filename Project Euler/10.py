# Find the sum of all the primes below two million.

import math
MAX = 2_000_000

def isPrime(num):
    for r in range(2, math.floor(math.sqrt(num)) + 1):
        if num % r == 0:
            return False
    return True

primes = []
for r in range(2, MAX):
    if isPrime(r):
        primes.append(r)


print("The answer is: ", sum(primes))