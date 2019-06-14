# Authors: @CiniMinis and @yotamco100
# Card-Jitsu classes

import random
import json


class Color(object):
    """
    A Card Color Enum, including conversions to strings.
    """
    RED = 'r'
    BLUE = 'b'
    GREEN = 'g'
    YELLOW = 'y'
    ORANGE = 'o'
    PURPLE = 'p'

    color2str = {RED:"Red", BLUE:"Blue", GREEN:"Green", YELLOW:"Yellow", ORANGE:"Orange", PURPLE:"Purple"}


class Element(object):
    """
    A Card Element Enum, including conversions to chars and strings.
    """
    FIRE = 0
    WATER = 1
    SNOW = 2

    beats_arr = {FIRE: SNOW, SNOW: WATER, WATER: FIRE}

    char2elem = {'F': FIRE, 'W': WATER, 'S': SNOW}
    elem2char = {FIRE: 'F', WATER: 'W', SNOW: 'S'}
    elem2str = {FIRE: 'Fire', WATER: 'Water', SNOW: 'Snow'}

    @staticmethod
    def beats(elem1, elem2):
        """
        An element battle function.
        
        Gets two Elements.
        Returns the winning Player's number, or 0 if stalemate.
        """
        if Element.beats_arr[elem1] == elem2:
            return 1
        elif Element.beats_arr[elem2] == elem1:
            return 2
        else:
            return 0
    



class Card(object):
    """
    A Card object. Represents a single Card-Jitsu card.
    """
    def __init__(self, element, color, number):
        """
        Creates a new Card.

        Gets an Element (from Enum), Color (from Enum), and number(int).
        Returns a new Card instance.
        """
        self.element = element
        self.color = color
        self.number = number

    @property
    def config(self):
        """
        Config property.
        Returns the card's config in syntax: [element char][color char][number char, in hex].
        """
        return Element.elem2char[self.element] + self.color + hex(self.number)[2].upper()

    def __str__(self):
        """
        Card toString.
        Returns a pretty-printed string of the Card object.
        """
        return "Card Element: {} \tCard Color: {} \tCard Level: {}".format(Element.elem2str[self.element], Color.color2str[self.color], self.number)

    @staticmethod
    def battle(card1, card2, is_reversed):
        """
        Determines the winner of two Card objects.

        Gets two Cards, is_reversed boolean (game state where lower number wins).
        Returns the winning player's number.
        """
        elem_out = Element.beats(card1.element, card2.element)
        if elem_out == 0:
            if card1.number == card2.number:
                return 0
            if (card1.number > card2.number) ^ is_reversed:
                return 1
            return 2
        else:
            return elem_out

    @staticmethod
    def cfg2card(cfg_str):
        """
        Given a config string, return a Card object that correlates with that config.

        Gets: Card Config(str).
        Returns: Card object(Card).
        """
        elem = Element.char2elem[cfg_str[0]]
        color = cfg_str[1]
        number = int(cfg_str[2], base=16)
        return Card(elem, color, number)
