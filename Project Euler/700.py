# https://projecteuler.net/problem=700
# Find the sum of all Eulercoins.

MAX = 1_000_000_000 # not large enough, but larger is too slow.  need a trick.


euleroins = [1504170715041707]

def eulercoinEquation(n):
    return 1504170715041707 * n % 4503599627370517

for n in range(1, MAX+1):
    next = eulercoinEquation(n)
    if next < euleroins[-1]:
        euleroins.append(next)

print("The answer is:", sum(euleroins))