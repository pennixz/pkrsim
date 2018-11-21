#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from unicards import unicard


class Card:

    def __init__(self, rank, rank_numeric, suit, ):
        self.rank = rank
        self.rank_numeric = rank_numeric
        self.suit = suit


class Deck:

    def __init__(self):
        self.deck = []
        self.table = []

    def show_deck(self):
        for card in self.deck:
            print(unicard('{}{}'.format(card.rank, card.suit)))

    def show_table(self):
        for card in self.table:
            print('{}{}'.format(card.rank, card.suit))

    def draw_card(self):
        self.table.append(self.deck.pop(0))

    def create_cards(self):
        self.possible_ranks = '23456789xJQKA'
        self.possible_suits = 'cdsh'
        self.rank_val = 1

        for rank in self.possible_ranks:
            if rank == 'x':
                rank = 10
            for suit in self.possible_suits:
                self.card = Card(rank, self.rank_val, suit)
                self.deck.append(self.card)

            self.rank_val += 1

        np.random.shuffle(self.deck)
