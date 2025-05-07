# https://projecteuler.net/problem=29


MIN = 2
MAX = 100

numbers = set()

for a in range(MIN, MAX+1):
    for b in range(MIN, MAX+1):
        numbers.add(a**b)

print("The answer is: ", len(numbers))