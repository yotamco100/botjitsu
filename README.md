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

For example, a Fire, Purple, 10 card will be written as: `Fp10`.

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

# The Goal
The goal of each participant is to build the best card-jitsu bot. The given data is exactly what a human player would have: Your hand and each player's "Cards Won" set.

Have fun!
