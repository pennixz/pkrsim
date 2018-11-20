import numpy as np


class Table():
    def __init__(self):
        self.max_seats = 8
        self.deck = None
        



class Deck():
    def __init__(self, table):
        self.table.deck = []
        

    def create_cards(self):
        self.possible_ranks = '23456789xjqka'
        self.possible_suits = 'cdsh'
        self.rank_val = 0

        for rank in possible_ranks:
            self.rank_val += 1
            for suit in possible_suits:
                self.card = Card(rank, self.rank_val, suit)
                self.table.deck.append(self.card)

        np.random.shuffle(self.deck)
            


class Card():
    def __init__(self, rank, rank_numeric, suit):
        self.rank = rank
        self.rank_numeric = rank_numeric
        self.suit = suit


