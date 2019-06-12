from Card import *

class Player(object):

    def __init__(self):
        self.deck = Deck()
        self._hand = self.deck.deal()
        self.won_cards = []
        self.element_sets = {Element.FIRE: set(), Element.WATER: set(), Element.SNOW: set()}

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
        #print(self.pretty_hand)
    
    def choose_card(self, card_index):
        chosen = self._hand[card_index]
        self._hand.remove(chosen)
        #print(self.pretty_hand)
        return chosen

    def check_win(self, card):
        self.won_cards.append(card)
        self.element_sets[card.element].add(card.color)
        if (len(self.element_sets[card.element]) == 3):
            return True
        other1 = self.element_sets[(card.element + 1) % 3]
        other2 = self.element_sets[(card.element + 2) % 3]
        
        sub12 = (other1 - other2) - set(card.color)
        if len(sub12) > 0 and len((other2 - sub12) - set(card.color)) > 0:
            return True
        sub21 = (other2 - other1) - set(card.color)
        if len(sub21) > 0 and len((other1 - sub21) - set(card.color)) > 0:
            return True
        return False
        
    
"""
my_player = Player()
my_player.start_turn()
print(my_player.hand + "\n")
chosen_card = my_player.choose_card(3)
print("\n" + chosen_card.config)
"""