# https://projecteuler.net/problem=43


from itertools import permutations  
from utils import reconstructFromDigits


PANDIGITAL_SET = [0,1,2,3,4,5,6,7,8,9]
PANDIGITAL_PERMUTATIONS = permutations(PANDIGITAL_SET)
DIVISORS = [2,3,5,7,11,13,17]

def reverseDigits(digits):
    digits = digits
    digits.reverse()
    return digits

specialPandigitalNumbers = []
for permutation in PANDIGITAL_PERMUTATIONS:
    permutation = list(permutation)
    isSpecialPermutation = True
    for startingDigit in range (1,8):
        subNum = reconstructFromDigits(reverseDigits(permutation[startingDigit:startingDigit+3]))
        divisor = DIVISORS[startingDigit-1]
        if subNum % divisor != 0:
            isSpecialPermutation = False
            break
    if isSpecialPermutation:
        specialPandigitalNumbers.append(reconstructFromDigits(reverseDigits(permutation)))

print('The answer is: ', sum(specialPandigitalNumbers))
