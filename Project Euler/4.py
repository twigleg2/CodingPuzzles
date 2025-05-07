# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers.

from utils import extractDigits

def isPalindromicNumber(num):
    digits = extractDigits(num)
    
    for r in range(len(digits)):
        if digits[r] != digits[-r-1]:
            return False
    
    return True

palindrome = 0

x = 999
y = 999
for i in range(x, 0, -1):
    for j in range(y, 0, -1):
        product = i * j
        if isPalindromicNumber(product):
            if product > palindrome:
                palindrome = product


print("The answer is: ", palindrome)