# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers

numbers = []
file = open("13.txt", "r")
for line in file:
    value = int(line.strip())
    numbers.append(value)

NUM_DIGITS = 10
target = 0
for i in range(0, NUM_DIGITS):
    target += 9 * 10**i

sum = sum(numbers)
while sum > target:
    print(sum)
    sum //= 10

print("The answer is: ", sum)