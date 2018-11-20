import numpy as np


class Deck():
    def __init__(self):
        self.deck = []
        
    def get_cards(self):
        return self.deck
    
    def show_cards(self):
        l = len(self.deck) - 1
        for x in range(l):
            print(self.deck[x].show())
    
    def create_cards(self):
        self.possible_ranks = '23456789xjqka'
        self.possible_suits = 'cdsh'
        self.rank_val = 0

        for rank in self.possible_ranks:
            self.rank_val += 1
            for suit in self.possible_suits:
                self.card = Card(rank, self.rank_val, suit)
                self.deck.append(self.card)
         
        np.random.shuffle(self.deck)
  


class Card():
    def __init__(self, rank, rank_numeric, suit):
        self.rank = rank
        self.rank_numeric = rank_numeric
        self.suit = suit

    def show(self):
        return self.rank, self.suit


