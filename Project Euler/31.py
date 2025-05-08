# https://projecteuler.net/problem=31

coins = [200,100,50,20,10,5,2,1]
target = 200


    # for every coin,
        # recursively add that coin to the runningTotal until it hits or exceeds the target
        # NOTE: Make sure to not add coins larger than the current coin being considered, as this will incorrectly allow for permutations to be counted as unique, when they are not
        # return 1 if target is hit
        # return 0 if target is exceeded

def makeMoney(runningTotal = 0, currentCoin = coins[0]):

    if runningTotal > target:
        return 0
    if runningTotal == target:
        return 1
    
    numWaysToMakeMoney = 0
    for c in coins:
        if c > currentCoin:
            continue
        numWaysToMakeMoney += makeMoney(runningTotal + c, c)

    return numWaysToMakeMoney



result = makeMoney()
print("The answer is: ", result)