import random

from Card import Card

class Deck:

    def __init__(self):

        self.suits = ("Diamonds", "Clubs", "Hearts", "Spades")

        self.ranks = ("Two", "Three", "Four", "Five", "Six",
                    "Seven", "Eight", "Nine", "Ten", "Jack",
                    "Queen", "King", "Ace")

        self.deck = []

        for the_suit in self.suits:

            for the_rank in self.ranks:

                self.deck.append(Card(the_suit, the_rank))

    def shuffle_deck(self):

        random.shuffle(self.deck)

    def __str__(self):

        deck_contents = ""

        for card in self.deck:

            deck_contents += "\n" + card.__str__()

        return deck_contents

    def deal_card(self):

        dealt_card = self.deck.pop()

        return dealt_card