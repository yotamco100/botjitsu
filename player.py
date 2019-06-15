# Authors: @CiniMinis, @yotamco100 and @MeshyIce
# A Player class for Card-Jitsu.

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

    def write(self, message):
        """Used to send data to the player"""
        self.writer.write(message.encode())
        await self.writer.drain()
    
    def read(self, max_length=256):
        """Used to receive data from the player"""
        message = await self.reader.read(100)
        message = message.decode()
        
        return message

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

    def start_turn(self):
        """Starts the turn by drawing a card."""
        self._hand.append(self.deck.draw())

    def draw_card(self, card_index):
        """Plays a card from the Player's hand."""
        try:
            chosen_card = self._hand[card_index]
        # If the index does not exist, choose a random card instead
        except KeyError:
            chosen_card = random.choice(self._hand)
        
        self._hand.remove(chosen_card)
        self.current_card = chosen_card

    def check_win(self, card):
        """Checks if the current player won the game."""
        self.won_cards.append(card)
        self.element_sets[card.element].add(card.color)
       
        # If any of the elements has 3 wins
        if any(len(element_set) == 3 for element_set in self.element_sets):
            return True
        
        all_sets_not_empty = all(len(element_set) > 0
                                 for element_set in self.element_sets)
        all_elements_set = set(card.color for element_set in self.element_sets
                               for card in element_set)
        
        # If all of the elements have at least 1 win
        if all_sets_not_empty and len(all_elements_set) >= 3:
            return True
        
        # If there is no win
        return False