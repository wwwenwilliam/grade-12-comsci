from Board import Board
from Computer import Computer
from Messager import Messager
from Button import Button

gameState = 0 #0-menu, 1-ship placement, 2-play
playerBoard = Board(550, 0)
computerBoard = Board(0, 0)
computer = Computer(0, playerBoard)

turn = True #True-player, False-comp

turnMessager = Messager(30, 560)
sinkMessager = Messager(400, 560)
bottomRightButton = Button(750, 510, 200, 80)

def setup():
    global playerBoard, computerBoard
    size(1050, 600)
    
    #generate boards
    playerBoard.createRandomBoard()
    computerBoard.createRandomBoard()
    
    
    
    
def draw():
    #no logic in here, only graphics
    global gameState, playerBoard, computerBoard, turnMessager, sinkMessager, bottomRightButton
    background(0)
    
    
    
    if gameState == 0:
        pass
    elif gameState == 1:
        #draw boards
        playerBoard.drawBoard()
        playerBoard.drawShips()
        
        computerBoard.drawBoard()
        #computerBoard.drawShips()
        
        #draw message
        turnMessager.printMessage(40)
        
        #draw button
        bottomRightButton.drawButton()
        
    elif gameState == 2:
        #draw boards
        playerBoard.drawBoard()
        playerBoard.drawShips()
        playerBoard.drawHits()
        
        computerBoard.drawBoard()
        # computerBoard.drawShips()
        computerBoard.drawHits()
        
        #draw any messages
        turnMessager.printMessage(40)
        sinkMessager.printMessage(40)
        
        #draw button
        bottomRightButton.drawButton()
        

def mousePressed():
    global gameState, playerBoard, computerBoard
    
    if gameState == 1:
        playerBoard.mouseClickedCheck()

def mouseReleased():
    #most logic should go in here
    global gameState, playerBoard, computerBoard, turn, computer, turnMessager, sinkMessager, bottomRightButton
    
    if gameState == 0:
        
        #set buttons message to "Ready" before going to gameState = 1
        #temp code
        bottomRightButton.setMessage("Ready")
        turnMessager.setMessage("Place your ships")
        gameState = 1
        
    if gameState == 1:
        if bottomRightButton.isClicked(): #button takes priority
            bottomRightButton.setMessage("Reset")
            turnMessager.setMessage("Player's Turn")
            gameState = 2
        else:
            #player places pieces
            playerBoard.mouseReleasedCheck()
        
        
    elif gameState == 2:
        if bottomRightButton.isClicked():
            playerBoard = Board(550, 0)
            computerBoard = Board(0, 0)
            computer = Computer(0, playerBoard)
            bottomRightButton.setMessage("Ready")
            turnMessager.setMessage("Place your ships")
            turn = True
            
            playerBoard.createRandomBoard()
            computerBoard.createRandomBoard()
            
            gameState = 1
            
            
        else:
            
            if turn:
                #player clicks for their turn
                sinkMessager.setMessage("")
                if computerBoard.clickToFire(sinkMessager):
                    
                    turnMessager.setMessage("Computer's Turn")
                    
                    if computerBoard.checkLoss():
                        turnMessager.setMessage("Player Wins")
                        
                    turn = not(turn)
                    
                
            else:
                #player clicks anywhere to pass AI's turn
                #will need to add a check if buttons are added
                computer.makeMove()
                
                turnMessager.setMessage("Player's Turn")
                
                if playerBoard.checkLoss():
                    turnMessager.setMessage("Computer Wins")
                    
                turn = not(turn)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
