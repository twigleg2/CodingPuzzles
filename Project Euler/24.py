# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

MAX = 1_000_000
permutations = [''] * MAX
startingString = '0123456789'
# startingString = '012'

def getPermutations(s):
    if len(s) == 1:
        return s[0]
    permutations = []
    for i in range(len(s)):
        c = s[i]
        remaining = s[:i] + s[i+1:]
        results = getPermutations(remaining)
        for p in results:
            permutations.append(c + p)

    return permutations
    

permutations = getPermutations(startingString)

print("The answer is: ", permutations[MAX-1])