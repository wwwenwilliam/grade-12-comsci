# Written by:
# Creation Date:
# Last Edited by:
# Last edit date:
# Documentation File:
# Purpose:


import random

# Global variable decorations

numSuits = 4
numCards = 13
deckCards = []
suitValue = [ "CLUBS","DIAMONDS","HEARTS","SPADES"]
cardValue = [ "ACE",'1','2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING' ]
cardSuit = 0
cardName = 1
cardsLeft = 0
playerBet = 0
playerInfo = [[ "A", 500 ], [ "B", 500 ], [ "HOUSE", 500 ]]  # Later you may want to put in an implementation to get how much each player want's to gamble
ante = 10

def initDeck( numSuits, numCards ):
    return( 48, [ [ True ] * numCards for i in range( numSuits)   ] )

def getValidNum( lowNum, highNum ):
    validNum = int( input( "Enter a number" ))
    keepGoing = ( validNum < lowNum ) or ( validNum > highNum )
    while keepGoing:
        print ( "Error" )
        validNum = int( input( "Enter a number" ))
        keepGoing = ( validNum < lowNum ) or ( validNum > highNum )
    return ( validNum )

def getValidSelection( validList ):
    validSelection = input( "Enter a selection" ).upper()
    keepGoing = not( validSelection in validList )

    while keepGoing:
         print ( "Error")
         validSelection = input( "Enter a selection" ).upper()
         keepGoing = not( validSelection in validList )
    return ( validSelection )


def getACard( numSuits, numCards, cardDeck ):
    whichSuit = random.randint( 0, numSuits - 1 )
    whichCardValue = random.randint( 0, numCards - 1 )
    while cardDeck [ whichSuit][ whichCardValue ] == False:
        whichSuit = random.randint( 0, numSuits - 1 )
        whichCardValue = random.randint( 0, numCards - 1 )
    cardDeck [ whichSuit][ whichCardValue ] = False
    return ( [ whichSuit, whichCardValue ] )

def drawCard(posX, posY, suit, number, deckImage):
    #takes position, card suit&number, image of all cards
    #draws card at position
    pass
    
def cardsNumberCheck(deckCards, minCards):
    #takes a deck of cards
    #returns true if there is enough cards
    pass
    
def buildAHand(deckCards, numSuits, numCards, amountCards):
    #takes deck, numSuits, numCards and num of cards to return
    #returns an array of cards the size of amountCards
    pass

def playerBetting(minBet, maxBet):
    #takes a player's info
    #returns the amount the player bet
    pass
    
def isAce(card):
    #takes a card
    #returns true if it is an ace
    pass
    
def adjustAce():
    #takes nothing
    #returns if ace high(True) or low(False)
    pass
    
def compareBet(hand, card, aceStatus):
    #takes a hand and a card
    #returns true if card is inbetween the cards in the bet
    pass
    
def loseCheck(whichPlayer, playerInfo):
    #takes player's information
    #returns true if bankrupt
    pass
    
def updateMoney(won, bet, whichPlayer, playerInfo):
    #takes a bet and two accounts in a tuple (player, house)
    #returns updated money
    pass

def askIfQuit():
    #returns true if player wants to quit
    pass
    
    
while True:
    ##check for enough cards
    if cardsNumberCheck(deckCards, 0):
        initDeck(numSuits, numCards)
    ##make player pay ante
    playerBetting(ante, ante)
    ##build a hand
    hand = [getACard(numSuits, numCards, deckCards), getACard(numSuits, numCards, deckCards)]
    ##adjust for ace if required
    if isAce(hand[0]) or isAce(hand[1]):
        aceStatus = adjustAce() #not really sure what happens here yet
    else:
        aceStatus = None
    ##player bets
    playerBet = playerBetting(0, playerInfo[whichPlayer][1])
    ##get one card
    lastCard = getACard(numSuits, numCards, deckCards)
    ##display card
    drawCard(posX, posY, lastCard[0][1], lastCard[0][0], deckImage)
    ##check to see if they won
    won = compareBet(hand, lastCard, aceStatus)
    ##update money
    (playerInfo[whichPlayer][1], playerInfo[2][1]) = updateMoney(won, playerBet, whichPlayer, playerInfo)
    ##check if player or house is out of money
    quit = loseCheck(whichPlayer, playerInfo) or loseCheck(3, playerInfo)
    ##check if player wants to quit
    quit = askIfQuit()
    ##check if we go on
    if quit:
        break
    ##pass turn on
    whichPlayer = !whichPlayer

