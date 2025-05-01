# By listing the first six prime numbers: 2,3,5,7,11,13, we can see that the 6th prime is 13.
# what is the 10,001st prime number?

import math

# targetPrime = 6
targetPrime = 10_001

def isPrime(num):
    for r in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % r == 0:
            return False
    
    return True


primes = [2]
# primes = [2,3,5,7,11,13]
num = primes[-1] + 1
while len(primes) < targetPrime:
    if isPrime(num):
        primes.append(num)
    num += 1


print("The answer is: ", primes[-1])
