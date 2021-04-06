
class Ship:
    
    shipType = [None, None, "Destroyer", "Submarine", "Cruiser", "Battleship", "Carrier"]
    
    def __init__(self, x, y, ln, direction):
        self.x = x
        self.y = y
        self.ln = ln #length of ship
        self.direction = direction #VERTICAL - True /HORIZONTAL - False
        self.occupiedSquares = []
        self.hits = [False for i in range(ln)]
        
        for i in range(ln):
            if direction:
                self.occupiedSquares.append([x+i, y])
            else:
                self.occupiedSquares.append([x, y+i])
                
        #stores info for moving the ship
        self.moving = False
                
    @staticmethod
    def generateRandomShip(ln, board):
        #generates a random ship
        randomDirection = bool(int(random(0, 2)))
        if randomDirection:
            randomX = int(random(0, board.getSizeX()-ln))
            randomY = int(random(0, board.getSizeY()))
        else:
            randomX = int(random(0, board.getSizeX()))
            randomY = int(random(0, board.getSizeY()-ln))
            
        randomShip = Ship(randomX, randomY, ln, randomDirection) 
        
        #if ship overlaps another, generate new ship
        if board.shipCollision(randomShip):
            return Ship.generateRandomShip(ln, board)
        else:
            return randomShip
                
    def isOnBoard(self, board):
        #returns true if ship is in bounds
        for squ in self.occupiedSquares:
            if squ[0] > board.getSizeX()-1 or squ[0] < 0:
                return False
            elif squ[1] > board.getSizeY()-1 or squ[1] < 0:
                return False
        return True
    
    def isPointOnShip(self, x, y):
        #checks if a point is on the ship
        for squ in self.occupiedSquares:
            if squ[0] == x and squ[1] == y:
                return True
        return False
    
    def drawShip(self, board):
        #draws ship
        fill(100)
        squareSize = board.getSquSize()
        if self.moving:
            if self.direction:
                rect(mouseX+5-squareSize/2, mouseY+5-squareSize/2, squareSize*self.ln-10, squareSize-10)
            else:
                rect(mouseX+5-squareSize/2, mouseY+5-squareSize/2, squareSize-10, squareSize*self.ln-10)
            fill(75)
            for squ in self.occupiedSquares:
                circle(mouseX+squareSize*(squ[0]-self.x), mouseY+squareSize*(squ[1]-self.y), squareSize/2)
            
        else:
            if self.direction:
                rect(self.x*squareSize+5+board.x, self.y*squareSize+5+board.y, squareSize*self.ln-10, squareSize-10)
            else:
                rect(self.x*squareSize+5+board.x, self.y*squareSize+5+board.y, squareSize-10, squareSize*self.ln-10)
            fill(75)
            for squ in self.occupiedSquares:
                circle(squareSize*squ[0]+board.x+squareSize/2, squareSize*squ[1]+board.y+squareSize/2, squareSize/2)
            
    #methods for player moving the ship ----------------------------
    
    def switchMoving(self):
        #flags/unflags the current ship as moving
        self.moving = not(self.moving)
        
    def placeShip(self, board):
        #should run when mousereleased and a ship is moving
        #checks if a new position is valid, updates to new position if valid
        placedX = (mouseX-board.x) // board.getSquSize()
        placedY = (mouseY-board.y) // board.getSquSize()
        
        #flip a ship
        if placedX == self.x and placedY == self.y:
            newDirection = not(self.direction)
        else:
            newDirection = self.direction
       
        #there's probably a better way to check for validity without making new object
        newShip = Ship(placedX, placedY, self.ln, newDirection)
        isValid = True
        if not newShip.isOnBoard(board):
            isValid = False
        if board.shipCollision(newShip):
            isValid = False
            
        if isValid:
            self.x = placedX
            self.y = placedY
            self.direction = newShip.direction
            self.occupiedSquares = newShip.occupiedSquares
            
        del(newShip)
        
    #methods for game ------------------------------------------
    
    def hit(self, clickX, clickY, message):
        #checks if a move hit this ship
        #updates own logic and a messenger if hit
        if self.isPointOnShip(clickX, clickY):
            if self.direction:
                self.hits[clickX-self.x] = True
            else:
                self.hits[clickY-self.y] = True
            
            if self.isSunk() and message != None:
                message.setMessage("{} sunk".format(Ship.shipType[self.ln]))
                
    def isSunk(self):
        #checks if sunk
        for hit in self.hits:
            if not hit:
                return False
        return True
    
    
        
