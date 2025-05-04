# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?
import math

# gridSize = 2
gridSize = 20
n = gridSize * 2
k = gridSize

def n_choose_k(n,k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))

answer = n_choose_k(n,k)
print("The answer is: ", answer)