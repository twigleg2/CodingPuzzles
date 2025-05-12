# Find the first four consecutive integers to have four distinct prime factors each
# What is the first of these numbers?

from utils import primeFactorsOf

NumUniquePrimeFactors = 4
consecutiveLength = NumUniquePrimeFactors

n = 0
consecutive = False
while not consecutive:
    n += 1
    consecutive = True
    for i in range(consecutiveLength):
        if len(set(primeFactorsOf(n + i))) != NumUniquePrimeFactors:
            consecutive = False
            break


print("The answer is: ", n)