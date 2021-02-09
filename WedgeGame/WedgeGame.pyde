def initializeDeck(numSuits, numCards):
    #creates a new deck
    pass

def drawCard(posX, posY, suit, number, cardImages):
    #takes position, card suit&number, image of all cards
    #draws card at position
    pass
    
def cardsNumberCheck(deckCards):
    #takes a deck of cards
    #returns true if there is enough cards
    
def getRandomCard(deckCards, numSuits, numCards):
    #takes a deck, number of suits & cards
    #returns tuple representing card (value, suit)
    
def buildAHand(deckCards, numSuits, numCards, amountCards):
    #takes deck, numSuits, numCards and num of cards to return
    #returns an array of cards the size of amountCards
    
def playerAnte(ante, playerAccount):
    #takes an ante and an account
    #returns amount after the bet

def playerBetting(bet, win, playerAccount):
    #takes a bet and an account
    #returns the amount after the bet



numSuits = 4
numCards = 13
deckCards = None

def setup():
    size(800, 600)
    
    cardImages = loadImage("playingcards.png")
    deckCards = initializeDeck(numSuits, numCards)
    
    
def draw():
    ##choosing which player
    
    ##before the player bets
    if not cardsNumberCheck(deckCards):
        deckCards = initalizeDeck(numSuits, numCards)
    playerHand = buildAHand(deckCards, numSuits, numCards, 2)
    #draw cards
    for i in range(2):
        drawCard(200 + 200*i, 100, suit, number, cardImages)
    ##the player bets
    
    ##after the player bets
    
    
    
    
    
