import random

def getValidSelection(passedList, prompt):
    #takes a list of vaild selections
    #returns player's selection if it is valid
    validValue = input("{}".format(prompt)).upper()
    
    while True:
        if validValue in passedList:
            return validValue
        else:
            validValue = input("Try Again: ").upper()
            
def getValidNum(lowNum, highNum, prompt):
    #takes a high num, low num and a prompt
    #returns input if inbetween values
    validNum = int(input("{}".format(prompt)))
    keepGoing = (validNum < lowNum) or (validNum > highNum)
    while keepGoing:
        validNum = int(input( "Try again: " ))
        keepGoing = (validNum < lowNum) or (validNum > highNum)
    return (validNum)

def getRandomCard(deckCards, numSuits, numCards):
    #takes a deck, amount of suits and cards
    #returns a random suit and value (random card)
    while True:
        randomSuit = random.randint(0, numSuits-1)
        randomCard = random.randint(0, numCards-1)
        if deckCards[randomCard][randomSuit] == True:
            deckCards[randomCard][randomSuit] = False
            return randomCard, randomSuit
        
def lostCheck(playerNum, playerMoney):
    #takes a player's number(0 included) & list of player accounts
    #returns true & prints losing message if player is bankrupt
    if playerMoney <= 0:
        print("Player {} is bankrupt".format(playerNum+1))
        #print player accounts
        print("Player Accounts: {}".format(playerAccounts))
        return True
    else:
        return False
    
def compareTwoCards(cardOne, cardTwo, aceHighLow):
    #takes two tuples (value, suit)
    #returns true if cardOne is bigger
    if cardOne[0] == 0:
        if cardTwo[0] != 0:
            if aceHighLow == "HIGH":
                return True
            else:
                return False
        else:
            return cardOne[1] > cardTwo[1]
    if cardTwo[0] == 0:
        #cardOne is never an Ace here
        if aceHighLow == "HIGH":
            return False
        else:
            return True
    if cardOne[0] == cardTwo[0]:
        return cardOne[1] > cardTwo[1]
    else:
        return cardOne[0] > cardTwo[0]
            
def initializeDeck(numSuits, numCards):
    #returns a full deck of cards
    #I reversed this here because numbers have higher ordering precedance than suits
    deckCards = [[True] * numSuits for i in range(numCards)]
    return deckCards

def checkAmountOfCards(deckCards):
    #takes a deck of cards
    #returns true if there are enough cards
    count = 0
    threshold = 30
    for card in deckCards:
        if card:
            count += 1
    return count < threshold

def displayCard(card, title):
    #takes card (a tuple)
    #prints card to console
    print("{}: {} of {}".format(
            title, CARDVALUES[card[0]], SUITVALUES[card[1]]
            )
        )
    

##deck constants
SUITVALUES = ["DIAMONDS", "CLUBS", "HEARTS", "SPADES"]
CARDVALUES = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", 
             "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]

##setup
numPlayers = int(input("Enter number of people playing: "))
playerAccounts = [100 for i in range(numPlayers)]
ante = 10
pot = 500
numSuits = 4
numCards = 13
deckCards = initializeDeck(numSuits, numCards)
gameRunning = True

##turn
while gameRunning:
    for numPlayer in range(numPlayers):
        #check amount of cards
        if not checkAmountOfCards(deckCards):
            deckCards = initializeDeck(numSuits, numCards)
            print("Deck restocked")
        ##each player's turn
        print()
        print()
        print("Player {}'s turn".format(numPlayer+1))
        print("Your money: {}".format(playerAccounts[numPlayer]))
        #subtract ante
        playerAccounts[numPlayer] -= ante
        #generate two random cards
        randomCardOne = getRandomCard(deckCards, numSuits, numCards)
        randomCardTwo = getRandomCard(deckCards, numSuits, numCards)
        #display cards
        displayCard(randomCardOne, "Card One")
        displayCard(randomCardTwo, "Card Two")
        if randomCardOne[0] == 0 or randomCardTwo[0] == 0:
            #if a card is an ace
            #ask if ace is high or low
            validAceInputs = ["HIGH", "LOW"]
            aceHighLow = getValidSelection(validAceInputs, 
                                           "Is ace HIGH or LOW? ")
        else:
            aceHighLow = False
        #sort cards
        if compareTwoCards(randomCardOne, randomCardTwo, aceHighLow):
            bothCards = [randomCardOne, randomCardTwo]
        else:
            bothCards = [randomCardTwo, randomCardOne]
        ##player bets
        #ask if player wants to pass
        validPassInputs = ["YES", "NO"]
        doesPass = getValidSelection(validPassInputs, 
                                     "Do you want to pass? (YES/NO) ")
        if doesPass == "YES":
            lostCheck(numPlayer, playerAccounts[numPlayer])
            continue
        else:
            #ask player to bet
            print("The pot has {} dollars".format(pot))
            print("You have {} dollars".format(playerAccounts[numPlayer]))
            playerBet = getValidNum(ante, min(pot, playerAccounts[numPlayer]), 
                                    "How much would you like to bet? ")
            #generate another card and see if it's between
            randomCardThree = getRandomCard(deckCards, numSuits, numCards)
            print("Card three: {} of {}".format(
                CARDVALUES[randomCardThree[0]], SUITVALUES[randomCardThree[1]]
                )
            )
            if (compareTwoCards(randomCardThree, bothCards[1], aceHighLow) and 
                compareTwoCards(bothCards[0], randomCardThree, aceHighLow)):
                    pot -= playerBet
                    playerAccounts[numPlayer] += playerBet
                    print("You won {} dollars".format(playerBet))
            else:
                pot += playerBet
                playerAccounts[numPlayer] -= playerBet
                print("You lost {} dollars".format(playerBet))
        #see if player or pot(house) is bankrupt
        if pot <= 0 or lostCheck(numPlayer, playerAccounts[numPlayer]):
            gameRunning = False
            break
        
    
    
    
    
    
    
    
    
    
    
    
    
