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
    if playerMoney < 0:
        print("Player {} is bankrupt".format(playerNum+1))
        #print player accounts
        print("Player Accounts: {}".format(playerAcccounts))
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
            


##setup for cards/deck
numSuits = 4
numCards = 13
#I reversed this here because numbers have higher ordering precedance than suits
deckCards = [[True] * numSuits for i in range(numCards)]
suitValue = ["DIAMONDS", "CLUBS", "HEARTS", "SPADES"]
cardValue = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", 
             "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]

##setup for money
numPlayers = int(input("Enter number of people playing: "))

playerAccounts = [1000 for i in range(numPlayers)]
ante = 100
pot = 500

##turn
while True:
    for numPlayer in range(numPlayers):
        #if player is bankrupt, move to next
        if playerAccounts[numPlayer] < 0:
            continue
        #each player's turn
        print("Player {}'s turn".format(numPlayer+1))
        print("Your money: {}".format(playerAccounts[numPlayer]))
        #subtract ante
        playerAccounts[numPlayer] -= 100
        #ask if ace is high or low
        validAceInputs = ["HIGH", "LOW"]
        aceHighLow = getValidSelection(validAceInputs, 
                                       "Is ace HIGH or LOW? ")       
        #generate two random cards
        randomCardOne = getRandomCard(deckCards, numSuits, numCards)
        randomCardTwo = getRandomCard(deckCards, numSuits, numCards)
        #sort cards
        if compareTwoCards(randomCardOne, randomCardTwo, aceHighLow):
            bothCards = [randomCardOne, randomCardTwo]
        else:
            bothCards = [randomCardTwo, randomCardOne]
        print("Card one: {} of {}".format(
            cardValue[bothCards[0][0]], suitValue[bothCards[0][1]]
            )
        )
        print("Card two: {} of {}".format(
            cardValue[bothCards[1][0]], suitValue[bothCards[1][1]]
            )
        )
        #ask if player wants to pass
        validPassInputs = ["YES", "NO"]
        doesPass = getValidSelection(validPassInputs, 
                                     "Do you want to pass? (YES/NO) ")
        if doesPass == "YES":
            lostCheck(numPlayer, playerAccounts[numPlayer])
            print()
            print()
            continue
        else:
            #ask player to bet
            print("The pot has {} dollars".format(pot))
            playerBet = getValidNum(ante, pot, 
                                    "How much would you like to bet? ")
            #generate another card and see if it's between
            randomCardThree = getRandomCard(deckCards, numSuits, numCards)
            print("Card three: {} of {}".format(
                cardValue[randomCardThree[0]], suitValue[randomCardThree[1]]
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
        #see if player is bankrupt
        lostCheck(numPlayer, playerAccounts[numPlayer])
        print()
        print()
              
        
    
    
    
    
    
    
    
    
    
    
    
    
