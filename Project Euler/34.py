# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

from utils import extractDigits
import math

MAX = 100_000

specialNumbers = []
for n in range(3, MAX):
    digits = extractDigits(n)
    total = 0
    for d in digits:
        total += math.factorial(d)
    if total == n:
        specialNumbers.append(n)

result = sum(specialNumbers)
print("The answer is: ", result)

