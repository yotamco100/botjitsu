#!/usr/bin/env python3.7
# Authors: @CiniMinis, @yotamco100 and @MeshyIce
# A Player class for Card-Jitsu.

import asyncio
import itertools
import random

import cards


class Player():
    """A Player class. Represents a single player in the game."""

    def __init__(self, reader, writer):
        """
        Creates a Player instance.
        Initializes a deck and deals 4 cards.
        """
        self.deck = cards.Deck()
        self._hand = self.deck.deal()
        self.won_cards = []
        self.current_card = None

        self.reader = reader
        self.writer = writer

        self.element_sets = {
            cards.Elements.FIRE: set(),
            cards.Elements.WATER: set(),
            cards.Elements.SNOW: set()
        }

    async def write(self, message):
        """Used to send data to the player"""
        self.writer.write(message.encode())
        await self.writer.drain()

    async def write_line(self, message):
        await self.write(message + '\n')

    async def read(self, max_length=256):
        """Used to receive data from the player"""
        message = await self.reader.read(100)
        message = message.decode()

        return message

    def pretty_hand(self):
        """Returns a pretty-printed version of the Player's hand."""
        return '\n'.join(f"{index}.\n{card}\n"
                         for index, card in enumerate(self._hand))

    def get_hand_string(self):
        """
        Returns the Player's hand in csv format, where each
        card is represented in Config syntax.
        """
        return ','.join(card.config for card in self._hand)

    def start_turn(self):
        """Starts the turn by drawing a card."""
        self.current_card = None
        self._hand.append(self.deck.draw())

    async def draw_card(self):
        """Plays a card from the Player's hand."""
        try:
            card_index = int(await self.read())
            chosen_card = self._hand[card_index]
        # If the index does not exist, choose a random card instead
        except (KeyError, ValueError):
            chosen_card = random.choice(self._hand)

        self._hand.remove(chosen_card)
        self.current_card = chosen_card

    def add_winning_card(self):
        """Adds the given card to the winning list"""
        card = self.current_card
        self.won_cards.append(card)
        self.element_sets[card.element].add(card.color)

    def check_win(self):
        """Checks it the current player won the game."""
        current_element = self.current_card.element

        # If the player won 3 cards of the same type and differnet colors
        if len(self.element_sets[current_element]) >= 3:
            return True

        # If the player won 3 cards in different colors and different sets
        if any(
                len(set(product)) == 3
                for product in itertools.product(*self.element_sets.values())):
            return True

        # If the player did not win
        return False

    def efficient_check_win(self):
        """Checks if the current player won the game.
        Using entirely unclear set theory wizardry for the specific case"""
        current_element = self.current_card.element
        current_color = self.current_card.color
        # Check if the new card completed a same element trio
        if len(self.element_sets[current_element]) >= 3:
            return True

        other_element_sets = [
            self.element_sets[(current_element + 1) % 3],
            self.element_sets[(current_element + 2) % 3]
        ]
        # using current color since the new card must be used if there is a new win
        unique_in_other_sets = [
            other_element_sets[i] - (other_element_sets[i - 1] + current_color)
            for i in range(2)
        ]
        # set of colors which could complete the unique_in_other set and the new card to a win
        completion_sets = [
            other_element_sets[i + 1] -
            (unique_in_other_sets[i] + current_color) for i in range(2)
        ]

        # If a trio of 3 elements is possible
        if any(
                len(unique_in_other_sets[i]) > 0
                and len(completion_sets[i - 1]) > 0 for i in range(2)):
            return True

        # If there is no win
        return False
