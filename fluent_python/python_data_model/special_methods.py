"""
A Pythonic Card Deck

By implementing the special methods __len__ and __getitem__, our FrenchDeck behaves
like a standard Python sequence, allowing it to benefit from core languages features
(e.g. iteration and slicing) and from the standard library, as shown by the examples
using random.choice, reversed and sorted. Thanks to composition, the __len__ and
__getitem__ implementations can delegate all the work to a list object, self._cards.

"""
import collections

from random import choice


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [
            Card(rank, suit)
            for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card("7", "diamonds")
print(beer_card)

# special class method __len__
# read len of french deck
deck = FrenchDeck()
print(len(deck))

# special class method __getitem__
# get specific cards from deck
print(deck[0])

# pick random card
print(choice(deck))

# slicing
print(deck[:3])

# iterate deck
print("** iterate **")
for card in deck:
    print(card)

# iterate deck in reverse
print("** iterate reverse **")
for card in reversed(deck):
    print(card)

# sorting
print("** sorting **")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
