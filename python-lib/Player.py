#!/usr/bin/env python3.7
# Authors: @CiniMinis, @yotamco100 and @MeshyIce
# A Player class for Card-Jitsu.

import asyncio
import itertools
import random

import cards


class Player():
    """A Player class. Represents a single player in the game."""

    def __init__(self, hand_config):
        """
        Creates a Player instance for the API using a given hand config.
        """
        self._hand = [cards.Card.cfg2card(cfg_str) for cfg_str in hand_config]
        self._won_cards = []
        
        self.element_sets = {
            cards.Elements.FIRE: set(),
            cards.Elements.WATER: set(),
            cards.Elements.SNOW: set()
        }

    def pretty_hand(self):
        """Returns a pretty-printed version of the Player's hand."""
        return '\n'.join(f"{index}. {card}"
                         for index, card in enumerate(self._hand))

    def get_hand_string(self):
            """
            Returns the Player's hand in csv format, where each
            card is represented in Config syntax.
            """
            return ','.join(card.config for card in self._hand)
    
    def choose_card(self, card_index):
        """Plays a card from the Player's hand."""
        try:
            chosen = self._hand[card_index]
        except KeyError:
            chosen = cards.random.choice(self._hand)
        
        self._hand.remove(chosen)

        return chosen

    def add_to_won_cards(self, card):
        """
        Given a card object, add it to won_cards array

        Gets: card(Card)
        Returns: None.
        """
        self._won_cards.append(card)