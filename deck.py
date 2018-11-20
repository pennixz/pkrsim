import numpy as np


class Table(self):
    def __init__(self):
        self.max_seats = 8
        self.deck = None
        
        

class Deck(self):
    def __init__(self):
        self.deck = []
    
    def create_cards(self):
        self.possible_ranks = '23456789jqka'
        self.possible_suits = 'cdsh'
        self.rank_val = 0
        
        for rank in possible_ranks:
        self.rank_val += 1
            for suit in possible_suits:
                self.card = Card(rank, self.rank_val, suit)
                self.deck.append(self.card)
        
        np.random.shuffle(self.deck)


class Card(self):
    def __init__(self, rank, rank_numeric, suit):
        self.rank = rank
        self.rank_numeric = rank_numeric
        self.suit = suit


