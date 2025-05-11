# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

from utils import isPalindromicNumber

MAX = 1_000_000

def reverseBits(n):
    reversed = 0
    while n > 0:
        reversed <<= 1
        if (n & 1) == 1:
            reversed |= 1
        n >>= 1
    return reversed


palindromes = []
for n in range(MAX):
    if isPalindromicNumber(n) and n == reverseBits(n):
        palindromes.append(n)


print("The answer is: ", sum(palindromes))