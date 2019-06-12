from Player import  *
import socket

class Server(object):

    def __init__(self, port):
        self.listener = socket.socket()
        self.listener.bind(("0.0.0.0", port))
        self.players = {}
        self.is_reversed = False
        print("Card Jitsu server initialized.")
    
    def listen(self, number):
        self.listener.listen()
        socket, _ = self.listener.accept()
        players[number] = {"socket":socket, "player":Player()}

    def connections(self):
        print("Waiting for player 1...")
        self.listen(1)
        print("Waiting for player 2...")
        self.listen(2)
        print("Both players connected. Starting game...")
        
    def run(self):
        self.connections()
        
    def round_win(self, card1, card2):
        # Checks for round winner and adds to won_cards

        print("Player 1's Card: {}".format(card1))
        print("Player 2's Card: {}".format(card2))

        winning_player = Card.battle(card1, card2, self.is_reversed)

        if winning_player == 0:
            print("Stalemate")
        else:
            print("Player {} wins the round!".format(winning_player))
            winning_card = eval("card" + str(winning_player))
            print("Winning card: " + str(winning_card))
            #self.players[winning_player]["player"].add_won_card(winning_card)

        self.is_reversed = False

        if winning_card.number == 10:
            self.is_reversed = True


if __name__ == "__main__":
    my = Server(8080)
    card1 = Card(Element.FIRE, Color.RED, 5)
    card2 = Card(Element.SNOW, Color.GREEN, 7)
    my.round_win(card1, card2)
