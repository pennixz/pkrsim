from deck import *

d = Deck()

table = Table(d)
table.deck.create_cards()

table.deck.draw_hand(table.seat1)
table.deck.draw_hand(table.seat2)
table.deck.draw_hand(table.seat3)
table.deck.draw_hand(table.seat4)
table.deck.draw_hand(table.seat5)
table.deck.draw_hand(table.seat6)

table.flop()
table.turn()
table.river()
# table.board = create_royal_flush() # doesn't work
# table.board = create_full_house()

print(table.show_board())

print('seat1')
print(table.eval_all(table.seat1.hand))

#print('seat2')
#print(table.eval_straight(table.seat1.hand))
#print(table.eval_flush(table.seat1.hand))
#print(table.eval_quads(table.seat2.hand))
#print(table.eval_trips(table.seat2.hand))
#print(table.eval_pairs(table.seat2.hand))
#print(table.eval_high_card(table.seat2.hand).rank[1])

#print('seat3')
#print(table.eval_straight(table.seat1.hand))
#print(table.eval_flush(table.seat1.hand))
#print(table.eval_quads(table.seat3.hand))
#print(table.eval_trips(table.seat3.hand))
#print(table.eval_pairs(table.seat3.hand))
#print(table.eval_high_card(table.seat3.hand).rank[1])

#print('seat4')
#print(table.eval_straight(table.seat1.hand))
#print(table.eval_flush(table.seat1.hand))
#print(table.eval_quads(table.seat4.hand))
#print(table.eval_trips(table.seat4.hand))
#print(table.eval_pairs(table.seat4.hand))
#print(table.eval_high_card(table.seat4.hand).rank[1])

#print('seat5')
#print(table.eval_straight(table.seat1.hand))
#print(table.eval_flush(table.seat1.hand))
#print(table.eval_quads(table.seat5.hand))
#print(table.eval_trips(table.seat5.hand))
#print(table.eval_pairs(table.seat5.hand))
#print(table.eval_high_card(table.seat5.hand).rank[1])

#print('seat6')
#print(table.eval_straight(table.seat1.hand))
#print(table.eval_flush(table.seat1.hand))
#print(table.eval_quads(table.seat6.hand))
#print(table.eval_trips(table.seat6.hand))
#print(table.eval_pairs(table.seat6.hand))
#print(table.eval_high_card(table.seat6.hand).rank[1])
