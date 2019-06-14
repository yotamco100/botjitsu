# Authors: @CiniMinis and @yotamco100
# Card-Jitsu classes

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
    RED = 'r'
    BLUE = 'b'
    GREEN = 'g'
    YELLOW = 'y'
    ORANGE = 'o'
    PURPLE = 'p'


class Elements(Enum):
    """
    A Card Element Enum used to distinguish between the different types of elements.
    """
    FIRE = 'F'
    WATER = 'W'
    SNOW = 'S'


type_effectiveness = {
    Elements.FIRE: Elements.SNOW,
    Elements.WATER: Elements.FIRE,
    Elements.SNOW: Elements.WATER,
}

element_characters = {
    'F': Elements.FIRE,
    'W': Elements.WATER,
    'S': Elements.SNOW
}


def does_beat(first_element, second_element):
    if type_effectiveness[first_element] == second_element:
        return 1 # The first element wins
    elif type_effectiveness[second_element] == first_element:
        return 2 # The second element wins
    
    # If both the elements are the same
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
        return f"{self.element.name}{self.color.name}{hex(self.number)[2:].upper()}"
        # @Meshorer: I believe this should be self.number instead of number, correct if wrong.

    def __str__(self):
        """
        Card toString.
        Returns a pretty-printed string of the Card object.
        """
        return f"""Element: {self.element.name}
Color: {self.color.name}
Level: {self.number}"""

    @staticmethod
    def battle(card1, card2, is_reversed):
        """
        Determines the winner of two Card objects.

        Gets two Cards, is_reversed boolean (game state where lower number wins).
        Returns the winning player's number.
        """
        winner = does_beat(card1.element, card2.element)
        if winner == 1:
            if card1.number == card2.number:
                return 0

            elif (card1.number > card2.number) ^ is_reversed:
                return 1

            return 2

        else:
            return winner  # @Meshorer: was elem_out

    @staticmethod
    def cfg2card(cfg_str):
        """
        Given a config string, return a Card object that correlates with that config.

        Gets: Card Config(str).
        Returns: Card object(Card).
        """
        elem = Elements(cfg_str[0])
        color = Colors(cfg_str[1])
        number = int(cfg_str[2], base=16)
        return Card(elem, color, number)