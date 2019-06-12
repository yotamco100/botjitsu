# Authors: @CiniMinis and @yotamco100
# Card-Jitsu Server object.

from Player import  *
import socket

class Server(object):
    """
    A Card-Jitsu server.
    Used to manage the game between two players.
    """
    def __init__(self, port):
        """
        Creates a server.

        Gets a port number.
        Returns a Server instance.
        """
        self.listener = socket.socket()
        self.listener.bind(("0.0.0.0", port))
        self.players = {}
        self.is_reversed = False
        print("Card Jitsu server initialized.")
    
    def listen(self, number):
        """
        Listens for a connection and adds it to the player list.

        Gets a player number to add.
        Returns None.
        """
        self.listener.listen()
        socket, _ = self.listener.accept()
        self.players[number] = {"socket":socket, "player":Player()}

    def connections(self):
        """
        Listens for connections until both players connect.

        Gets None.
        Returns None.
        """
        print("Waiting for player 1...")
        self.listen(1)
        print("Waiting for player 2...")
        self.listen(2)
        print("Both players connected. Starting game...")
        
    def run(self):
        """
        Runs the game.
        Connects the players and manages the game until a winner is chosen.

        Gets None.
        Returns None.
        Prints winner.
        """
        #self.connections()
        # TESTING
        self.players[1] = {"socket":None, "player":Player()}
        self.players[2] = {"socket":None, "player":Player()}
        # END TESTING
        #Players are now connected and the show is on the road
        winner = None
        while winner is None:
            self.players[1]["player"].start_turn()
            self.players[2]["player"].start_turn()
            if self.is_reversed:
                print("Watch out! Reverse is active!")
            #player 1 chooses card
            card1 = None #1s choice
            card1 = self.players[1]["player"].choose_card(random.randint(0,4))
            #player 2 chooses card
            card2 = None #2s choice
            card2 = self.players[2]["player"].choose_card(random.randint(0,4))
            winner = self.round_win(card1, card2)
        print("Player {} wins!".format(winner))


        
    def round_win(self, card1, card2):
        """
        Checks for round winner and adds to won_cards.
        Also sets the is_reversed global game state parameter.

        Gets the two Chosen cards for the round.
        Returns the winning player's number, or None if stalemate.
        """
        print("Player 1's Card: {}".format(card1))
        print("Player 2's Card: {}".format(card2))

        winning_player = Card.battle(card1, card2, self.is_reversed)
        winner = None
        if winning_player == 0:
            print("Stalemate")
            return None
        else:
            print("Player {} wins the round!".format(winning_player))
            winning_card = eval("card" + str(winning_player))
            print("Winning card: " + str(winning_card))
            is_win = self.players[winning_player]["player"].check_win(winning_card)
            print("\nWon cards:")
            for card in self.players[winning_player]["player"].won_cards:
                print(str(card))
            print("\n\n")
            return winning_player if is_win else None
        

        self.is_reversed = False

        if winning_card.number == 10:
            self.is_reversed = True


if __name__ == "__main__":
    my = Server(8080)
    my.run()
