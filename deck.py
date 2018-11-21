#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import re


class Card:

    def __init__(self, rank, rank_numeric, suit, ):
        self.rank = rank
        self.rank_numeric = rank_numeric
        self.suit = suit
    
    def show_card(self):
        return '{}{}'.format(self.rank, self.suit)

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
                self.deck.append(self.card.show_card())

            self.rank_val += 1

        np.random.shuffle(self.deck)


class Seat:
    def __init__(self):
        self.hand = []

    def show_hand(self):
        return self.hand[0], self.hand[1]


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

               
    def flop(self):
        for i in range(3):
            self.board.append(self.deck.draw_card())

    def turn(self):
        self.board.append(self.deck.draw_card())

    def river(self):
        self.board.append(self.deck.draw_card())


    def eval_equals(self, hand):
        
        # check if hand and board contains same ranked cards and returns amount of matches found in "poker terms"
        # -- currently doesn't work. idk.
        # -- this also probably won't be very effective with evaluating full house
        r = re.compile('.' + hand[0][0])
        rr = re.compile('.' + hand[1][0])
        d = len(list(filter(r.match, self.board)))
        dd = len(list(filter(rr.match, self.board)))
        if d or dd:
            if d == 4 or dd == 4:
                return 'quads'
            elif d == 3 or dd == 3:
                return 'trips'
            elif d == 2 or dd == 2:
                return 'dubs'
        
      




