# Authors: @CiniMinis and @yotamco100
# A Player object for Card-Jitsu.

import random
import asyncio
import cards


class Player():
    """A Player class. Represents a single player in the game."""
    def __init__(self, reader, writer):
        """
        Creates a Player instance. Initializes a deck and deals 4 cards.
        """
        self.deck = cards.Deck()
        self._hand = self.deck.deal()
        self.won_cards = []
        
        self.reader = reader
        self.writer = writer

        self.element_sets = {
            cards.Element.FIRE: set(),
            cards.Element.WATER: set(),
            cards.Element.SNOW: set()
        }

    async def write(self, message):
        self.writer.write(message.encode())
        await self.writer.drain()

    @property
    def pretty_hand(self):
        """
        Pretty Hand Property.
        Returns a pretty-printed version of the Player's hand.
        """
        return '\n'.join(f"{index}. {card}"
                         for index, card in enumerate(self._hand))

    @property
    def hand(self):
        """
        Hand Property.
        Returns the Player's hand in csv format, where each
        Card is represented in Config syntax.
        """
        return ','.join(card.config for card in self._hand)

    def start_turn(self):
        """Starts the turn by drawing a card."""
        self._hand.append(self.deck.draw())
        #print(self.pretty_hand)

    def choose_card(self, card_index):
        """Plays a card from the Player's hand."""
        try:
            chosen = self._hand[card_index]
            self._hand.remove(chosen)
        except KeyError:
            chosen = random.chocie(self._hand)

        return chosen

    def check_win(self, card):
        """
        Checks if the Player won the game, using @CiniMinis set theory skills.

        Gets the played Card.
        Returns if the player won the game in boolean form.
        """
        self.won_cards.append(card)
        self.element_sets[card.element].add(card.color)
       
        if len(self.element_sets[card.element]) == 3:
            return True

        other1 = self.element_sets[(card.element + 1) % 3]
        other2 = self.element_sets[(card.element + 2) % 3]

        sub12 = (other1 - other2) - set(card.color)
        if len(sub12) > 0 and len((other2 - sub12) - set(card.color)) > 0:
            return True
        
        sub21 = (other2 - other1) - set(card.color)
        if len(sub21) > 0 and len((other1 - sub21) - set(card.color)) > 0:
            return True
        
        return False
