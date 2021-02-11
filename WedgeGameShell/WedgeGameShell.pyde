def initializeDeck(numSuits, numCards):
    #creates a new deck
    
def initializeAllPlayers():
    #returns default playerinfo
    return [["PLAYER 2", 100], ["PLAYER 1", 100], ["HOUSE", 500]]

def drawCard(posX, posY, suit, number, deckImage):
    #takes position, card suit&number, image of all cards
    #draws card at position
    
def cardsNumberCheck(deckCards, minCards):
    #takes a deck of cards
    #returns true if there is enough cards
    
def getRandomCard(deckCards, numSuits, numCards):
    #takes a deck, number of suits & cards
    #returns tuple representing card (value, suit)
    
def buildAHand(deckCards, numSuits, numCards, amountCards):
    #takes deck, numSuits, numCards and num of cards to return
    #returns an array of cards the size of amountCards
    
def playerAnte(ante, whichPlayer, playerInfo):
    #takes an ante and an account
    #returns amount after the bet

def playerBetting(whichPlayer, playerInfo):
    #takes a player's info
    #returns the amount the player bet
    
def isAce(card):
    #takes a card
    #returns true if it is an ace
    
def adjustAce():
    #takes nothing
    #returns if ace high(True) or low(False)
    
def compareBet(hand, card, aceStatus):
    #takes a hand and a card
    #returns true if card is inbetween the cards in the bet
    
def loseCheck(whichPlayer, playerInfo):
    #takes player's information
    #returns true if bankrupt
    
def updateMoney(won, bet, whichPlayer, playerInfo):
    #takes a bet and two accounts in a tuple (player, house)
    #returns updated money

def askIfQuit():
    #returns true if player wants to quit
    
# Global variable declarations
numSuits = 4
numCards = 13
deckCards = None
suitValue = ["CLUBS","DIAMONDS","HEARTS","SPADES"]
cardValue = [‘ACE’, ’2’, ’3’, ’4’, ’5’, ’6’, ’7’, ’8’, ’9’, ’10’, ’JACK’, ’QUEEN’, ’KING’]
playerInfo = None
whichPlayer = True #True-player1, False-player2
cardsTaken = 2
deckImage = loadImage("playingcards.png")
cardsLeft = 52
playerBet = 0

def setup():
    global numSuits, numCards, deckCards, suitValue, cardValue, playerInfo, whichPlayer, cardsTaken, deckImage, cardsLeft, playerBet
    
    size(800, 600)
    
    deckCards = initializeDeck(numSuits, numCards)
    playerInfo = initializeAllPlayers()
    
    
def draw():
    global numSuits, numCards, deckCards, suitValue, cardValue, playerInfo, whichPlayer, cardsTaken, deckImage, cardsLeft, playerBet
    ##check for enough cards
    if cardsNumberCheck(deckCards, 48):
        initializeDeck(numSuits, numCards)
    ##make player pay ante
    playerAnte(ante, whichPlayer, playerInfo)
    ##build a hand
    hand = [getRandomCard(deckCards, numSuits, numCards), getRandomCard(deckCards, numSuits, numCards)]
    ##display cards
    drawCard(posX, posY, hand[0][0], hand[0][1], deckImage)
    drawCard(posX, posY, hand[1][0], hand[1][1], deckImage)
    ##adjust for ace if required
    if isAce(hand[0]) or isAce(hand[1]):
        aceStatus = adjustAce() #not really sure what happens here yet
    else:
        aceStatus = None
    ##player bets
    playerBet = playerBetting(whichPlayer, playerInfo)
    ##get one card
    lastCard = getRandomCard(deckCards, numSuits, numCards)
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
        noLoop()
    ##pass turn on
    whichPlayer = !whichPlayer
        
    

    
    
    
    
    
