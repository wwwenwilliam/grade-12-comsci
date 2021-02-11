# Written by:
# Creation Date:
# Last Edited by:
# Last edit date:
# Documentation File:
# Purpose:


import random

# Global variable decorations

messageList = [ "Enter your bet between $20 and the money in your pot", "That bet is out of range - You may only bet between $20 and the money in your pot", "Enter Y to continue, any other single letter to stop ", "Must Enter Y or any other single letter to stop" ]
numSuits = 4
numCards = 13
deckCards = []
suitValue = [ "CLUBS","DIAMONDS","HEARTS","SPADES"]
cardValue = [ "ACE",'2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING' ]
cardSuit = 0
cardName = 1
cardsLeft = 0
cardsToStart = 0.95

playerBet = 0
player1 = True
playerInfo = [[ "A", 200 ], [ "B", 200 ], [ "HOUSE", 200 ]]  # Later you may want to put in an implementation to get how much each player want's to gamble and their names
playerName = 0
playerPot = 1
theHouse = 2

playGame = True
minBet = 20
maxBet = 100
ante = 10
minBalance = ante + minBet
playerHand = []
asciiString = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z, "
asciiList = asciiString.split( ',' )
#print ( asciiList )



def initDeck( startingCardsPercent, numSuits, numCards ):
    #returns a full deck
    return( int( startingCardsPercent * numSuits * numCards ), [ [ True ] * numCards for i in range( numSuits)   ] )


def bubbleSort ( whichCol, arrayToSort ):
    limit = len(arrayToSort)
    for i in range(1, limit):
        isSorted = True
        for j in range(limit-i):
            if arrayToSort[j][whichCol] > arrayToSort[j+1][whichCol]:
                (arrayToSort[j], arrayToSort[j+1]) = (arrayToSort[j+1], arrayToSort[j])
                isSorted = False
        if isSorted:
            break
    return( arrayToSort )

def getValidNum( whichMessage, lowNum, highNum ):
    #takes a low number & high number
    #returns a the user's valid input
    validNum = int( input( messageList[ whichMessage ] ))
    keepGoing = ( validNum < lowNum ) or ( validNum > highNum )
    while keepGoing:
        print ( messageList[ whichMessage + 1 ] )
        validNum = int( input( messageList[ whichMessage ] ))
        keepGoing = ( validNum < lowNum ) or ( validNum > highNum )
    return ( validNum )

def getValidSelection( whichMessage, validList ):
    validSelection = input( messageList[ whichMessage ] ).upper()
    keepGoing = not( validSelection in validList )

    while keepGoing:
         print ( messageList[ whichMessage + 1 ] )
         validSelection = input( messageList[ whichMessage ] ).upper()
         keepGoing = not( validSelection in validList )
    return ( validSelection )

def getACard( numSuits, numCards, cardDeck ):
    #returns a random card
    whichSuit = random.randint( 0, numSuits - 1 )
    whichCardValue = random.randint( 0, numCards - 1 )
    while cardDeck [ whichSuit][ whichCardValue ] == False:
        whichSuit = random.randint( 0, numSuits - 1 )
        whichCardValue = random.randint( 0, numCards - 1 )
    cardDeck [ whichSuit][ whichCardValue ] = False
    return ( [ whichSuit, whichCardValue ] )

def getAHand( whichCol, numCardsToTake, numSuits, numCards, cardDeck ):
    #takes parameter to sort by, and number of cards to return
    #returns random sorted hand
    cardHand = []
    for i in range(numCardsToTake):
        cardHand.append(getACard( numSuits, numCards, cardDeck ))
    cardHand = bubbleSort(1, cardHand)
    return( cardHand )

def makeBet( playerInfo, minBet, maxBet ):
    #returns a valid bet
    playerBet = getValidNum(0, minBet, maxBet)
    return ( playerBet )

def displayCards( whereToStart, playerHand ):
    #prints cards to console
    for i in range(whereToStart, len(playerHand)):
        print(suitValue[playerHand[i][0]], "of", cardValue[playerHand[i][1]])

def reportResults( playerInfo ):
    #prints accounts to console
    print("Account values: ")
    print(playerInfo)

def checkWin ( playerHand ):
    #checks if card is in between two values
    if(playerHand[0][1] >= playerHand[2][1] and playerHand[1][1] >= playerHand[2][1]):
        win = True
    else:
        win = False
    return win

                                            # this will eventually become draw in processing but remember draw provides it's own loop

while playGame:
    if cardsLeft <= 0:
        cardsLeft,cardDeck = initDeck(  cardsToStart, numSuits, numCards )

    playerInfo[ player1 ][ playerPot ] -= ante
    playerHand = getAHand( cardName, 2, numSuits, numCards, cardDeck )
    displayCards( 0, playerHand )
    playerBet = makeBet( playerInfo[ player1 ], minBet, maxBet )
    nextCard = getACard( numSuits, numCards, cardDeck )
    playerHand.append( nextCard )

    #print( "nextCard ", nextCard )
    #print( 'player hand ', playerHand )
    displayCards( 2, playerHand )

    playerWon = checkWin( playerHand )
    if playerWon:
        playerInfo[ player1 ][ playerPot ] += playerBet
        playerInfo[ theHouse ][ playerPot ] -= playerBet
    else:
        playerInfo[ player1 ][ playerPot ] -= playerBet
        playerInfo[ theHouse ][ playerPot ] += playerBet

    reportResults( playerInfo )

    #print ( playerInfo, maxBet )
    #print ( "ML ", cardDeck )



    if ( ( playerInfo[ 0 ][ playerPot ] < minBalance ) or ( playerInfo[ 1 ][ playerPot ] < minBalance ) or ( playerInfo[ 2 ][ playerPot ] < minBalance )):
        playGame = False
    elif ( getValidSelection( 2, asciiList ) != "Y" ):
        playGame = False
    else:
        player1 = not player1
