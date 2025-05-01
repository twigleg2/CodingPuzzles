# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10  without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

MAX_DIVISOR = 20
num = 2520

def modAll(num, MAX_DIVISOR):
    for i in range (2, MAX_DIVISOR+1):
        if num % i != 0:
            return False
    return True

while modAll(num, MAX_DIVISOR) != True:
    num += 2 # skip all odd numbers

print("The answer is: ", num)