# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
# difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# MAX_NUM = 10
MAX_NUM = 100

sumOfSquares = 0
squareOfSum = 0

for i in range(MAX_NUM + 1):
    sumOfSquares += i**2
    squareOfSum += i

squareOfSum **= 2
print("sumOfSquares: ", sumOfSquares)
print("squareOfSum: ", squareOfSum)

print("The answer is: ", squareOfSum - sumOfSquares)