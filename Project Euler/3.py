# What is the largest prime factor of the number 600851475143?

# num = 13195
num = 600851475143
divisor = 2
primes = []
while num >= divisor:
    if num % divisor == 0:
        primes.append(divisor)
        num = num / divisor
    else:
        divisor += 1

print("The answer is: ", primes[-1])