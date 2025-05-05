# Problem 23: Non-abundant sums

# An abundant number is a number for which the sum of its proper divisors is greater than the number itself.
# The smallest abundant number is 12, and it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# Find the sum of all positive integers which cannot be written as the sum of two abundant numbers.

MAX = 28123

def sumDivisors(n):
    """Returns the sum of proper divisors of n."""
    if n < 2:
        return 0
    total = 1  # 1 is a proper divisor of all integers > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Avoid adding the square root twice
                total += n // i
    return total
# change next line to be a dictionary
numberToSumOfDivisors = {i: sumDivisors(i) for i in range(1, MAX+1)}
abundantNumbers = [i for i in range(1, MAX+1) if numberToSumOfDivisors[i] > i]

def isSumOfTwoAbundantNumbers(n):
    """Returns True if n can be written as the sum of two abundant numbers."""
    for i in range(len(abundantNumbers)):
        if abundantNumbers[i] >= n:
            break
        if (n - abundantNumbers[i]) in abundantNumbers:
            return True
    return False

intsWhichAreNotSumsOfTwoAbundantNumbers = []
for i in range(1, MAX+1):
    if not isSumOfTwoAbundantNumbers(i):
        intsWhichAreNotSumsOfTwoAbundantNumbers.append(i)


sum = sum(intsWhichAreNotSumsOfTwoAbundantNumbers)
print("The answer is: ", sum)