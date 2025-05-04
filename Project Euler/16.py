# 2^15 = 32768 and the sum of the digits is 3+2+7+6+8 = 16
# What is the sum of the digits in the number 2^1000?

number = 2**1000

sum = 0
while number > 0:
    sum += number % 10
    number//=10

print("The answer is: ", sum)