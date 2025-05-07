# Find the sum of all the primes below two million.

from utils import isPrime
MAX = 2_000_000

primes = []
for r in range(2, MAX):
    if isPrime(r):
        primes.append(r)


print("The answer is: ", sum(primes))