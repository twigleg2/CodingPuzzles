# https://projecteuler.net/problem=54


RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SUITS = ['C', 'D', 'H', 'S']

fileName = "54.txt"
with open(fileName) as f:
    hands = f.readlines()
    hands = [hand.strip() for hand in hands]
    hands = [hand.split(" ") for hand in hands]
    hands = map(lambda hand: [hand[:5], hand[5:]], hands)
    hands = list(hands)
    
    
print("hands", hands)