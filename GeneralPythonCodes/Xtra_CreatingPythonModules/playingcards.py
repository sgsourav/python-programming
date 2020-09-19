# =========================================================================== #
# Python Module for Playing Cards, created by Sourav Sen Gupta
# Contains definitions for three Classes : Card, Deck and Hand
# =========================================================================== #

# Import random
import random

# =========================================================================== #
# Class for a Single Playing Card

class Card(object):
    ''' Standard playing card.
        If no argument is given, initializes "A of Spades".
    '''
    def __init__(self, suit = "Spades", value = "A"):
        '''initializer for card'''
        self.suit = suit
        self.value = value
        
    def __str__(self):
        '''string representation for card'''
        return 'Card(suit = ' + self.suit + ', value = ' + self.value + ')'
        
    def show(self):
        '''print the suit and value of a card'''
        print(self.value, "of", self.suit)

# =========================================================================== #
# Class for a Deck of Playing Cards
# Built as set of Card-type objects

class Deck(object):
    ''' Standard deck of playing cards.
        Contains 52 different cards with 4 suits and 13 values.
    '''
    def __init__(self):
        '''initializer for deck'''
        self.cards = []
        self.setCards()
        
    def __str__(self):
        '''string representation for deck'''
        return 'Standard Deck with 52 Cards'
        
    def setCards(self):
        '''set standard 52 cards in a deck'''
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
                
    def show(self):
        '''print the cards in a deck'''
        for card in self.cards:
            print(card.value, "of", card.suit)
                    
    def listCards(self):
        '''list of all cards in a deck'''
        return self.cards

    def shuffleCards(self):
        '''randomly shuffle the cards in a deck'''
        random.shuffle(self.cards)
        
    def drawCard(self):
        '''draw the top card from a deck'''
        return self.cards.pop()

# =========================================================================== #
# Class for a Hand of Playing Cards
# Inherits from the base class Deck

class Hand(Deck):
    ''' One hand of playing cards.
        Initializes with a blank hand, with provision to add cards.
    '''
    def __init__(self, owner = None):
        '''initializer for hand'''
        self.cards = []
        self.owner = owner
        
    def __str__(self):
        '''string representation for hand'''
        return 'A hand of playing Cards belonging to ' + self.owner
    
    def addCard(self, card=None):
        '''add a card to the hand'''
        if card:
            self.cards.append(card)

# =========================================================================== #

# Python Script to test the Classes
if __name__ == "__main__":
    print("Testing plyingcards module.")
    
    # Create a Deck
    deck = Deck()
    print("Deck created : ", str(deck))

    # Create a Hand
    hand = Hand("Bob")
    print("Hand created : ", str(hand))

    # Shuffle the Deck of Cards
    deck.shuffleCards()

    # Draw a Card from the Deck
    card = deck.drawCard()
    print("Card drawn : ", str(card))

    # Add the drawn card to the hand
    hand.addCard(card)

    # Show the Hand
    print("Cards in hand")
    hand.show()

# =========================================================================== #
