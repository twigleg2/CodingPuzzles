# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product of abc

tripletSum = 1000

def isTriplet(a,b,c):
    return (a**2 + b**2) == c**2

def findTriplet(tripletSum):
    a = 0
    b = 0
    c = tripletSum

    while a < c:
        a += 1
        b = a+1
        c = tripletSum - a - b
        while b < c:
            if isTriplet(a,b,c):
                return (a,b,c)
            b += 1
            c -= 1

triplet = findTriplet(tripletSum)
print("The answer is: ", triplet[0] * triplet[1] * triplet[2])