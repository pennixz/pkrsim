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
        self.rank_val = 2

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
                res.append([(tmp[x], tmp[x + 1], tmp[x + 2], tmp[x + 3], tmp[x + 4]),
                    tmp[x].rank[1] + tmp[x + 1].rank[1] + tmp[x + 2].rank[1] + tmp[x + 3].rank[1] + tmp[x + 4].rank[1]])
        return res
    
    def eval_full_house(self, pairs, trips):
        res = []
        print(pairs[0][0])
        try:
            if trips[0][0].index(pairs[0][0][0]) or trips[0][0].index(pairs[0][0][1]):
                pass
        except ValueError:
            res.append([(trips[0][0], pairs[0][0]), trips[0][1] + pairs[0][1]])
        except IndexError:
            pass

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
            hearts.reverse()
            res.append([(hearts[0], hearts[1], hearts[2], hearts[3], hearts[4]),
                hearts[0].rank[1] + hearts[1].rank[1] + hearts[2].rank[1] + hearts[3].rank[1] + hearts[4].rank[1]])

            return res

        elif len(diamonds) >= 5:
            diamonds.sort(key=lambda y: y.rank[1])
            diamonds.reverse()
            res.append([(diamonds[0], hearts[1], hearts[2], hearts[3], hearts[4]),
                hearts[0].rank[1] + hearts[1].rank[1] + hearts[2].rank[1] + hearts[3].rank[1] + hearts[4].rank[1]])

            return res

        elif len(clubs) >= 5:
            diamonds.sort(key=lambda y: y.rank[1])
            diamonds.reverse()
            res.append([(diamonds[0], diamonds[1], diamonds[2], diamonds[3], diamonds[4]),
                diamonds[0].rank[1] + diamonds[1].rank[1] + diamonds[2].rank[1] + diamonds[3].rank[1] +
                diamonds[4].rank[1]])

            return res

        elif len(spades) >= 5:
            spades.sort(key=lambda y: y.rank[1])
            spades.reverse()
            res.append([(spades[0], spades[1], spades[2], spades[3], spades[4]),
                spades[0].rank[1] + spades[1].rank[1] + spades[2].rank[1] + spades[3].rank[1] +
                spades[4].rank[1]])

            return res

    def eval_quads(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()

        res = []
        for x in range(4):
            if (all_cards[x].rank[1] == all_cards[x + 1].rank[1] and all_cards[x + 1].rank[1] == all_cards[x + 2].rank[1] 
                and all_cards[x + 2].rank[1] == all_cards[x + 3].rank[1]):
                res.append([(all_cards[x], all_cards[x + 1], all_cards[x + 2], all_cards[x + 3]), all_cards[x].rank[1] * 4])

        return res

    def eval_trips(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()

        res = []
        for x in range(5):
            if all_cards[x].rank[1] == all_cards[x + 1].rank[1] and all_cards[x + 1].rank[1] == all_cards[x + 2].rank[1]:
                res.append([(all_cards[x], all_cards[x + 1], all_cards[x + 2]), all_cards[x].rank[1] * 3])

        return res
    
    def eval_two_pairs(self, pairs):
        pass        

    def eval_pairs(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()

        res = []
        for x in range(6):
            if all_cards[x].rank[1] == all_cards[x + 1].rank[1]: 
                res.append([(all_cards[x], all_cards[x + 1]),all_cards[x].rank[1] * 2])

        return res

    def eval_high_card(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()

        return all_cards[0]

    
    def eval_winner(self):
        seat1v = self.eval_all(self.seat1.hand)
        seat1best = None
        #seat2v = self.eval_all(self.seat2.hand)
        #seat2best = None
        #seat3v = self.eval_all(self.seat3.hand)
        #seat3best = None
        #seat4v = self.eval_all(self.seat4.hand)
        #seat4best = None
        #seat5v = self.eval_all(self.seat5.hand)
        #seat5best = None
        #seat6v = self.eval_all(self.seat6.hand)
        #seat6best = None
        for x in range(6):
            pass
                    

    def eval_all(self, hand):
        res = []
        straightV = self.eval_straight(hand)
        flushV = self.eval_flush(hand)
        quadsV = self.eval_quads(hand)
        tripsV = self.eval_trips(hand)
        pairsV = self.eval_pairs(hand)
        highV = self.eval_high_card(hand)
        full_houseV = self.eval_full_house(pairsV, tripsV)

        return quadsV, full_houseV, flushV, straightV, tripsV, pairsV, highV


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
