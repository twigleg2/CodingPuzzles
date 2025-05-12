# Find the next triangle number (above T_285 = 40755) that is also pentagonal and hexagonal.


from utils import nthTriangleNumber, isPentagonalNumber, isHexagonalNumber

n = 286
while True:
    nextTriangleNumber = nthTriangleNumber(n)
    if isPentagonalNumber(nextTriangleNumber) and isHexagonalNumber(nextTriangleNumber):
        break
    n += 1
        
        
print("The answer is: ", nextTriangleNumber)