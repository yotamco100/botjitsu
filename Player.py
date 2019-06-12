# Authors: @CiniMinis and @yotamco100
# A Player object for Card-Jitsu.

from Card import *

class Player(object):
    """
    A Player class. Represents a single player in the game.
    """
    def __init__(self):
        """
        Creates a Player instance. Inits a Deck and deals 4 cards.

        Gets None.
        Returns a Player instance.
        """
        self.deck = Deck()
        self._hand = self.deck.deal()
        self.won_cards = []
        self.element_sets = {Element.FIRE: set(), Element.WATER: set(), Element.SNOW: set()}

    @property
    def pretty_hand(self):
        """
        Pretty Hand Property.
        Returns a pretty-printed version of the Player's hand.
        """
        hand_str = ""
        for index, card in enumerate(self._hand):
            hand_str += str(index) + "." + " " + str(card) + "\n"
        return hand_str

    @property
    def hand(self):
        """
        Hand Property.
        Returns the Player's hand in csv format, where each
        Card is represented in Config syntax.
        """
        hand_str = ""
        for index, card in enumerate(self._hand):
            hand_str += card.config + ","
        return hand_str[:-1]
        
    def start_turn(self):
        """
        Starts the turn by drawing a card.

        Gets None.
        Returns none.
        """
        self._hand.append(self.deck.draw())
        #print(self.pretty_hand)
    
    def choose_card(self, card_index):
        """
        Plays a card from the Player's hand.

        Gets the Card's index in the hand.
        Returns the chosen Card instance.
        """
        chosen = self._hand[card_index]
        self._hand.remove(chosen)
        #print(self.pretty_hand)
        return chosen

    def check_win(self, card):
        """
        Checks if the Player won the game, using @CiniMinis set theory skills.

        Gets the played Card.
        Returns if the player won the game in boolean form.
        """
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