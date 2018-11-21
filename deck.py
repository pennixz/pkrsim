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
        # todo:
        # - add check for pairs not connected to player hand

        match_one = [x for x in self.board if hand[0][0] in x] 
        match_two = [x for x in self.board if hand[1][0] in x]
        total_matches = len(match_one) + len(match_two)
        if match_one:
            if len(match_one) == 4:
                print('QUADS!')
                print(match_one)
            elif len(match_one) == 3:
                print('TRIPS')
                print(match_one)
            elif len(match_one) == 2:
                print('DUBS')
                print(match_one)

        if match_two:
            if len(match_two) == 4:
                print('QUADS!')
                print(match_two)
            elif len(match_two) == 3:
                print('TRIPS')
                print(match_two)
            elif len(match_two) == 2:
                print('DUBS')
                print(match_two)



