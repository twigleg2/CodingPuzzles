# find the last 10 digits of 28433 * 2^7830457 + 1

NUM_DIGITS = 10
POWER = 7830457
NUM = 28433


powerOfTwo = 1
for i in range(POWER):
    powerOfTwo *= 2
    powerOfTwo %= 10**NUM_DIGITS

print("The answer is: ", 28433 * powerOfTwo % 10**NUM_DIGITS + 1)