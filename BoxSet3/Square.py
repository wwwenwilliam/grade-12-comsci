

class Square:
    
    def __init__(self, x, y, lenx, leny, velx, vely):
        self.x = x
        self.y = y
        self.lenx = lenx
        self.leny = leny
        self.velx = velx
        self.vely = vely
        self.direction = [None, None]
        self.colour = color(random(0, 255), random(0, 255), random(0, 255))
        
    def drawSquare(self):
        fill(self.colour)
        rect(self.x, self.y, self.lenx, self.leny)
        
    def moveSquare(self):
        self.x += self.velx
        self.y += self.vely
        
    def predictPos(self):
        return (self.x+self.velx, self.y+self.vely)
    
    def pointInSquare(self, x, y):
        position = self.predictPos()
        xcollision = x >= position[0] and x < position[0] + self.lenx
        ycollision = y >= position[1] and y < position[1] + self.leny
        return xcollision and ycollision
    
    def switchDirection(self, switch):
        if switch == "HORIZONTAL":
            self.velx = -self.velx
        elif switch == "VERTICAL":
            self.vely = -self.vely
    
    def findDirection(self):
        if self.velx == 0:
            self.direction[0] = 0
            self.direction[1] = self.vely // abs(self.vely)
        elif self.vely == 0:
            self.direction[1] = 0
            self.direction[0] = self.velx // abs(self.velx)
        else:
            self.direction = [self.velx // abs(self.velx), self.vely // abs(self.vely)]
        return self.direction
        
    def findLine(self, direction):
        #should not be called w/ velx or vely = 0
        slope = float(self.vely)/self.velx
        if direction[0] == 1:
            if direction[1] == 1:
                colpoint = (self.x+self.lenx, self.y+self.leny)
            else:
                colpoint = (self.x+self.lenx, self.y)
        else:
            if direction[1] == 1:
                colpoint = (self.x, self.y+self.leny)
            else:
                colpoint = (self.x, self.y)
        
        b = colpoint[1] - slope*colpoint[0]
        return (slope, b)
    
    def findLeadingPoint(self, direction):
        if direction[0] == 1:
            if direction[1] == 1:
                return (self.x+self.lenx, self.y+self.leny)
            else:
                return (self.x+self.lenx, self.y)
        elif direction[1] == -1:
            if direction[1] == 1:
                return (self.x, self.y+self.leny)
            else:
                return (self.x, self.y)
            
    def findIntersect(self, aline, direction):
        linever = None
        linehor = None
        if direction[1] == 1:
            linever = self.y
        else:
            linever = self.y + self.leny
        
        if direction[0] == 1:
            linehor = self.x
        else:
            linehor = self.x + self.lenx
            
        #lines shouldn't ever be parallel
        verInter = (linever - aline[1]) / aline[0]
        if verInter >= self.x and verInter <= self.x + self.lenx:
            return "VERTICAL"
        
        horInter = aline[0]*linehor + aline[1]
        if horInter >= self.y and horInter <= self.y + self.leny:
            return "HORIZONTAL"
        
        return None
        
        
    def squareCollision(self, twoSquare):
        onePos = self.predictPos()
        twoPos = (twoSquare.x, twoSquare.y)
        
        xcollision = (twoPos[0]-self.lenx+1) <= onePos[0] and onePos[0] <= twoPos[0] + twoSquare.lenx-1
        ycollision = (twoPos[1]-self.leny+1) <= onePos[1] and onePos[1] <= twoPos[1] + twoSquare.leny-1
        return xcollision and ycollision
    
    
        
    
        
    
