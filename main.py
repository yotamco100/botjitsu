#!/usr/bin/env python3.7
# Authors: @CiniMinis, @yotamco100 and @MeshyIce
# Card-Jitsu Server object.

import asyncio
import socket
import threading
import time

import cards
import player

# Global variables used in most functions
players = dict()
is_reversed = False


async def get_card_from_players(p):
    """Asks the player for a card and updates player.current_card"""
    p.write(p.get_hand_string())
    selection = p.read()
    p.choose_card(int(selection))


async def check_winner(p1, p2):
    """Checks if there is a winner"""
    global is_reversed

    p1_card, p2_card = p1.current_card, p2.current_card
    print("Player 1's card:\n", p1_card)
    print("Player 2's card:\n", p2_card)

    winner = cards.Card.battle(p1_card, p2_card, is_reversed)
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
        return

    print(f"Player {winner} wins the round!")
    # If the player that won the round also won the game

    print()
    print('Won cards:')
    for card in players[winner].won_cards:
        print(card)

    players[winner].add_winning_card()
    is_win = players[winner].check_win()
    # Returns None if there is no winner
    if is_win:
        return is_win


async def run_game():
    """The main game loop, controls the turns"""
    global players, is_reversed
    assert len(players) == 2, 'The number of players is incorrect!'

    p1, p2 = players[1], players[2]

    await p1.write_line('Game Started!')
    await p2.write_line('Game Started!')

    winner = None
    # While the game runs
    while winner is None:
        p1.start_turn()
        p2.start_turn()

        if is_reversed:
            p1.write('* ')
            p2.write('* ')

        # Draw cards for each player
        await p1.draw_card()
        await p2.draw_card()

        winner = await check_winner(p1, p2)
        winner_notification = f"Player {winner} wins!"
        await p1.write_line(winner_notification)
        await p2.write_line(winner_notification)

        is_reversed = False
        # Reverse is activated if a card with a value of 10 and over is played
        if p1.current_card.number >= 10 or p2.current_card.number >= 10:
            is_reversed = True


async def receive_connection(reader, writer):
    global players

    player_count = len(players)

    new_player = player.Player(reader, writer)
    players[player_count + 1] = new_player

    # Notify the player what number he is
    start_message = f"You are player #{player_count + 1}!"
    await new_player.write_line(start_message)

    # If there are 2 players connecting, start the game
    if len(players) == 2:
        await run_game()


if __name__ == "__main__":
    host, port = 'localhost', 14683
    print(f"Server opened with IP {host} and port {port}")

    loop = asyncio.get_event_loop()
    coroutine = asyncio.start_server(receive_connection,
                                     host=host,
                                     port=port,
                                     loop=loop)
    server = loop.run_until_complete(coroutine)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
