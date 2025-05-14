# https://projecteuler.net/problem=38

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2,...,n) where n > 1?

from utils import extractDigits, reconstructFromDigits

MAX = 987654321
digitsSet = set(extractDigits(MAX))
MAX_DIGITS = len(digitsSet)

largest = 0
for n in range(10000): # n*1 concat n*2 is too large if n has more than 4 digits
    digits = []
    i = 1
    for i in range(1, MAX_DIGITS+1):
        newDigits = extractDigits(n * i)
        newDigits.reverse()
        digits += newDigits
        if 0 in digits or len(digits) > MAX_DIGITS:
            break
        if len(digits) == MAX_DIGITS and set(digits) == digitsSet:
            digits.reverse()
            largest = max(largest, reconstructFromDigits(digits))


print("The answer is: ", largest)
