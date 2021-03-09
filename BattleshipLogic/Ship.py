class Ship:
    
    shipType = [None, None, "Destroyer", "Submarine", "Cruiser", "Battleship", "Carrier"]
    shipImage = [None, None, "placeholder"]
    
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
        self.moveX = 0
        self.moveY = 0
                
    @staticmethod
    def generateRandomShip(ln, board):
        #generates a random ship
        randomDirection = bool(int(random(0, 2)))
        if randomDirection:
            randomX = int(random(0, 10-ln))
            randomY = int(random(0, 10))
        else:
            randomX = int(random(0, 10))
            randomY = int(random(0, 10-ln))
            
        randomShip = Ship(randomX, randomY, ln, randomDirection) 
        
        #if ship overlaps another, generate new ship
        if board.shipCollision(randomShip):
            return Ship.generateRandomShip(ln, board)
        else:
            return randomShip
                
    def isOnBoard(self):
        #returns true if ship is in bounds
        for squ in self.occupiedSquares:
            if squ[0] > 9 or squ[0] < 0:
                return False
            elif squ[1] > 9 or squ[1] < 0:
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
        if self.moving:
            if self.direction:
                rect(mouseX+5-25, mouseY+5-25, 50*self.ln-10, 50-10)
            else:
                rect(mouseX+5-25, mouseY+5-25, 50-10, 50*self.ln-10)
            
        else:
            if self.direction:
                rect(self.x*50+5+board.x, self.y*50+5+board.y, 50*self.ln-10, 50-10)
            else:
                rect(self.x*50+5+board.x, self.y*50+5+board.y, 50-10, 50*self.ln-10)
            
    #methods for player moving the ship ----------------------------
    
    def switchMoving(self):
        #flags/unflags the current ship as moving
        self.moving = not(self.moving)
        
    def placeShip(self, board):
        #should run when mousereleased and a ship is moving
        placedX = (mouseX-board.x) // 50
        placedY = (mouseY-board.y) // 50
        
        #flip a ship
        if placedX == self.x and placedY == self.y:
            newDirection = not(self.direction)
        else:
            newDirection = self.direction
       
        #there's probably a better way to check for validity without making new object
        newShip = Ship(placedX, placedY, self.ln, newDirection)
        isValid = True
        if not newShip.isOnBoard():
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
    
    def hit(self, clickX, clickY):
        if self.isPointOnShip(clickX, clickY):
            if self.direction:
                self.hits[clickX-self.x] = True
            else:
                self.hits[clickY-self.y] = True
            
            if self.isSunk():
                print("{} sunk".format(Ship.shipType[self.ln]))
                
    def isSunk(self):
        for hit in self.hits:
            if not hit:
                return False
        return True
    
    
        
