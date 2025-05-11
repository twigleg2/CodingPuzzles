# How many circular primes are there below one million?

from utils import generatePrimesUnder
from utils import extractDigits
from utils import reconstructFromDigits

MAX = 1_000_000


primes = generatePrimesUnder(MAX)

count = 0
for p in primes:
    isCircularPrime = True
    digits = extractDigits(p)
    for i in range(len(digits)):
        number = reconstructFromDigits(digits[-i:] + digits[:-i])
        if not number in primes:
            isCircularPrime = False
            break
    if isCircularPrime:
        count += 1

print("The answer is: ", count)