#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


class Card:
    # class for creating cards
    def __init__(self, rank, rank_numeric, suit, ):
        self.rank = rank, rank_numeric
        self.suit = suit

    def show_card(self):
        # returns card in string format
        return '{}{}'.format(self.rank[0], self.suit)


class Deck:
    # class for creating deck
    def __init__(self):
        self.deck = []
        self.table = []
        self.possible_ranks = '23456789xJQKA'
        self.possible_suits = 'cdsh'
        self.rank_val = 1

    def show_deck(self):
        # returns list of deck in string format
        res = []
        for card in self.deck:
            res.append('{}{}'.format(card.rank[0], card.suit))

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
        for rank in self.possible_ranks:
            # looping through letters of possible_ranks

            if rank == 'x':
                rank = 10

            for suit in self.possible_suits:
                # looping through letters of possible_suits and finally creating new card with current rank and suit

                card = Card(rank, self.rank_val, suit)
                self.deck.append(card)

            self.rank_val += 1

        np.random.shuffle(self.deck)


class Seat:
    # class for creating seat

    def __init__(self):
        self.hand = []

    def get_hand(self):
        # returns list of cards in hand as strings

        return '{}{}, {}{}'.format(self.hand[0].rank[0], self.hand[0].suit, self.hand[1].rank[0], self.hand[1].suit)


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
            res.append(str(cards.rank[0]) + cards.suit)
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
        # add check for sorted numeric ranks to check straight(highest first)
        # add check to see if an Ace makes a straight with 2345 if no other found
        # add check for straight flush ?
        # add check for royal flush ?

        tmp = []

        for card in self.board:
            tmp.append(card)

        for card in hand:
            tmp.append(card)

        # tmp.sort()
        # tmp.reverse()

        for x in tmp:

            if (x.rank_numeric == tmp[x + 1].rank_numeric + 1
                    and tmp[x + 1].rank_numeric == tmp[x + 2].rank_numeric + 1
                    and tmp[x + 2].rank_numeric == tmp[x + 3].rank_numeric + 1
                    and tmp[x + 3].rank_numeric == tmp[x + 4].rank_numeric + 1):
                print('STRAIGHT FOUND:')
                format_it = '{}{} {}{} {}{} {}{} {}{}'.format(tmp[x].rank, tmp[x].suit, tmp[x + 1].rank,
                                                              tmp[x + 1].suit,
                                                              tmp[x + 2].rank, tmp[x + 2].suit, tmp[x + 3].rank,
                                                              tmp[x + 3].suit, tmp[x + 4].rank, tmp[x + 4].suit)
                print(format_it)

    def eval_equals(self, hand):

        # check if hand and board contains same ranked cards and returns amount of matches found in "poker terms"
        # todo:
        # - add check for pairs not connected to player hand
        # - add check for pair in hand
        # - add return pair value
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])

        dubs = []
        trips = []
        quads = []
        hi = len(all_cards)
        for i in range(hi):
            hits = 0
            tem = []
            for j in range(hi):
                if all_cards[i].rank[1] == all_cards[j].rank[1]:
                    tem.append([all_cards[i], all_cards[j]])

                    hits += 1
            print(hits)
            if hits >= 4:
                quads.append(tem)
            elif hits >= 3:
                trips.append(tem)
            elif hits >= 2:
                dubs.append(tem)

        if quads:
            print(
                'QUADS with these cards: {}{} {}{} {}{} {}{}'.format(quads[0][0].rank[0], quads[0][0].suit,
                                                                     quads[0][1].rank[0],
                                                                     quads[0][1].suit, quads[0][2].rank[0],
                                                                     quads[0][2].suit,
                                                                     quads[0][3].rank[0], quads[0][3].suit))
        elif trips:
            print(trips[0])
            # print('TRIPS with these cards: {}{} {}{} {}{}'.format(trips[0][0].rank[0], trips[0][0].suit,
            #                                                      trips[0][1].rank[0],
            #                                                      trips[0][1].suit, trips[0][2].rank[0],
            #                                                      trips[0][2].suit, ))
        elif dubs:
            print(dubs)
            # top_pair = self.get_biggest_pair(dubs)
            # print('DUBS with these cards: {]{] {]{]'.format(top_pair[0].rank[0], top_pair[0].suit, top_pair[1].rank[0],
            #                                               top_pair[1].suit))


def get_biggest_pair(list_of_equals):
    ceil = 0
    top_pair = None
    for x in range(len(list_of_equals)):
        if list_of_equals[x][0].rank(1) > ceil:
            ceil = list_of_equals[x][0].rank[1]
            top_pair = list_of_equals[x]
    return top_pair
