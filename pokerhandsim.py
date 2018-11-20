import deck as dck


table = dck.Table()
table.deck = dck.Deck()
table.deck.create_cards()
table.pre_flop()
table.flop()
table.turn()
table.river()

print(table.get_board())
print(table.get_hands())
