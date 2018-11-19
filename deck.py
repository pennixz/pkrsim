import numpy as np


class Table(object):
    def __init__(self):
        self.seats = 6
        self.deck = None
        self.hands = []
        self.Flop = []
        self.Turn = None
        self.River = None
        self.k = None

    def pre_flop(self):
        for x in range(self.seats):
            self.hands.append(self.deck.draw_hand())

    def flop(self):
        for x in range(3):
            self.Flop.append(self.deck.draw_card())

    def turn(self):
        self.Turn = self.deck.draw_card()

    def river(self):
        self.River = self.deck.draw_card()

    def determine_winner(self):
        # to be continued
        self.k = None

    def get_hands(self):
        return self.hands

    def get_board(self):
        return self.Flop, self.Turn, self.River


class Deck(object):
    def __init__(self):
        self.deckSize = 52
        self.deck = []

    def draw_card(self):
        res = self.deck.pop(0)
        return res

    def draw_hand(self):
        card1 = self.draw_card()
        card2 = self.draw_card()
        return card1, card2

    def create_cards(self):
        for x in range(13):
            if x == 0:
                self.deck.append(['A', 's'])
                self.deck.append(['A', 'c'])
                self.deck.append(['A', 'd'])
                self.deck.append(['A', 'h'])
            elif x == 1:
                self.deck.append(['2', 's'])
                self.deck.append(['2', 'c'])
                self.deck.append(['2', 'd'])
                self.deck.append(['2', 'h'])
            elif x == 2:
                self.deck.append(['3', 's'])
                self.deck.append(['3', 'c'])
                self.deck.append(['3', 'd'])
                self.deck.append(['3', 'h'])
            elif x == 3:
                self.deck.append(['4', 's'])
                self.deck.append(['4', 'c'])
                self.deck.append(['4', 'd'])
                self.deck.append(['4', 'h'])
            elif x == 4:
                self.deck.append(['5', 's'])
                self.deck.append(['5', 'c'])
                self.deck.append(['5', 'd'])
                self.deck.append(['5', 'h'])
            elif x == 5:
                self.deck.append(['6', 's'])
                self.deck.append(['6', 'c'])
                self.deck.append(['6', 'd'])
                self.deck.append(['6', 'h'])
            elif x == 6:
                self.deck.append(['7', 's'])
                self.deck.append(['7', 'c'])
                self.deck.append(['7', 'd'])
                self.deck.append(['7', 'h'])
            elif x == 7:
                self.deck.append(['8', 's'])
                self.deck.append(['8', 'c'])
                self.deck.append(['8', 'd'])
                self.deck.append(['8', 'h'])
            elif x == 8:
                self.deck.append(['9', 's'])
                self.deck.append(['9', 'c'])
                self.deck.append(['9', 'd'])
                self.deck.append(['9', 'h'])
            elif x == 9:
                self.deck.append(['10', 's'])
                self.deck.append(['10', 'c'])
                self.deck.append(['10', 'd'])
                self.deck.append(['10', 'h'])
            elif x == 10:
                self.deck.append(['J', 's'])
                self.deck.append(['J', 'c'])
                self.deck.append(['J', 'd'])
                self.deck.append(['J', 'h'])
            elif x == 11:
                self.deck.append(['Q', 's'])
                self.deck.append(['Q', 'c'])
                self.deck.append(['Q', 'd'])
                self.deck.append(['Q', 'h'])
            elif x == 12:
                self.deck.append(['K', 's'])
                self.deck.append(['K', 'c'])
                self.deck.append(['K', 'd'])
                self.deck.append(['K', 'h'])
        np.random.shuffle(self.deck)
