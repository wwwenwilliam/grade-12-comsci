#mostly exists to handle graphics
#some useful functionality though
class Ship:
    #accessed via ln of ship
    shipType = [None, None, "Destroyer", "Submarine", "Cruiser", "Battleship", "Carrier"]
    shipImage = [None, None, "placeholder", "placeholder", "placeholder", "placeholder", "placeholder"]
    
    
    def __init__(x, y, ln, direction):
        self.x = x #position of first square of ship
        self.y = y
        self.ln = ln #length/type of ship
        self.direction = direction #direction of the "tail" of the ship #"LEFT", "RIGHT", "UP", "DOWN"
        self.occupiedSquares = []
        self.hits = [False for i in range(ln)]
        
        if direction == "RIGHT":
            self.occupiedSquares = [(x+i, y) for i in range(ln)]
        elif direction == "LEFT":
            self.occupiedSquares = [(x-i, y) for i in range(ln)]
        elif direction == "UP":
            self.occupiedSquares = [(x, y+i) for i in range(ln)]
        else:
            self.occupiedSquares = [(x, y-i) for i in range(ln)]
    
    def drawShip(self):
        #draws ship to screen
        pass
        
    def hit(self, x, y):
        #checks if ship is hit
        #takes x, y of shot; returns True if hit and False if not
        for i in range(self.ln):
            if x == self.occupiedSquares[i][0] and y == self.occupiedSquares[i][0]:
                self.hits[i] = True
                return True
        return False
        
    def isSunk(self):
        #checks if ship is sunken
        for hit in self.hits:
            if hit == False:
                return False
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
