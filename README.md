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

Cards of number 10 are power cards, which means that winning with these cards activates their power.
In our deck, the power of all three power cards is the "reverse" power which causes cards with lower numbers to beat cards with larger numbers in the following round.

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
In order to win a CardJitsu game, you must be the first player to win 3 rounds with cards, either of all different elements with different colors, or of the same element in different colors.

The goal of each participant is to build the best card-jitsu bot. The given data is exactly what a human player would have: Your hand, if reverse is active and the cards played in each round.

Have fun!
