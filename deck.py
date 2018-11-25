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
        self.burn_cards = []
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

    def burn_card(self):
        self.burn_cards.append(self.deck.pop(0))

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

        self.deck.burn_card()
        for i in range(3):
            self.board.append(self.deck.draw_card())

    def turn(self):
        self.deck.burn_card()
        self.board.append(self.deck.draw_card())

    def river(self):
        self.deck.burn_card()
        self.board.append(self.deck.draw_card())

    def eval_all(self, hand):
        self.eval_straight(hand)
        self.eval_flush(hand)
        self.eval_equals(hand)

    def eval_straight(self, hand):
        res = []
        tmp = self.board + hand
        tmp.sort(key=lambda y: y.rank[1])
        tmp.reverse()
    
        for x in range(3):

            if (tmp[x].rank[1] == tmp[x + 1].rank[1] + 1
                    and tmp[x + 1].rank[1] == tmp[x + 2].rank[1] + 1
                    and tmp[x + 2].rank[1] == tmp[x + 3].rank[1] + 1
                    and tmp[x + 3].rank[1] == tmp[x + 4].rank[1] + 1):
                    
                res.append((tmp[x], tmp[x + 1], tmp[x + 2], tmp[x + 3], tmp[x + 4]))
                res.append(tmp[x].rank[1] + tmp[x + 1].rank[1] + tmp[x + 2].rank[1] + tmp[x + 3].rank[1] + tmp[x + 4].rank[1])
                return res

    def eval_flush(self, hand):
        hearts = []
        diamonds = []
        spades = []
        clubs = []
        res = []
        all_cards = self.board + hand
        for i in range(len(all_cards)):
            if all_cards[i].suit == 'h':
                hearts.append(all_cards[i])
            elif all_cards[i].suit == 'd':
                diamonds.append(all_cards[i])
            elif all_cards[i].suit == 'c':
                clubs.append(all_cards[i])
            elif all_cards[i].suit == 's':
                spades.append(all_cards[i])

        if len(hearts) >= 5:
            hearts.sort(key=lambda y: y.rank[1])
            hearts.reverse
            res.append((hearts[0], hearts[1], hearts[2], hearts[3], hearts[4]))
            res.append(hearts[0].rank[1] + hearts[1].rank[1] + hearts[2].rank[1] + hearts[3].rank[1] + hearts[4].rank[1])

            return res

        if len(diamonds) >= 5:
            diamonds.sort(key=lambda y: y.rank[1])
            diamonds.reverse
            res.append((hearts[0], hearts[1], hearts[2], hearts[3], hearts[4]))
            res.append(hearts[0].rank[1] + hearts[1].rank[1] + hearts[2].rank[1] + hearts[3].rank[1] + hearts[4].rank[1])

            return res

       if len(clubs) >= 5:
            print('FLUSH!')
            clubs.sort(key=lambda y: y.rank[1])
            clubs.reverse()
            print('{}{} {}{} {}{} {}{} {}{}'.format(clubs[0].rank[0], clubs[0].suit, clubs[1].rank[0],
                                                    clubs[1].suit, clubs[2].rank[0], clubs[2].suit,
                                                    clubs[3].rank[0],
                                                    clubs[3].suit, clubs[4].rank[0], clubs[4].suit))
        if len(spades) >= 5:
            print('FLUSH!')
            spades.sort(key=lambda y: y.rank[1])
            spades.reverse()
            print('{}{} {}{} {}{} {}{} {}{}'.format(spades[0].rank[0], spades[0].suit, spades[1].rank[0],
                                                    spades[1].suit, spades[2].rank[0], spades[2].suit,
                                                    spades[3].rank[0],
                                                    spades[3].suit, spades[4].rank[0], spades[4].suit))

    def eval_quads(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()
        
        res = []
        for x in range(4):
            if all_cards[x] == all_cards[x + 1] and all_cards[x + 1] == all_cards[x + 2] and all_cards[x + 2] == all_cards[x + 3]:
                res.append((all_cards[x], all_cards[x + 1], all_cards[x + 2], all_cards[x + 3]))
                res.append(all_cards[x].rank[1] * 4)
                    
        return res

    def eval_trips(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()

        res = []
        for x in range(5):
            if all_cards[x] == all_cards[x + 1] and all_cards[x + 1] == all_cards [x + 2]:
                res.append((all_cards[x], all_cards[x + 1], all_cards[x + 2]))
                res.append(all_cards[x].rank[1] * 3)

        return res
            
    def eval_pairs(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()

        res = []
        for x in range(6):
            if all_cards[x] == all_cards[x + 1]:
                res.append((all_cards[x], all_cards[x + 1]))
                res.append(all_cards[x].rank[1] * 2)

        return res

    def eval_highcard(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key = lambda y: y.rank[1])
        all_cards.reverse()

        return all_cards[0]

def get_biggest_pair(list_of_equals):
    ceil = 0
    top_pair = None

    for x in range(len(list_of_equals[0]) - 1):
        if list_of_equals[x][0].rank[1] > ceil:
            ceil = list_of_equals[x][0].rank[1]
            top_pair = [list_of_equals[x][0], list_of_equals[x][1]]

    return top_pair


def create_royal_flush():
    res = []
    card = Card('A', 14, 'h')
    res.append(card)
    card = Card('K', 13, 'h')
    res.append(card)
    card = Card('Q', 12, 'h')
    res.append(card)
    card = Card('J', 11, 'h')
    res.append(card)
    card = Card('10', 10, 'h')
    res.append(card)
    return res


def create_full_house():
    res = []
    card = Card('J', 11, 'h')
    res.append(card)
    card = Card('J', 11, 'd')
    res.append(card)
    card = Card('J', 11, 'c')
    res.append(card)
    card = Card('Q', 12, 'd')
    res.append(card)
    card = Card('Q', 12, 'c')
    res.append(card)

    return res
