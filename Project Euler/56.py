# Considering natural numbers of the form, a**b, where a,b < 100, what is the maximum digital sum?


from utils import extractDigits


MAX = 100

maxDigitSum = 0
for a in range(1, MAX):
    for b in range(1, MAX):
        digits = extractDigits(a**b)
        digitSum = sum(digits)
        if digitSum > maxDigitSum:
            maxDigitSum = digitSum

print("The answer is: ", maxDigitSum)