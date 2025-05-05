# NOTE: See Problem 18 for description

# fileName = "18.txt"
fileName = "67.txt"

triangle = []
file = open(fileName, "r")
for line in file:
    values = line.strip().split()
    ints = [int(value) for value in values]
    triangle.append(ints)

memoization = {}

def recursiveAdd(rc):
    r,c = rc
    
    if r >= len(triangle) or c >= len(triangle[r]):
        return 0
    if r == len(triangle)-1:
        return triangle[r][c]

    result = memoization.get(rc)
    if result:
        return result
    else:
        resultLeft = triangle[r][c] + recursiveAdd((r+1, c))
        resultRight = triangle[r][c] + recursiveAdd((r+1, c+1))
        memoization[rc] = resultLeft if resultLeft > resultRight else resultRight

        return memoization[rc]

answer = recursiveAdd((0,0))
print("The answer is: ", answer)