# How many Lychrel numbers are there below ten-thousand?



from utils import isPalindromicNumber, reverseNumber

MAX = 10_000
N = 50

count = 0
for n in range(1, MAX + 1):
    for i in range(N):
        n += reverseNumber(n)
        if isPalindromicNumber(n):
            count += 1
            break


print("The answer is:", MAX - count)