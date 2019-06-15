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

    def __str__(self):
        """
        Returns a pretty-print ready string of the card.
        """
        return f"""Element: {self.element.name}
Color: {self.color.name}
Level: {self.number}"""

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
            

class Deck(object):
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

            for line in decks['decks']:
                element, color, number = line
                element = Elements(element)
                color = Colors(int(color))
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