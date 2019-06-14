# Authors: @CiniMinis and @yotamco100
# A Player object for Card-Jitsu.

from Card import *

class Player(object):
    """
    A Player class. Represents a single player in the game.
    """
    def __init__(self, hand_config):
        """
        Creates a Player instance. Inits a Deck and deals 4 cards.

        Gets None.
        Returns a Player instance.
        """
        self._hand = [Card.cfg2card(cfg_str) for cfg_str in hand_config]
        self._won_cards = []
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
        for card in self._hand:
            hand_str += card.config + ","
        return hand_str[:-1]

    @property
    def pretty_won_cards(self):
        """
        Pretty Won Cards Property.
        Returns a pretty-printed version of the Player's won cards.
        """
        won_cards_str = ""
        for index, card in enumerate(self._won_cards):
            won_cards_str += str(index) + "." + " " + str(card) + "\n"
        return won_cards_str

    @property
    def won_cards(self):
        """
        won cards Property.
        Returns the Player's won cards in csv format, where each
        Card is represented in Config syntax.
        """
        won_cards_str = ""
        for card in self._won_cards:
            won_cards_str += card.config + ","
        return won_cards_str[:-1]
    
    def choose_card(self, card_index):
        """
        Plays a card from the Player's hand.

        Gets the Card's index in the hand.
        Returns the chosen Card instance.
        """
        try:
            chosen = self._hand[card_index]
            self._hand.remove(chosen)
        except KeyError:
            chosen = self._hand[random.randint(0,4)]
        #print(self.pretty_hand)
        return chosen

    def add_to_won_cards(self, card):
        """
        Given a card object, add it to won_cards array

        Gets: card(Card)
        Returns: None.
        """
        self._won_cards.append(card)