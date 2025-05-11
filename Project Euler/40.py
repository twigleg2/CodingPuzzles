# An irrational decimal fraction is created by concatenating the positive integers from 1 to infinity:
#   0.1234567891011121314151617181920212223...
# The 12th digit of the fractional part is 1
# find the product of the 1st, 10th, 100th, 1,000th, 10,000th, 100,000th and 1,000,000th digits

from utils import extractDigits

MAX = 1_000_000

digits = [0]
n = 1
while len(digits) < MAX+1:
    arr = extractDigits(n)[::-1]
    for item in arr:
        digits.append(item)
    n += 1

product = 1
for i in range(len(extractDigits(MAX))):
    product *= digits[10**i]


print("The answer is: ", product)