from deck import *


# spade
d = Deck()
table = Table(d)
table.deck.create_cards()
table.deck.draw_hand(table.seat1)


print(table.seat1.show_hand())
