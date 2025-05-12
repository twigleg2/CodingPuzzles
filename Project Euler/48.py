# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


from utils import extractDigits, reconstructFromDigits

MAX = 1000
NUM_DIGITS = 10

total = 0
for i in range(1, MAX+1):
    total += i**i

digits = extractDigits(total)
lastTenDigits = digits[:NUM_DIGITS]
answer = reconstructFromDigits(lastTenDigits)
print("The answer is: ", answer)