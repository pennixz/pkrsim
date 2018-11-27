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
        self.verbose = False

    def all_draw_hand(self):
        self.deck.draw_hand(self.seat1)
        self.deck.draw_hand(self.seat2)
        self.deck.draw_hand(self.seat3)
        self.deck.draw_hand(self.seat4)
        self.deck.draw_hand(self.seat5)
        self.deck.draw_hand(self.seat6)

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
                            tmp[x].rank[1] + tmp[x + 1].rank[1] + tmp[x + 2].rank[1] + tmp[x + 3].rank[1] +
                            tmp[x + 4].rank[1]])
                return res

        return False

    def eval_full_house(self, pairs, trips):
        res = []
        try:
            if trips[0][0].index(pairs[0][0][0]) or trips[0][0].index(pairs[0][0][1]):
                pass

        except ValueError:
            res.append([(trips[0][0], pairs[0][0]), trips[0][1] + pairs[0][1]])
        except IndexError:
            pass
        except TypeError:
            pass

        if res:
            return res
        else:
            return False

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
                        hearts[0].rank[1] + hearts[1].rank[1] + hearts[2].rank[1] + hearts[3].rank[1] + hearts[4].rank[
                            1]])

            return res

        elif len(diamonds) >= 5:
            diamonds.sort(key=lambda y: y.rank[1])
            diamonds.reverse()
            res.append([(diamonds[0], diamonds[1], diamonds[2], diamonds[3], diamonds[4]),
                        diamonds[0].rank[1] + diamonds[1].rank[1] + diamonds[2].rank[1] + diamonds[3].rank[1] +
                        diamonds[4].rank[
                            1]])

            return res

        elif len(clubs) >= 5:
            clubs.sort(key=lambda y: y.rank[1])
            clubs.reverse()
            res.append([(clubs[0], clubs[1], clubs[2], clubs[3], clubs[4]),
                        clubs[0].rank[1] + clubs[1].rank[1] + clubs[2].rank[1] + clubs[3].rank[1] +
                        clubs[4].rank[1]])

            return res

        elif len(spades) >= 5:
            spades.sort(key=lambda y: y.rank[1])
            spades.reverse()
            res.append([(spades[0], spades[1], spades[2], spades[3], spades[4]),
                        spades[0].rank[1] + spades[1].rank[1] + spades[2].rank[1] + spades[3].rank[1] +
                        spades[4].rank[1]])

            return res

        else:
            return False

    def eval_quads(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()

        res = []
        for x in range(4):
            if (all_cards[x].rank[1] == all_cards[x + 1].rank[1] and all_cards[x + 1].rank[1] == all_cards[x + 2].rank[
                1]
                    and all_cards[x + 2].rank[1] == all_cards[x + 3].rank[1]):
                res.append(
                    [(all_cards[x], all_cards[x + 1], all_cards[x + 2], all_cards[x + 3]), all_cards[x].rank[1] * 4])

        if res:
            return res
        else:
            return False

    def eval_trips(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()

        res = []
        for x in range(5):
            if (all_cards[x].rank[1] == all_cards[x + 1].rank[1]
                    and all_cards[x + 1].rank[1] == all_cards[x + 2].rank[1]):
                res.append([(all_cards[x], all_cards[x + 1], all_cards[x + 2]), all_cards[x].rank[1] * 3])
                return res

        return False

    def eval_two_pairs(self, pairs):
        try:
            if len(pairs) >= 2:
                return pairs[0][0], pairs[1][0], (pairs[0][1] + pairs[1][1])

        except TypeError:
            return False

    def eval_pairs(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()

        res = []
        for x in range(6):
            if all_cards[x].rank[1] == all_cards[x + 1].rank[1]:
                res.append([(all_cards[x], all_cards[x + 1]), all_cards[x].rank[1] * 2])
                x += 2

        if res:
            return res
        else:
            return False

    def eval_high_card(self, hand):
        all_cards = self.board + hand
        all_cards.sort(key=lambda y: y.rank[1])
        all_cards.reverse()

        return all_cards[0]

    def eval_winner(self):
        res = []
        seat1v = self.eval_all(self.seat1.hand)
        seat2v = self.eval_all(self.seat2.hand)
        seat3v = self.eval_all(self.seat3.hand)
        seat4v = self.eval_all(self.seat4.hand)
        seat5v = self.eval_all(self.seat5.hand)
        seat6v = self.eval_all(self.seat6.hand)
        res.extend([seat1v, seat2v, seat3v, seat4v, seat5v, seat6v])
        if self.verbose:
            print('----- SEAT 1 ------ \nQuads: ', seat1v[0], '\nFull House: ', seat1v[1], '\nFlush: ', seat1v[2],
                  '\nStraight: ', seat1v[3], '\nTwo pair: ', seat1v[4], '\nTrips: ', seat1v[5], '\nPairs: ',
                  seat1v[6], '\nHigh card: ', seat1v[7])
            print('----- SEAT 2 ------ \nQuads: ', seat2v[0], '\nFull House: ', seat2v[1], '\nFlush: ', seat2v[2],
                  '\nStraight: ', seat2v[3], '\nTwo pair: ', seat2v[4], '\nTrips: ', seat2v[5], '\nPairs: ',
                  seat2v[6], '\nHigh card: ', seat2v[7])
            print('----- SEAT 3 ------ \nQuads: ', seat3v[0], '\nFull House: ', seat3v[1], '\nFlush: ', seat3v[2],
                  '\nStraight: ', seat3v[3], '\nTwo pair: ', seat3v[4], '\nTrips: ', seat3v[5], '\nPairs: ',
                  seat3v[6], '\nHigh card: ', seat3v[7])
            print('----- SEAT 4 ------ \nQuads: ', seat4v[0], '\nFull House: ', seat4v[1], '\nFlush: ', seat4v[2],
                  '\nStraight: ', seat4v[3], '\nTwo pair: ', seat4v[4], '\nTrips: ', seat4v[5], '\nPairs: ',
                  seat4v[6], '\nHigh card: ', seat4v[7])
            print('----- SEAT 5 ------ \nQuads: ', seat5v[0], '\nFull House: ', seat5v[1], '\nFlush: ', seat5v[2],
                  '\nStraight: ', seat5v[3], '\nTwo pair: ', seat5v[4], '\nTrips: ', seat5v[5], '\nPairs: ',
                  seat5v[6], '\nHigh card: ', seat5v[7])
            print('----- SEAT 6 ------ \nQuads: ', seat6v[0], '\nFull House: ', seat6v[1], '\nFlush: ', seat6v[2],
                  '\nStraight: ', seat6v[3], '\nTwo pair: ', seat6v[4], '\nTrips: ', seat6v[5], '\nPairs: ',
                  seat6v[6], '\nHigh card: ', seat6v[7])

        for x in range(7):
            tmp = []
            curr_check = None
            if x == 0:
                curr_check = 'Quads'
            elif x == 1:
                curr_check = 'Full House'
            elif x == 2:
                curr_check = 'Flush'
            elif x == 3:
                curr_check = 'Straight'
            elif x == 4:
                curr_check = 'Two Pair'
            elif x == 5:
                curr_check = 'Trips'
            elif x == 6:
                curr_check = 'Pairs'
            elif x == 7:
                curr_check = 'High Card'

            if seat1v[x]:
                tmp.append(('Seat1 ', curr_check, seat1v[x]))
            if seat2v[x]:
                tmp.append(('Seat2 ', curr_check, seat2v[x]))
            if seat3v[x]:
                tmp.append(('Seat3 ', curr_check, seat3v[x]))
            if seat4v[x]:
                tmp.append(('Seat4 ', curr_check, seat4v[x]))
            if seat5v[x]:
                tmp.append(('Seat5 ', curr_check, seat5v[x]))
            if seat6v[x]:
                tmp.append(('Seat6 ', curr_check, seat6v[x]))

            if tmp:
                for i in range(len(tmp)):
                    print(tmp[i])
                break

    def compare(self, variations):
        print(variations)

    def eval_all(self, hand):
        straight_v = self.eval_straight(hand)
        flush_v = self.eval_flush(hand)
        quads_v = self.eval_quads(hand)
        trips_v = self.eval_trips(hand)
        pairs_v = self.eval_pairs(hand)
        high_v = self.eval_high_card(hand)
        full_house_v = False
        if pairs_v and trips_v:
            full_house_v = self.eval_full_house(pairs_v, trips_v)
        two_pair_v = self.eval_two_pairs(pairs_v)

        return quads_v, full_house_v, flush_v, straight_v, two_pair_v, trips_v, pairs_v, high_v


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
