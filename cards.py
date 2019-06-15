#!/usr/bin/env python3.7
# Authors: @CiniMinis, @yotamco100 and @MeshyIce
# Card-Jitsu classes and enums

import random
from dataclasses import dataclass
from enum import Enum
from json import load


class Colors(Enum):
    """
    A Card Color Enum used to distinguish between the different types of colors.

    Conversion:
        >>> print(Colors.RED.value)
        r

        >>> print(Colors.RED.name)
        RED

        >>> red = Colors('r')
        >>> print(red.value)
        r

        >>> fail = Colors('x')
        ValueError: 'x' is not a valid Colors
    """
    RED = 'Red'
    BLUE = 'Blue'
    GREEN = 'Green'
    YELLOW = 'Yellow'
    ORANGE = 'Orange'
    PURPLE = 'Purple'


class Elements(Enum):
    """
    A Card Element Enum used to distinguish between the different types of elements.
    """
    FIRE = 'Fire'
    WATER = 'Water'
    SNOW = 'Snow'


type_effectiveness = {
    Elements.FIRE: Elements.SNOW,
    Elements.WATER: Elements.FIRE,
    Elements.SNOW: Elements.WATER,
}


def does_beat(first_element, second_element):
    # If the first element wins
    if type_effectiveness[first_element] == second_element:
        return 1
    # If the second element wins
    elif type_effectiveness[second_element] == first_element:
        return 2

    # If both elements are the same
    return 0


@dataclass
class Card():
    """A Card object. Represents a single Card-Jitsu card."""
    """
    Creates a new Card.

    Gets an Element (from Enum), Color (from Enum), and number(int).
    Returns a new Card instance.
    """
    element: Elements
    color: Colors
    number: int

    @property
    def config(self):
        """
        Config property.
        Returns the card's config in syntax: [element char][color char][number char, in hex].
        """
        return f"[{self.element.value}] [{self.color.value}] [{self.number}]"

    def __str__(self):
        """
        Returns a pretty-print ready string of the card.
        """
        return f"""=== Element: {self.element.name}
=== Color: {self.color.name}
=== Level: {self.number}"""

    @staticmethod
    def battle(card1, card2, is_reversed):
        """Determines the winner of the two cards."""
        winner = does_beat(card1.element, card2.element)

        if winner == 0:
            if card1.number == card2.number:
                return 0

            # If first card is bigger than the second
            # (or the opposite if is_reverse is True)
            elif (card1.number > card2.number) ^ is_reversed:
                return 1

            # The second player has one the round
            return 2
        else:
            return winner


class Deck():
    """Represents a deck of cards, where cards can be drawn from."""

    def __init__(self):
        """
        Creates a new deck.
        
        Opens a deck config file and reads the cards
        in the config syntax explained above,
        then shuffles the Deck.
        """
        self.deck = []

        with open('deck.json') as deck_file:
            decks = load(deck_file)

            for card in decks['cards']:
                element = Elements(card['element'])
                color = Colors(card['color'])
                number = int(card['number'])
                self.deck.append(Card(element, color, number))

        random.shuffle(self.deck)

    def draw(self):
        """Draw one Card from the Deck."""
        return self.deck.pop()

    def deal(self, card_num=4):
        """Draw card_num Card from the Deck. Used at start of game."""
        return [self.draw() for _ in range(card_num)]

    def play_card(self, card):
        """Plays a certain card and inserts it to the bottom of the deck"""
        self.deck.insert(0, card)
