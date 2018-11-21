#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


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
        res = []
        for card in self.jeck:
            res.append('{}{}'.format(card.rank, card.suit))
        
        return res

    def show_table(self):
        res = []
        for card in self.table:
            res.append('{}{}'.format(card.rank, card.suit))
        
        return res

    def draw_card(self):
        return self.deck.pop(0)
    
    def draw_hand(self, seat):
        c1 = self.deck.pop(0)
        c2 = self.deck.pop(0)
        seat.hand = [c1, c2]

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


class Seat:
    def __init__(self):
        self.hand = []

    def show_hand(self):
        return '{}{}, {}{}'.format(self.hand[0].rank, 
                self.hand[0].suit, self.hand[1].rank,
                self.hand[1].suit)


class Table:

    def __init__(self, deck):
        self.deck = deck
        self.seats = 6
        self.board = []
        self.seat1 = Seat()
        self.seat2 = Seat()
        self.seat3 = Seat()
        self.seat4 = Seat()
        self.seat5 = Seat()
        self.seat6 = Seat()

               

    def evaluate(hand):
        # comparing hand to board cards
        # 
        # check royal flush > straight flush > FOAK >
        # full house > flush > straight > three of a kind >
        # two pair > one pair > high card
        self.temp_val = 0




