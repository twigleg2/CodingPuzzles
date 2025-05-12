# find the pair of pentagonal numbers for which their sum and difference are pentagonal AND the difference between the two pentagonal numbers is minimised
# What is the difference between the pair of pentagonal numbers?


from utils import isPentagonalNumber, nthPentagonalNumber

MAX = 10_000 # this is arbitrary and might need to change
pentagonalNumbers = [nthPentagonalNumber(n) for n in range(1, MAX)]


for j in range(1, MAX):
    pentagonalNumberJ = pentagonalNumbers[j]
    for k in range(j):
        pentagonalNumberK = pentagonalNumbers[k]
        if isPentagonalNumber(pentagonalNumberJ - pentagonalNumberK) and isPentagonalNumber(pentagonalNumberJ + pentagonalNumberK):
            print("The answer is: ", pentagonalNumberJ - pentagonalNumberK)
            exit(0)
