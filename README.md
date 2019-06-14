# CardJitsu Bot Championship
Do you think your bot has what it takes to beat the rest in an intense match of CardJitsu?

The beloved Club Penguin minigame returns in a brutal bot battle to the ~~death~~ worst paper-cut.
You know.
From the cards.

# Card Configs
## The Cards
Each card is represented in a very computer-readable style we call DeckConfig (dcfg). Very creative, we know.

Any card can be represented using just 3 characters:
```
[Element][Color][Number]
```
Where:

`Element` is either `Fire`, `Water`, or `Snow`, represented as the uppercase first letter of each.

`Color` is one of six colors: `red`, `blue`, `green`, `yellow`, `orange`, or `purple`. Represented as the lowercase first letter of each.

`Number` is an integer represented in Hexadecimal format.

For example, a Fire, Purple, 10 card will be written as: `FpA`.

Cards with the number 10 are "Power Cards", which means that winning with these cards activates their power.
In the tournament deck, the power-up of all three Power Cards is the "Reverse" power-up, which causes cards with lower numbers to beat cards with larger numbers in the following round, but only if the cards played that round share the same element, as explained in the "How do I win a CardJitsu round?" section.

## The Deck
Since each card is so easily read, a Deck can be easily arranged using a .dcfg file, where each line is a card in DeckConfig syntax.

For example, a 5-card my_deck.dcfg file looks like this:
```
Wb8
So3
Fr4
Fo5
Sg8
```

For ease of use, each Card and Player have a pretty-printing function they can call to display the cards in a more human-readable format: ```Card Element: Fire,   Card Color: Red,     Card Level: 4```

## Read More
You are more than welcome to read more about cardjitsu play in the club penguin wiki:
https://clubpenguin.fandom.com/wiki/Card-Jitsu

# Game Interface

## Player Number
When first connecting to the server, you will be sent either "1" or "2" to indicate whether you register as player 1 or player 2.

## The Hand
The first message sent to the player is a listing of the 5 cards which make up his hand. If the reverse powerup is active in the game, it will be preceeded by a message of ```* ```.
For example:
```FyA,Fr6,WoA,Sg6,Wo5```
```* ``` followed by ```FyA,WoA,Sg6,Wo5,Fp6```
Are valid hands.

## Card Selection
To select a card, send a number between 0 and 4 to the server representing the index of the card which you wish to play.
Any invalid message, as well as taking too long to reply (exact time will be decided during the match),  will trigger a random card to be selected.

## Round Result
After both players have selected their cards, the server will return a round result of the following format:
player_1s_card vs. player_2s_card: no_of_winning_player wins!

## Match Result
When a player wins, a message is sent to both players saying which player won, with the format of:
Player no_of_winning_player wins!

## Example
The following is an exanple of a quick game which shows all aspects of the game, where messages preceeded by > are sent to the server.
```
1
FyA,WoA,Wo5,SgA,Fg8
>1
WoA vs. Fr6: 1 wins!
*FyA,Wo5,SgA,Fg8,Fb3
>4
Fb3 vs. FyA: 1 wins!
FyA,Wo5,SgA,Fg8,Wp4
>2
SgA vs. Wo5: 1 wins!
Player 1 wins!
```

# The Goal

## How do I win a CardJitsu round/game?

Consult this handy graphic:

![alt text](https://i.imgur.com/bMHJlW3.png)

Water beats Fire, Fire beats Ice, Ice beats water. If the cards played share the same element, the higher number is used to determine who wins. If the Reverse power-up is in effect, as explained above, the lower number wins. If two cards are exactly the same, a "Stalemate" happens and the round concludes without a winner.

In order to win a CardJitsu game, you must be the first player to win 3 rounds with cards, either of all different elements with different colors, or of the same element in different colors.

## How do I win a BotJitsu Tournament?

The goal of each participant is to build the best card-jitsu bot. The given data is exactly what a human player would have: Your hand, if reverse is active and the cards played in each round.

Have fun!
