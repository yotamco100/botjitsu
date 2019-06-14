# Author: Yotam Cohen
# A Python library for the BotJitsu tournament

from Player import *
#import bot_code



class Game(object):
    """
    This class is an API for the game state.
    Includes constants, functions, and game
    state variables for ease of use as an API.
    """
    FULL_DECK = json.load(open('deck.json'))['decks']

    def __init__(self, my_hand_config):
        #TODO: implement game data
        self.my_player = Player(my_hand_config)
        self.enemy_player = Player([])  # since you don't know the enemy's hand.
        # enemy_player can keep track of the opponent's won_cards.

    @staticmethod
    def cards_remaining_in_deck(won_cards):
        """
        Given a won_cards string, determines what cards remain in the deck.

        Gets: won_cards(str[], config strings)
        Returns: remaining_in_deck(str[], config strings)
        """
        remaining_deck = list(FULL_DECK)
        for card in won_cards:
            remaining_deck.remove(card)
        return remaining_deck

    def _update_hand(self, new_hand):
        """
        updates the Player's hand in the game object.

        Gets: new_hand(str[], config syntax)
        Returns: None.
        """
        self.my_player._hand = [Card.cfg2card(new_card) for new_card in new_hand]

    # TODO: add more useful API methods

    

# TODO:
"""
now, in context of the API
(API init game shit)
while winner is None:
    bot_1_choice = bot_1_code.do_turn(game)?
    bot_2_choice = bot_2_code.do_turn(game)?
    # maybe, idk how we'll truly implement it yet
    send card choices
    receive round data
    update game accordingly
    check for winner
done
"""