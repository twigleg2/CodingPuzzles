# Find the value of d < 1000  for which 1/d contains the longest recurring cycle in its decimal fraction part.

MAX = 1000

def longDivision(num, div):
    digits = []
    remainders = []
    while True:
        digits.append(num // div)
        r = num % div
        if r == 0:
            break
        if r in remainders:
            return len(remainders)
        remainders.append(r)
        num = remainders[-1] * 10
    
    return 0


longestChain = 0
value = 0
for d in range(2,MAX):
    chainLength = longDivision(1,d)
    if chainLength > longestChain:
        longestChain = chainLength
        value = d

print(f"The number {value} has the longest repeating section, with length {longestChain}")