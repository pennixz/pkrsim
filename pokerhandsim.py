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

# table.flop()
# table.turn()
# table.river()
# table.board = table.deck.create_royal_flush()
table.board = create_full_house()

print('Seat1 evals:')
print('Hand: {}{} {}{}'.format(table.seat1.hand[0].rank[0], table.seat1.hand[0].suit, table.seat1.hand[1].rank[0],
                               table.seat1.hand[1].suit))
table.eval_straight(table.seat1.hand)
table.eval_flush(table.seat1.hand)
table.eval_equals(table.seat1.hand)
print('Seat2 evals:')
print('Hand: {}{} {}{}'.format(table.seat2.hand[0].rank[0], table.seat2.hand[0].suit, table.seat2.hand[1].rank[0],
                               table.seat2.hand[1].suit))
table.eval_straight(table.seat2.hand)
table.eval_flush(table.seat2.hand)
table.eval_equals(table.seat2.hand)
print('Seat3 evals:')
print('Hand: {}{} {}{}'.format(table.seat3.hand[0].rank[0], table.seat3.hand[0].suit, table.seat3.hand[1].rank[0],
                               table.seat3.hand[1].suit))
table.eval_straight(table.seat3.hand)
table.eval_flush(table.seat3.hand)
table.eval_equals(table.seat3.hand)
print('Seat4 evals:')
print('Hand: {}{} {}{}'.format(table.seat4.hand[0].rank[0], table.seat4.hand[0].suit, table.seat4.hand[1].rank[0],
                               table.seat4.hand[1].suit))
table.eval_straight(table.seat4.hand)
table.eval_flush(table.seat4.hand)
table.eval_equals(table.seat4.hand)
print('Seat5 evals:')
print('Hand: {}{} {}{}'.format(table.seat5.hand[0].rank[0], table.seat5.hand[0].suit, table.seat5.hand[1].rank[0],
                               table.seat5.hand[1].suit))
table.eval_straight(table.seat5.hand)
table.eval_flush(table.seat5.hand)
table.eval_equals(table.seat5.hand)
print('Seat6 evals:')
print('Hand: {}{} {}{}'.format(table.seat6.hand[0].rank[0], table.seat6.hand[0].suit, table.seat6.hand[1].rank[0],
                               table.seat6.hand[1].suit))
table.eval_straight(table.seat6.hand)
table.eval_flush(table.seat6.hand)
table.eval_equals(table.seat6.hand)
