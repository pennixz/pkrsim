from deck import *

d = Deck()
table = Table(d)

table.deck.create_cards()
table.all_draw_hand()

table.flop()
table.turn()
table.river()
# table.board = create_royal_flush()
# table.board = create_full_house()

print(table.show_board())
table.eval_winner()
