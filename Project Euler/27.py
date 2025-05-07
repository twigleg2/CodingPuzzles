# https://projecteuler.net/problem=27

# Considering quadratics of the form:

# n**2 + an + b, where |a| < 1000 and |b| <= 1000

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

MAX = 1000

from utils import isPrime

def quadratic(n,a,b):
    return n**2 + a*n + b

longestPrimeChain = 0
coefficients = (0,0)
    
for a in range(-1*MAX + 1, MAX):
    for b in range(-1*MAX, MAX + 1):
        n = 0
        while True:
            result = quadratic(n,a,b)
            if not isPrime(result):
                break
            n += 1
        if n > longestPrimeChain:
            longestPrimeChain = n
            coefficients = (a,b)


product = coefficients[0] * coefficients[1]
print("The answer is: ", product)