# https://projecteuler.net/problem=22

# Names scores
# Sort the names alphabetically and then calculate the score for each name by m ultiplying its position in the list with the sum of the alphabetical values of its letters.
# The alphabetical value of a letter is its position in the alphabet (A=1, B=2, ..., Z=26).

from utils import wordValue


fileName =  "22.txt"
with open(fileName, "r") as file:
    names = file.read().replace('"', '').split(',')
names.sort()

for i in range(len(names)):
    nameValue = wordValue(names[i])
    names[i] = (i + 1) * nameValue

sum = sum(names)
print("The answer is: ", sum)