#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


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
        for card in self.deck:
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
        seat.hand.append(self.deck.pop(0))
        seat.hand.append(self.deck.pop(0))


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

    def get_hand(self):
        return '{}{}, {}{}'.format(self.hand[0].rank, self.hand[0].suit, self.hand[1].rank, self.hand[1].suit)


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

    def show_board(self):
        res = []
        for cards in self.board:
            res.append('{}{}'.format(cards.rank, cards.suit))
        return res


    def flop(self):
        for i in range(3):
            self.board.append(self.deck.draw_card())

    def turn(self):
        self.board.append(self.deck.draw_card())

    def river(self):
        self.board.append(self.deck.draw_card())

    def eval_straight(self, hand):
        self.dm = 0     

    def eval_equals(self, hand):
        
        # check if hand and board contains same ranked cards and returns amount of matches found in "poker terms"
        # todo:
        # - add check for pairs not connected to player hand
        
        show = self.show_board()
        match_one = [x for x in show if str(hand[0].rank) in str(x)] 
        match_two = [x for x in show if str(hand[1].rank) in str(x)]
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
                val = match_one[0][0] + match_one[0][0]
                print('dub value: {}!'.format(val))

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
                val = match_two[0][0] + match_one[0][0]
                print('dub value: {}!'.format(val))



