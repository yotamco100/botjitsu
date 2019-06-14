# Authors: @CiniMinis and @yotamco100
# Card-Jitsu classes

import random
from dataclasses import dataclass
from enum import Enum
from json import load

class Color(Enum):
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
    FIRE = 0
    WATER = 1
    SNOW = 2

type_effectiveness = {
    Elements.FIRE: Elements.SNOW,
    Elements.WATER: Elements.FIRE,
    Elements.SNOW: Elements.WATER,
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
        return f"{self.element.name}{self.color.name}{:x}".format(self.number)

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
            return elem_out
            

class Deck(object):
    """
    A Deck object. Represents a Deck of Cards, where Cards can be drawn from.
    """
    def __init__(self):
        """
        Creates a new deck.
        
        Opens a deck config file and reads Cards in
        Config syntax, explained above, then shuffles
        the Deck.

        Gets None.
        Returns a Deck instance.
        """
        self.deck = []

        with open('deck.json') as deck_file:
            decks = json.load(deck_file)

            for line in decks['decks']:
                element, color, number = line
                self.deck.append(Card(element, color, number))
        
        random.shuffle(self.deck)

    def draw(self):
        """Draw one Card from the Deck."""
        return self.deck.pop()
    
    def deal(self, card_num=4):
        """Draw card_num Card from the Deck. Used at start of game."""
        return [self.draw() for _ in range(card_num)]
