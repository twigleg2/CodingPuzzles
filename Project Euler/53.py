# How many, not necessarily distinct, values of nCr for 1 <= n <= 100, are greater than one-million?


from utils import nCr


TARGET = 1_000_000
MAX_N = 100

count = 0
for n in range(1, MAX_N + 1):
    for r in range(1, n + 1):
        if nCr(n, r) > TARGET:
            count += 1

print("The answer is: ", count)