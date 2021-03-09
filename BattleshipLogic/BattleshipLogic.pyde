from Board import Board
from Computer import Computer
from Messager import Messager

gameState = 2 #0-menu, 1-ship placement, 2-play
playerBoard = Board(550, 0)
computerBoard = Board(0, 0)
computer = Computer(0, playerBoard)
turnMessager = Messager(30, 560)
sinkMessager = Messager(400, 560)
turn = True #True-player, False-comp

def setup():
    global playerBoard, computerBoard
    size(1050, 600)
    
    #generate boards
    playerBoard.createRandomBoard()
    computerBoard.createRandomBoard()
    
    
    
    
def draw():
    #no logic in here, only graphics
    global gameState, playerBoard, computerBoard, turnMessager, sinkMessager
    background(0)
    
    
    
    if gameState == 0:
        pass
    elif gameState == 1:
        #draw boards
        playerBoard.drawBoard()
        playerBoard.drawShips()
        
        computerBoard.drawBoard()
        #computerBoard.drawShips()
        
        #draw button
        
        
    elif gameState == 2:
        #draw boards
        playerBoard.drawBoard()
        playerBoard.drawShips()
        playerBoard.drawHits()
        
        computerBoard.drawBoard()
        # computerBoard.drawShips()
        computerBoard.drawHits()
        
        turnMessager.printMessage(40)
        sinkMessager.printMessage(40)
        

def mousePressed():
    global gameState, playerBoard, computerBoard
    
    if gameState == 1:
        playerBoard.mouseClickedCheck()

def mouseReleased():
    #most logic should go in here
    global gameState, playerBoard, computerBoard, turn, computer, turnMessager, sinkMessager
    
    if gameState == 0:
        pass
    if gameState == 1:
        #player places pieces
        playerBoard.mouseReleasedCheck()
        
        #add some button to set pieces (move to gameState = 2)
        
        
    elif gameState == 2:
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
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
