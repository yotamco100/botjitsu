from Card import *

class Player(object):

    def __init__(self):
        self.deck = Deck()
        self.hand = self.deck.deal()
        
    def start_turn(self):
        self.hand.append(self.deck.draw())
        for index, card in enumerate(self.hand):
            print(str(index+1) + "." + " " + str(card))
    

my_player = Player()
my_player.start_turn()