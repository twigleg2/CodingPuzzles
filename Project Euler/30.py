

from utils import extractDigits

MAX = 1_000_000
POWER = 5

specialNumbers = []
for n in range(2, MAX):
    digits = extractDigits(n)
    total = 0
    for d in digits:
        total += d**POWER
    if total == n:
        specialNumbers.append(n)

result = sum(specialNumbers)
print("The answer is: ", result)