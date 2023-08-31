from itertools import product

# lists the suits and ranks
Suits = ["♠", "♥", "♣", "♦"]
Ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
Values = {
    "A": [1,11],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}
    

deck = list(product(Ranks, Suits))  # creates a list of tuples of the cards

# Tests if the deck has been made
print(deck)
print(Values)