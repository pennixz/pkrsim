from deck import *


# spade
d = Deck()
table = Table(d)
table.deck.create_cards()
table.deck.draw_hand(table.seat1)
table.flop()
table.turn()
table.river()


print(table.eval_equals(table.seat1.hand))
print(table.show_board())
print(table.seat1.get_hand())
