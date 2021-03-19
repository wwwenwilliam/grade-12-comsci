
class Square():
    dragFactor = 1.05
    mouseFactor = 125
    
    def __init__(self, x, y, lenx, leny):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.lenx = lenx
        self.leny = leny
        self.area = float(lenx*leny)
        self.dragged = False
        
    def drawSquare(self):
        rect(self.position.x, self.position.y, self.lenx, self.leny)
        
    def moveSquare(self):
        self.position += self.velocity
        self.velocity /= Square.dragFactor
        # self.position.x = int(self.position.x)
        # self.position.y = int(self.position.y)
        
    def accelerateSquare(self, acceleration):
        self.velocity += acceleration
        
    def isPointin(self, x, y):
        xcollision = x >= self.position.x and x <= self.position.x + self.lenx
        ycollision = y >= self.position.y and y <= self.position.y + self.leny
        return xcollision and ycollision
    
    def setDragTrue(self, mousex, mousey):
        if self.isPointin(mousex, mousey):
            self.dragged = True
    
    def setDragFalse(self):
        self.dragged = False
    
    def mouseAcceleration(self, mousex, mousey):
        if self.dragged:
            self.accelerateSquare(PVector(mousex-self.position.x-(self.lenx/2), mousey-self.position.y-(self.leny/2))/Square.mouseFactor)
            
    def switchDirection(self, direction):
        if direction == "HORIZONTAL":
            self.velocity.x = -self.velocity.x
        elif direction == "VERTICAL":
            self.velocity.y = -self.velocity.y
            
    def wallCollision(self):
        if self.position.x <= 0:
            self.position.x = 1
            self.switchDirection("HORIZONTAL")
        elif self.position.x + self.lenx >= 800:
            self.position.x = 799-self.lenx
            self.switchDirection("HORIZONTAL")
        
        if self.position.y <= 0:
            self.position.y = 1
            self.switchDirection("VERTICAL")
        elif self.position.y + self.leny >= 800:
            self.position.y = 799-self.leny
            self.switchDirection("VERTICAL")
            
    @staticmethod
    def squareBounce(one, two, direction):
        #one is always top/left
        #two is to the bottom/right
        oneSpeedOriginal = one.velocity.mag()
        twoSpeedOriginal = two.velocity.mag()
        totalSpeed = oneSpeedOriginal + twoSpeedOriginal
        totalArea = one.area + two.area
        
        oneSpeedDiff = totalSpeed * (two.area/totalArea)
        twoSpeedDiff = totalSpeed * (one.area/totalArea)
        if direction == "HORIZONTAL":
            one.velocity += PVector(oneSpeedDiff, 0)
            two.velocity += PVector(-twoSpeedDiff, 0)
        elif direction == "VERTICAL":
            one.velocity += PVector(0, oneSpeedDiff)
            two.velocity += PVector(0, -twoSpeedDiff)
        
    @staticmethod
    def squareCollision(oneSquare, twoSquare):
        xcollision = (twoSquare.position.x-oneSquare.lenx+1) <= oneSquare.position.x and oneSquare.position.x <= twoSquare.position.x + twoSquare.lenx-1
        ycollision = (twoSquare.position.y-oneSquare.leny+1) <= oneSquare.position.y and oneSquare.position.y <= twoSquare.position.y + twoSquare.leny-1
        return xcollision and ycollision
