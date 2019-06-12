from Card import *

class Player(object):

    def __init__(self):
        self.deck = Deck()
        self._hand = self.deck.deal()
        self.won_cards = []

    @property
    def pretty_hand(self):
        hand_str = ""
        for index, card in enumerate(self._hand):
            hand_str += str(index) + "." + " " + str(card) + "\n"
        return hand_str

    @property
    def hand(self):
        hand_str = ""
        for index, card in enumerate(self._hand):
            hand_str += card.config + ","
        return hand_str[:-1]
        
    def start_turn(self):
        self._hand.append(self.deck.draw())
        print(self.pretty_hand)
    
    def choose_card(self, card_index):
        chosen = self._hand[card_index]
        self._hand.remove(chosen)
        print(self.pretty_hand)
        return chosen

    def add_won_card(self, card):
        self.won_cards.append(card)
    
"""
my_player = Player()
my_player.start_turn()
print(my_player.hand + "\n")
chosen_card = my_player.choose_card(3)
print("\n" + chosen_card.config)
"""