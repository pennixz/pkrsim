one_card = """ 
 ---------------
| {}             |
|               |
|               |
|               |
|       {}       |
|               |
|               |
|               |
|            {}  |
 ---------------
"""
two_card = """ 
 ---------------    ---------------
| {}             |  | {}             |
|               |  |               |
|               |  |               |
|               |  |               |
|       {}       |  |       {}       |
|               |  |               |
|               |  |               |
|               |  |               |
|            {}  |  |            {}  |
 ---------------    ---------------  
"""
three_card = """ 
 ---------------    ---------------    ----------------
| {}             |  | {}            |  | {}             |
|               |  |               |  |                |
|               |  |               |  |                |
|               |  |               |  |                |
|       {}       |  |       {}      |  |       {}       |    
|               |  |               |  |                |
|               |  |               |  |                |
|               |  |               |  |                |
|            {}  |  |            {}  |  |            {}  |
 ---------------    ---------------    ----------------
"""
four_card = """ 
 ---------------    ---------------    ---------------    --------------- 
| {}             |  | {}             |  | {}             |  | {}             |
|               |  |               |  |               |  |               |
|               |  |               |  |               |  |               |
|               |  |               |  |               |  |               |
|       {}       |  |       {}       |  |       {}       |  |       {}       |  
|               |  |               |  |               |  |               |
|               |  |               |  |               |  |               |
|               |  |               |  |               |  |               |
|            {}  |  |            {}  |  |            {}  |  |            {}  |
 ---------------    ---------------    ---------------    ---------------
"""
dealer_default = """ 
 ---------------    ---------------
| {}             |  | ::::::::::::: |
|               |  | ::::::::::::: |
|               |  | ::::::::::::: |
|               |  | ::::::::::::: |
|       {}       |  | ::::::::::::: |
|               |  | ::::::::::::: |
|               |  | ::::::::::::: |
|               |  | ::::::::::::: |
|            {}  |  | ::::::::::::: |
 ---------------    ---------------  
"""

bj_text = """
  ______     __         ______     ______     __  __       __     ______     ______     __  __    
 /\  == \   /\ \       /\  __ \   /\  ___\   /\ \/ /      /\ \   /\  __ \   /\  ___\   /\ \/ /    
 \ \  __<   \ \ \____  \ \  __ \  \ \ \____  \ \  _"-.   _\_\ \  \ \  __ \  \ \ \____  \ \  _"-.  
  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ /\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/\/_/ \/_____/   \/_/\/_/   \/_____/   \/_/\/_/ 
                                                                                                                 

"""
hit_text = """
┬ ┬┬┌┬┐┌─┐  ┬ ┬  ┌─┐┬─┐  ┌┐┌
├─┤│ │  ┌┘  └┬┘  │ │├┬┘  │││
┴ ┴┴ ┴  o    ┴   └─┘┴└─  ┘└┘
"""
d_won_text = """
┬ ┬┌─┐┬ ┬  ┬ ┬┬┌┐┌┬
└┬┘│ ││ │  ││││││││
 ┴ └─┘└─┘  └┴┘┴┘└┘o
"""
p_bust_text = """
┬ ┬┌─┐┬ ┬  ┌┐ ┬ ┬┌─┐┌┬┐┌─┐┌┬┐
└┬┘│ ││ │  ├┴┐│ │└─┐ │ ├┤  ││
 ┴ └─┘└─┘  └─┘└─┘└─┘ ┴ └─┘─┴┘
"""
d_bust_text = """
┌┬┐┌─┐┌─┐┬  ┌─┐┬─┐  ┌┐ ┬ ┬┌─┐┌┬┐┌─┐┌┬┐
 ││├┤ ├─┤│  ├┤ ├┬┘  ├┴┐│ │└─┐ │ ├┤  ││
─┴┘└─┘┴ ┴┴─┘└─┘┴└─  └─┘└─┘└─┘ ┴ └─┘─┴┘
"""
bj_a_text = """
╔╗ ╦  ╔═╗╔═╗╦╔═ ╦╔═╗╔═╗╦╔═
╠╩╗║  ╠═╣║  ╠╩╗ ║╠═╣║  ╠╩╗
╚═╝╩═╝╩ ╩╚═╝╩ ╩╚╝╩ ╩╚═╝╩ ╩
"""
p_won_text = """
┌┬┐┌─┐┌─┐┬  ┌─┐┬─┐  ┬ ┬┬┌┐┌
 ││├┤ ├─┤│  ├┤ ├┬┘  │││││││
─┴┘└─┘┴ ┴┴─┘└─┘┴└─  └┴┘┴┘└┘
"""
p_hand_text = """
╦ ╦╔═╗╦ ╦╦═╗  ╦ ╦╔═╗╔╗╔╔╦╗
╚╦╝║ ║║ ║╠╦╝  ╠═╣╠═╣║║║ ║║
 ╩ ╚═╝╚═╝╩╚═  ╩ ╩╩ ╩╝╚╝═╩╝
"""
dealer_hand_text = """
╔╦╗╔═╗╔═╗╦  ╔═╗╦═╗  ╦ ╦╔═╗╔╗╔╔╦╗
 ║║║╣ ╠═╣║  ║╣ ╠╦╝  ╠═╣╠═╣║║║ ║║
═╩╝╚═╝╩ ╩╩═╝╚═╝╩╚═  ╩ ╩╩ ╩╝╚╝═╩╝
"""
from deck import Deck, Card


def play():
    t_deck.draw_hand(dealer)
    t_deck.draw_hand(player)
    p_score = player[0].rank[1] + player[1].rank[1]
    d_score = dealer[0].rank[1]
    print(dealer_hand_text)
    print(dealer_default.format(dealer[0].rank[0], dealer[0].suit, dealer[0].rank[0]))
    print('Dealer hand value: {}'.format(str(d_score)))
    print(p_hand_text)
    print(two_card.format(player[0].rank[0], player[1].rank[0], player[0].suit, player[1].suit, player[0].rank[0],
                          player[1].rank[0]))
    print('Your hand value: {}'.format(str(p_score)))
    if p_score == 21:
        print(bj_a_text)
        print(p_won_text)
        input()
        return
    elif d_score == 21:
        print(bj_a_text)
        print(d_won_text)
        input()
        return
    elif p_score < 21 and d_score < 21:
        print(hit_text)
        res = input()
        if res == 'y':
            r = t_deck.draw_card()
            p_score += r.rank[1]
            player.append(r)
            print(dealer_hand_text)
            print(dealer_default.format(dealer[0].rank[0], dealer[0].suit, dealer[0].rank[0]))
            print(p_hand_text)
            print(three_card.format(player[0].rank[0], player[1].rank[0], player[2].rank[0], player[0].suit,
                                    player[1].suit,
                                    player[2].suit, player[0].rank[0], player[1].rank[0], player[2].rank[0]))
            print('Your hand value: {}'.format(str(p_score)))
            if p_score < 21:
                print(hit_text)
                rs = input()
                if rs == 'y':
                    t = t_deck.draw_card()
                    p_score += t.rank[1]
                    player.append(t)
                    print(dealer_hand_text)
                    print(dealer_default.format(dealer[0].rank[0], dealer[0].suit, dealer[0].rank[0]))
                    print(p_hand_text)
                    print(four_card.format(player[0].rank[0], player[1].rank[0], player[2].rank[0], player[3].rank[0],
                                           player[0].suit,
                                           player[1].suit,
                                           player[2].suit, player[3].suit, player[0].rank[0], player[1].rank[0],
                                           player[2].rank[0], player[3].rank[0]))
                    print('Your hand value: {}'.format(str(p_score)))
                if p_score < 21:
                    print('welp. bye')
                    return
                else:
                    print(p_bust_text)
                    print(d_won_text)
                    input()
                    return
        else:
            d_score += dealer[1].rank[1]
            if d_score > 16:
                dealer.append(t_deck.draw_card())


t_deck = Deck()
dealer = []
player = []
player_money = 1000
t_deck.create_cards()

for card in t_deck.deck:
    if card.rank[1] == 14:
        card.rank[1] = 11, 1
    elif card.rank[1] > 10:
        card.rank[1] = 10

t_deck.shuffle(t_deck.deck)
print(bj_text)
print('Welcome to BlackJack! Ready to play? y/n')
resp = input()
if resp == 'y':
    play()
