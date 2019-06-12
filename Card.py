import random


class Color(object):
    RED = 'r'
    BLUE = 'b'
    GREEN = 'g'
    YELLOW = 'y'
    ORANGE = 'o'
    PURPLE = 'p'

    color2str = {RED:"Red", BLUE:"Blue", GREEN:"Green", YELLOW:"Yellow", ORANGE:"Orange", PURPLE:"Purple"}


class Element(object):
    FIRE = 0
    WATER = 1
    SNOW = 2

    beats = {FIRE: SNOW, SNOW: WATER, WATER: FIRE}

    char2elem = {'F': FIRE, 'W': WATER, 'S': SNOW}
    elem2char = {FIRE: 'F', WATER: 'W', SNOW: 'S'}
    elem2str = {FIRE: 'Fire', WATER: 'Water', SNOW: 'Snow'}

    @staticmethod
    def beats(elem1, elem2):
        if beats[elem1] == elem2:
            return 1
        elif beats[elem2] == elem1:
            return 2
        else:
            return 0
    



class Card(object):

    def __init__(self, element, color, number):
        self.element = element
        self.color = color
        self.number = number

    @property
    def config(self):
        return Element.elem2char[self.element] + self.color + hex(self.number)[2].upper()

    def __str__(self):
        return "Card Element: {} \tCard Color: {} \tCard Level: {}".format(Element.elem2str[self.element], Color.color2str[self.color], self.number)

class Deck(object):

    def __init__(self):
        self.deck = []
        with open("deck.dcfg", "r") as config:
            for line in config:
                elem = Element.char2elem[line[0]]
                color = line[1]
                number = int(line[2], base=16)
                self.deck.append(Card(elem, color, number))
                # print(self.deck[-1])
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()
    
    def deal(self, card_num=4):
        return [self.draw() for _ in range(card_num)]


if __name__ == "__main__":
    newDeck = Deck()
    print(len(newDeck.deck))
    hand = newDeck.deal()
    for card in hand:
        print(card)
    print(len(newDeck.deck))