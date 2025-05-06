# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# MAX = 3
MAX = 1_000

def numberOfDigits(n):
    numDigits = 1
    while n > 9:
        numDigits += 1
        n = n//10
    return numDigits


count = 2
RecentFibNums = (1, 1)
while numberOfDigits(RecentFibNums[0]) < MAX:
    count +=1
    RecentFibNums = (RecentFibNums[0]+ RecentFibNums[1], RecentFibNums[0] )


print("The answer is: ", count)