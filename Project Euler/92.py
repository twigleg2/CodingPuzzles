# https://projecteuler.net/problem=92

from utils import extractDigits

MAX = 10_000_000

def squareDigitsThenAdd(num):
    digits = extractDigits(num)
    return sum(d**2 for d in digits)


numberToTerminator = {1: 1, 89: 89}

count = 0
nextInChain = 0
terminator = 0
for n in range (1, MAX):
    nextInChain = n
    chain = [n]
    while True:
        if nextInChain in numberToTerminator:
            terminator = numberToTerminator[nextInChain]
            break
        else:
            nextInChain = squareDigitsThenAdd(nextInChain)
            chain.append(nextInChain)
    
    for c in chain:
        numberToTerminator[c] = terminator
    if terminator == 89:
        count += 1

print("The answer is:", count)