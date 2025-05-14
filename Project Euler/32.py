# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

from utils import extractDigits

digitsSet = set(extractDigits(987654321))
MAX_DIGITS = len(digitsSet)

products = {0}


for n in range(2, 100): # n must be smaller than m, so limit n to 2 digit numbers
    nDigits = extractDigits(n)
    if 0 in nDigits:
        continue
    for m in range(n+1, 10000 // n): # m will be at most 4 digits, reduced as n grows larger
        mDigits = extractDigits(m)
        if 0 in mDigits or len(nDigits) + len(mDigits) >= MAX_DIGITS:
            continue
        product = n * m
        productDigits = extractDigits(product)
        if 0 in productDigits or len(nDigits) + len(mDigits) + len(productDigits) != MAX_DIGITS:
            continue
        if set(nDigits + mDigits + productDigits) == digitsSet:
            products.add(product)




print("The answer is: ", sum(products))