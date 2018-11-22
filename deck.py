#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


class Card:
    # class for creating cards
    def __init__(self, rank, rank_numeric, suit, ):
        self.rank = rank
        self.rank_numeric = rank_numeric
        self.suit = suit
    
    def show_card(self):
        # returns card in string format
        return '{}{}'.format(self.rank, self.suit)

class Deck:
    # class for creating deck
    def __init__(self):
        self.deck = []
        self.table = []

    def show_deck(self):
        # returns list of deck in string format
        res = []
        for card in self.deck:
            res.append('{}{}'.format(card.rank, card.suit))
        
        return res


    def draw_card(self):
        # draws the top card of the deck and returns it
        return self.deck.pop(0)
    
    def draw_hand(self, seat):
        # draw two cards from deck to seat.hand
        seat.hand.append(self.deck.pop(0))
        seat.hand.append(self.deck.pop(0))


    def create_cards(self):
        # creating all 52 card possibilities
        self.possible_ranks = '23456789xJQKA'
        self.possible_suits = 'cdsh'
        self.rank_val = 1

        for rank in self.possible_ranks:
            # looping through letters of possible_ranks
            
            if rank == 'x':
                rank = 10
            
            for suit in self.possible_suits:
                # looping through letters of possible_suits and finally creating new card with current rank and suit
               
                self.card = Card(rank, self.rank_val, suit)
                self.deck.append(self.card)

            self.rank_val += 1

        np.random.shuffle(self.deck)


class Seat:
    # class for creating seat
    
    def __init__(self):
        self.hand = []
    
    def get_hand(self):
        # returns list of cards in hand as strings
       
        return '{}{}, {}{}'.format(self.hand[0].rank, self.hand[0].suit, self.hand[1].rank, self.hand[1].suit)


class Table:
    # class for creating table
    
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
        # return board in string format.
        # E.g:
        # >>> table.show_board()
        # returns:
        # >>> ['Jd', '8c', 'Ac', '9d', '2h']
        
        res = []
        for cards in self.board:
            res.append('{}{}'.format(cards.rank, cards.suit))
        return res


    def flop(self):
        # draw 3 top cards from deck and add to board list
        # todo:
        # - research poker rules for drawing cards, some may be supposed to be discarded and not put on board
        
        for i in range(3):
            self.board.append(self.deck.draw_card())

    def turn(self):
        # todo: ^
        
        self.board.append(self.deck.draw_card())

    def river(self):
        # todo: ^
        
        self.board.append(self.deck.draw_card())

    def eval_straight(self, hand):
        # check if board cards and hand cards makes a straight using rank_numeric in reverse order
        # todo:
        # - add check for sorted numeric ranks to check straight(highest first)
        # - add check to see if an Ace makes a straight with 2345 if no other found
        # - ? add check for straight flush ?
        # - ? add check for royal flush ? 
        
        tmp = []
        
        card_one = hand[0].rank
        print(card_one)
         
        for card in self.board:
            tmp.append(card)
        
        for card in hand:
            tmp.append(card)

        #tmp.sort()
        #tmp.reverse()
        print(tmp)
      
        for x in tmp:
            format_it = '{}{} {}{} {}{} {}{} {}{}'.format(tmp[x].rank, tmp[x].suit, tmp[x+1].rank, tmp[x+1].suit, 
                    tmp[x+2].rank, tmp[x+2].suit, tmp[x+3].rank, tmp[x+3].suit, tmp[x+4].rank, tmp[x+4].suit)

            if (tmp[x.rank_numeric] == tmp[x.rank_numeric + 1] + 1 
            and tmp[x.rank_numeric + 1] == tmp[x.rank_numeric + 2] + 1 
            and tmp[x.rank_numeric + 2] == tmp[x.rank_numeric + 3] + 1 
            and tmp[x.rank_numeric + 3] == tmp[x.rank_numeric + 4] + 1):
            
                  
                print('STRAIGHT FOUND:')
                print()
    
                        
    
    def eval_equals(self, hand):
        
        # check if hand and board contains same ranked cards and returns amount of matches found in "poker terms"
        # todo:
        # - add check for pairs not connected to player hand
        # - add check for pair in hand
        # - add return pair value

        show = self.show_board()
        
        # match rank of card one in hand with rank of cards on the board
        match_one = [x for x in show if str(hand[0].rank) in str(x)]

        # match rank of card two in hand with rank of cards on the board
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



