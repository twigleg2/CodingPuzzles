# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

# gridSize = 2
gridSize = 20
memoization = {}

def traverse(xy):
    x,y = xy
    if x > gridSize or y > gridSize:
        return 0
    if xy == (gridSize,gridSize):
        return 1
    
    result = memoization.get(xy)
    if result:
        return result
    else:
        result = traverse((x + 1, y)) +  traverse((x, y + 1))
        memoization[xy] = result
        return result

answer = traverse((0,0))
print("The answer is: ", answer)