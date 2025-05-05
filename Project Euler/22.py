# https://projecteuler.net/problem=22

# Names scores
# Sort the names alphabetically and then calculate the score for each name by m ultiplying its position in the list with the sum of the alphabetical values of its letters.
# The alphabetical value of a letter is its position in the alphabet (A=1, B=2, ..., Z=26).


fileName =  "22.txt"
with open(fileName, "r") as file:
    names = file.read().replace('"', '').split(',')
names.sort()

alphabetValue = {chr(i): i - 64 for i in range(65, 91)}  # A=1, B=2, ..., Z=26


for i in range(len(names)):
    nameValue = sum(alphabetValue[char] for char in names[i])
    names[i] = (i + 1) * nameValue

sum = sum(names)
print("The answer is: ", sum)