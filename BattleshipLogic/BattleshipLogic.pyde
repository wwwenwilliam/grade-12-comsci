from Board import Board
gameState = 1 #0-menu, 1-ship placement, 2-play
playerBoard = Board(550, 0)
computerBoard = Board(0, 0)
turn = True #True-player, False-comp

def setup():
    global gameState, playerBoard, computerBoard
    size(1050, 600)
    
    #generate boards
    playerBoard.createRandomBoard()
    computerBoard.createRandomBoard()
    
    
    
    
def draw():
    #no logic in here, only graphics
    global gameState, playerBoard, computerBoard
    background(0)
    
    playerBoard.drawBoard()
    playerBoard.drawShips()
    
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
        
        computerBoard.drawBoard()
        #computerBoard.drawShips()

def mousePressed():
    global gameState, playerBoard, computerBoard
    
    if gameState == 1:
        playerBoard.mouseClickedCheck()

def mouseReleased():
    #most logic should go in here
    global gameState, playerBoard, computerBoard, turn
    
    if gameState == 0:
        pass
    if gameState == 1:
        #player places pieces
        playerBoard.mouseReleasedCheck()
        
        #add some button to set pieces (move to gameState = 2)
        
        
    elif gameState == 2:
        if turn:
            #player clicks for their turn
            clickX = (mouseX-self.x) // 50
            clickY = (mouseY-self.y) // 50
            computerBoard.fire(clickX, clickY)
            
        else:
            pass
            #player clicks anywhere (except for any buttons) to pass AI's turn
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
