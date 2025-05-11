# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

from utils import extractDigits

MAX = 987654321
digits = extractDigits(MAX)

products = {0}

def containsDuplicates(list):
    return len(list) != len(set(list))


numbersToDigits = {}

def getDigits(num):
    d = numbersToDigits.get(num)
    if d:
        return d
    numbersToDigits[num] = extractDigits(num)
    return numbersToDigits.get(num)


for n in range(39, int(MAX**0.5)):
    nDigits = getDigits(n)
    if 0 in nDigits:
        continue
    for m in range(n+1, MAX):
        product = n * m
        usedDigits = nDigits + getDigits(m) + getDigits(product)
        if 0 in usedDigits:
            continue
        if len(usedDigits) == 9 and not containsDuplicates(usedDigits):
            print(f"{n} x {m} = {product}")
            products.add(product)




print("The answer is: ", sum(products))