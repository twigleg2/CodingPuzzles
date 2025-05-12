# https://projecteuler.net/problem=42
# Similar to problem 22

# How many words in the gievn file are triangle words?

from utils import isTriangleNumber
from utils import wordValue


fileName = "42.txt"
with open(fileName, "r") as file:
    names = file.read().replace('"', '').split(',')

wordValues = [wordValue(name) for name in names]
triangleWords = [word for word in wordValues if isTriangleNumber(word)]

print(f"Number of triangle words: {len(triangleWords)}")