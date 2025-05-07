# Starting with the number 1 and moving to the right in a clockwise direction a 5x5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001x1001 spiral formed in the same way?

# GRID_SIDE_LENGTH = 5
GRID_SIDE_LENGTH = 1001

numbers = [n for n in range(1, GRID_SIDE_LENGTH**2 + 1)]

index = 0
sumOfDiagonals = 1
step = 2
while True:
    try:
        for n in range(4):
            index += step
            sumOfDiagonals += numbers[index]
        step += 2
    except:
        break

print("The answer is: ", sumOfDiagonals)