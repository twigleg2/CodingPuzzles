

MAX = 1_000_000
# MAX = 14
longestChain = 1
collatzNumber = 1
for n in range(1, MAX):
    currentChainLength = 1
    startingNumber = n
    while n > 1:
        # print(n)
        if n % 2 == 0:
            n = n//2
        else:
            n = (n*3) + 1
        currentChainLength += 1

    if currentChainLength > longestChain:
        longestChain = currentChainLength
        collatzNumber = startingNumber


print("The Longest Chain is: ", longestChain)
print("From the starting number: ", collatzNumber)