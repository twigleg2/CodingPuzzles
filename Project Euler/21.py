# https://projecteuler.net/problem=21

# Amicable numbers

def sumDivisors(n):
    """Returns the sum of proper divisors of n."""
    divisors = [1]  # 1 is a proper divisor of all integers > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid adding the square root twice
                divisors.append(n // i)
    return sum(divisors)

numbersToDivisorSums = {}
for i in range(1, 10000):
    numbersToDivisorSums[i] = sumDivisors(i)

amicableNumbers = set()
for i in range(1, 10000):
    if i not in amicableNumbers:
        a = numbersToDivisorSums[i]
        if a in numbersToDivisorSums:
            b = numbersToDivisorSums[a]
        if a != b and b == i:
            amicableNumbers.add(i)
            amicableNumbers.add(a)  

print("The answer is: ", sum(amicableNumbers))