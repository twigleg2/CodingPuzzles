# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3+3+5+4+4 = 19 letters used in total.
# If all the numbers from 1 to 1,000 (one thousand) inclusive were written out in words, how many letters would be used?

dict = {
    0: 0, # used in 10, 20, etc.
    1: 3, # one
    2: 3, # two
    3: 5, # three
    4: 4, # four
    5: 4, # five
    6: 3, # six
    7: 5, # seven
    8: 5, # eight
    9: 4, # nine
    10: 3, # ten
    11: 6, # eleven
    12: 6, # twelve
    13: 8, # thirteen
    14: 8, # fourteen
    15: 7, # fifteen
    16: 7, # sixteen
    17: 9, # seventeen
    18: 8, # eighteen
    19: 8, # nineteen
    20: 6, # twenty
    30: 6, # thirty
    40: 5, # forty
    50: 5, # fifty
    60: 5, # sixty
    70: 7, # seventy
    80: 6, # eighty
    90: 6, # ninety
    100: 10, # hundred and
    'and': 3, # and
    1000: 8 # thousand
}

MAX = 1000
# MAX = 5

totalLetters = 0
for n in range(1, MAX + 1):
    ones = n % 10
    n //= 10
    tens = n % 10
    n //= 10
    hundreds = n % 10
    n //= 10
    thousands = n % 10

    if tens == 1:
        totalLetters += dict[10 + ones]
    else:
        totalLetters += dict[10 * tens] + dict[ones]
    
    if hundreds:
        totalLetters += dict[hundreds] + dict[100]
        if ones == 0 and tens == 0:
            totalLetters -= dict['and']

    if thousands:
        totalLetters += dict[thousands] + dict[1000]

print("The answer is: ", totalLetters)
    