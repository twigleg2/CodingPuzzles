# In the 20 x 20 grid, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 x 63 x 78 x 14 = 1788696
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 x 20 grid?

grid = []
file = open("11.txt", "r")
for line in file:
    values = line.strip().split()
    ints = [int(value) for value in values]
    grid.append(ints)

ADJ_LEN = 4
largestProduct = 0

numRows = len(grid)
numCols = len(grid[0])

directions = [(1,0),(0,1),(1,1),(1,-1)]

for r in range(numRows):
    for c in range(numCols):
        for dir in directions:
            prod = 1
            for k in range(ADJ_LEN): # TODO: check out of bounds
                try:
                    prod *= grid[r + dir[1]*k][c + dir[0]*k]
                    if prod > largestProduct:
                        largestProduct = prod
                except:
                    pass


print("The answer is: ", largestProduct)