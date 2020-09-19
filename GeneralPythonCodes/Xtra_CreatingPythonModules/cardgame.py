# =========================================================================== #
# Python Script for Playing Poker, created by Sourav Sen Gupta
# Imports the classes Card, Deck, Hand from an external Module
# =========================================================================== #

from playingcards import Card, Deck, Hand

# Create a Deck
deck = Deck()
print("Deck created : ", str(deck))

# Create a Hand for each of the 5 Players
players = ["Alice", "Bob", "Charles", "Dalton", "Emory"]
hands = dict((player,None) for player in players)

for player in players:
    hand = Hand(player)
    hands[player] = hand
    print("Hand created : ", str(hand))

# Shuffle the Deck of Cards
deck.shuffleCards()

# Draw cards from Deck and add to Hands
for _ in range(2):
    for player in players:
        # Draw a Card from the Deck
        card = deck.drawCard()
        # Add the drawn card to the hand
        hands[player].addCard(card)

# Show the Hands
print()
print()
for player in players:
    print("Hand of ", player)
    hands[player].show()
    print()

# =========================================================================== #
