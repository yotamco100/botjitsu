#!/usr/bin/env python3.7
# Authors: @CiniMinis, @yotamco100 and @MeshyIce
# Card-Jitsu Server object.

import asyncio
import socket
import threading
import time

import player
import cards


# Global variables used in most functions
players = dict()
is_reversed = False


async def get_card_from_players(player):
    """Asks the player for a card and updates player.current_card"""
    player.write(player.get_hand_string())
    selection = player.read()
    player.choose_card(int(selection))


def check_winner(p1, p2):
    """Checks if there is a winner"""
    p1_card, p2_card = p1.current_card, p2.current_card
    print("Player 1's card:\n", p1_card)
    print("Player 2's card:\n", p2_card)

    winner = cards.Card.battle(p1_card, p2_card)
    battle_outcome = f"{p1_card.config} vs. {p2_card.config}: winner={winner}\n"

    await p1.write(battle_outcome)
    await p2.write(battle_outcome)
    print(battle_outcome)

    # After playing the card, insert the card to the bottom of the deck
    p1.deck.play_card(p1_card)
    p2.deck.play_card(p2_card)

    # If there is no winner
    if winner == 0:
        print('Stalemate!')
    else:
        print(f"Player {winner} wins the round!")
        # If the player that won the round also won the game
        is_win = players[winner].check_win()
        if is_win:
            return is_win
        
        print()
        print('Won cards:')


async def run_game():
    global players
    assert len(players) == 2, 'The number of players is incorrect!'
    p1, p2 = players

    winner = None

    while winner is None:
        p1.start_turn()
        p2.start_turn()

        if is_reversed:
            p1.write('* ')
            p2.write('* ')

        # Player 1 is choosing a card
        async p1.update_current_card()
        async p2.update_current_card()

        check_winner(p1, p2)


async def receive_connection(reader, writer):
    global players

    player_count = len(players)

    players[player_count + 1] = player.Player(reader, writer)

    player.write(str(number))

    if len(players) == 2:
        run_game()


if __name__ == "__main__":
    host, port = 'localhost', 14683
    print(f"Server opened with IP {host} and port {port}")

    loop = asyncio.get_event_loop()
    coroutine = asyncio.start_server(receive_connection,
                                     host=host,
                                     port=port,
                                     loop=loop)
