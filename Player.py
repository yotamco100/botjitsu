from Card import *

class Player(object):

    def __init__(self):
        self.deck = Deck()
        self.hand = self.deck.deal()
        