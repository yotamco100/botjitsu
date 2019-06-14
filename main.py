# Authors: @CiniMinis and @yotamco100
# Card-Jitsu Server object.

from Player import *
import socket
import asyncio
import threading
import time


def receive_connection(reader, writer):
    


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
        socket.send((str(number) + "\n").encode())
        self.players[number] = {"socket": socket, "player": Player()}

    def receive_connection(self):
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

    @staticmethod
    def card_selection(player_dict):
        """
        Queries the player for his selected card.
        Sends the player's hand and manages the card selection

        Gets client socket and the player object.
        Returns the selected card.
        Prints None.
        """
        player = player_dict["player"]
        client = player_dict["socket"]
        card = None
        try:
            client.send((player.hand + "\n").encode())
            client.settimeout(60)  # 0.3
            selection = client.recv(256)
            client.settimeout(None)
            card = player.choose_card(int(selection.decode()[0]))
        except Exception as e:
            print(e)
            card = player.choose_card(random.randint(0, 4))
        player_dict["card"] = card

    def run(self):
        """
        Runs the game.
        Connects the players and manages the game until a winner is chosen.

        Gets None.
        Returns None.
        Prints winner.
        """
        self.connections()
        # TESTING
        #self.players[1] = {"socket":None, "player":Player()}
        #self.players[2] = {"socket":None, "player":Player()}
        # END TESTING
        #Players are now connected and the show is on the road
        winner = None
        while winner is None:
            self.players[1]["player"].start_turn()
            self.players[2]["player"].start_turn()

            if self.is_reversed:
                print("Watch out! Reverse is active!")
                sock1 = self.players[1]["socket"]
                sock1.send("* ".encode())
                sock2 = self.players[2]["socket"]
                sock2.send("* ".encode())

            #player 1 chooses card
            self.players[1]["card"] = None  #1s choice
            self.players[2]["card"] = None
            threading.Thread(target=Server.card_selection,
                             args=(self.players[1], )).start()
            threading.Thread(target=Server.card_selection,
                             args=(self.players[2], )).start()
            #TESTING
            #Server.card_selection(self.players[1])
            #Server.card_selection(self.players[2])
            #card1 = self.players[1]["player"].choose_card(random.randint(0,4))
            #card2 = self.players[2]["player"].choose_card(random.randint(0,4))
            #END TESTING
            #player 2 chooses card
            while self.players[1]["card"] is None or self.players[2][
                    "card"] is None:
                time.sleep(0.01)
            card2 = self.players[2]["card"]
            card1 = self.players[1]["card"]
            winner = self.round_win(card1, card2)
        win_msg = "Player {} wins!".format(winner)
        print(win_msg)
        sock1 = self.players[1]["socket"]
        sock1.send(win_msg.encode())
        sock2 = self.players[2]["socket"]
        sock2.send(win_msg.encode())
        self.listener.close()

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
        round_str = card1.config + " vs. " + card2.config + ": " + str(
            winning_player) + " wins!\n"
        sock1 = self.players[1]["socket"]
        sock1.send(round_str.encode())
        sock2 = self.players[2]["socket"]
        sock2.send(round_str.encode())
        print(round_str)

        winner = None
        if winning_player == 0:
            print("Stalemate")
            winner = None
        else:
            print("Player {} wins the round!".format(winning_player))
            winning_card = eval("card" + str(winning_player))
            print("Winning card: " + str(winning_card))
            is_win = self.players[winning_player]["player"].check_win(
                winning_card)
            print("\nWon cards:")
            for card in self.players[winning_player]["player"].won_cards:
                print(str(card))
            print("\n\n")
            winner = winning_player if is_win else None

        self.is_reversed = False

        if winning_card.number == 10:
            self.is_reversed = True

        return winner


if __name__ == "__main__":
    host, port = 'localhost', 14683
    print(f"Server opened with IP {host} and port {port}")

    loop = asyncio.get_event_loop()
    coroutine = asyncio.start_server(receive_connection,
                                     host=host,
                                     port=port,
                                     loop=loop)
