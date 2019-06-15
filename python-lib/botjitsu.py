# Author: Yotam Cohen
# A Python library for the BotJitsu tournament

from Player import *
from json import load
from cards import *
#import bot_code



class Game(object):
    """
    This class is an API for the game state.
    Includes constants, functions, and game
    state variables for ease of use as an API.
    """
    FULL_DECK = []

    with open('deck.json') as deck_file:
        decks = load(deck_file)

        for card in decks['cards']:
            element = Elements(card['element'])
            color = Colors(card['color'])
            number = int(card['number'])
            FULL_DECK.append(Card(element, color, number))

    def __init__(self, my_number, my_hand_config):
        #TODO: implement game data
        self.my_number = my_number
        self.my_player = Player(my_hand_config)
        self.enemy_player = Player([])  # since you don't know the enemy's hand.
        # enemy_player can keep track of the opponent's won_cards.

    """
    # NOTE: Too overpowered?
    @staticmethod
    def cards_remaining_in_deck(won_cards):
        "#""
        Given a won_cards string, determines what cards remain in the deck.

        Gets: won_cards(Card[])
        Returns: remaining_in_deck(Card[])
        "#""
        remaining_deck = list(Game.FULL_DECK)
        for card in won_cards:
            remaining_deck.remove(card)
        return remaining_deck

    """

    def _update_hand(self, new_hand):
        """
        updates the Player's hand in the game object.

        Gets: new_hand(str[], new-age config syntax)
        Returns: None.
        """
        self.my_player._hand = [cards.Card.cfg2card(new_card) for new_card in new_hand]

    def _update_round_winner(self, winning_player, winning_card):
        """
        Updates the Player's won_cards with the winning card.

        Gets: winning_player (int), winning_card(str, new-age config format)
        """
        if winning_player == self.my_number:
            self.my_player.add_to_won_cards(cards.Card.cfg2card(winning_card))
        else:
            self.enemy_player.add_to_won_cards(cards.Card.cfg2card(winning_card))


    # TODO: add more useful API methods

    

# TODO:
"""
now, in context of the API
(API init game shit)
while winner is None:
    bot_choice = bot_code.do_turn(game)
    # maybe, idk how we'll truly implement it yet
    send card choices
    receive round data
    update game accordingly (game._update_hand(), game._update_round_winner()...)
    check for winner
done
"""