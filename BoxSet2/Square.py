class Square():
    dragFactor = 9999999
    mouseFactor = 2
    
    def __init__(self, x, y, lenx, leny, velx, vely):
        self.posx = x*100
        self.posy = y*100
        self.velx = velx*100
        self.vely = vely*100
        self.lenx = lenx*100
        self.leny = leny*100
        self.area = float(lenx*leny)
        self.dragged = False
        
    def drawSquare(self):
        rect(self.posx/100, self.posy/100, self.lenx/100, self.leny/100)
        
    def moveSquare(self):
        self.posx += self.velx
        self.posy += self.vely
        self.velx -= self.velx / Square.dragFactor
        self.vely -= self.vely / Square.dragFactor
        # self.posx = int(self.posx)
        # self.posy = int(self.posy)
        
    def accelerateSquare(self, x, y):
        self.velx += x
        self.vely += y
        
    def isPointin(self, x, y):
        xcollision = x*100 >= self.posx and x*100 <= self.posx + self.lenx
        ycollision = y*100 >= self.posy and y*100 <= self.posy + self.leny
        return xcollision and ycollision
    
    def setDragTrue(self, mousex, mousey):
        if self.isPointin(mousex, mousey):
            self.dragged = True
    
    def setDragFalse(self):
        self.dragged = False
    
    def mouseAcceleration(self, mousex, mousey):
        if self.dragged:
            self.accelerateSquare((mousex-(self.posx+self.lenx/2)/100)*Square.mouseFactor, (mousey-(self.posy+self.leny/2)/100)*Square.mouseFactor)
            
    def switchDirection(self, direction):
        if direction == "HORIZONTAL":
            self.velx = -self.velx
        elif direction == "VERTICAL":
            self.vely = -self.vely
            
    def wallCollision(self):
        if self.posx <= 0:
            self.posx = 1
            self.switchDirection("HORIZONTAL")
        elif self.posx + self.lenx >= 80000:
            self.posx = 79900-self.lenx
            self.switchDirection("HORIZONTAL")
        
        if self.posy <= 0:
            self.posy = 1
            self.switchDirection("VERTICAL")
        elif self.posy + self.leny >= 80000:
            self.posy = 79900-self.leny
            self.switchDirection("VERTICAL")
            
    def willCollide(self, aSquare):
        if aSquare != self:
            self.posx += self.velx
            self.posy += self.vely
            if Square.squareCollision(self, aSquare):
                self.posx -= self.velx
                self.posy -= self.vely
                return True
            else:
                self.posx -= self.velx
                self.posy -= self.vely
                return False
            
    def findDirection(self):
        return (self.velx/abs(self.velx) , self.vely/abs(self.vely))
    
    def calcLine(self, direction):
        slope = float(self.vely)/self.velx
        if direction[0] == 1:
            if direction[1] == 1:
                colpoint = (self.posx+self.lenx, self.posy+self.leny)
            else:
                colpoint = (self.posx+self.lenx, self.posy)
        else:
            if direction[1] == 1:
                colpoint = (self.posx, self.posy+self.leny)
            else:
                colpoint = (self.posx, self.posy)
        
        b = colpoint[1] - slope*colpoint[0]
        return (slope, b)
    
    def lineToTop(self, aLine):
        linetop = self.posy
        linetopintersect = (linetop - aLine[1])/aLine[0]
        if linetopintersect >= self.posx and linetopintersect <= self.posx + self.lenx:
            return True
        return False
        
    def lineToBottom(self, aLine):
        linebottom = self.posx + self.lenx
        linebottomintersect = (linebottom - aLine[1])/aLine[0]
        if linebottomintersect >= self.posx and linebottomintersect <= self.posx + self.lenx:
            return True
        return False
        
    def lineToLeft(self, aLine):
        lineleft = self.posy
        lineleftintersect = aLine[0]*lineleft + aLine[1]
        if lineleftintersect >= self.posy and lineleftintersect <= self.posy + self.leny:
            return True
        return False
        
    def lineToRight(self, aLine):
        lineright = self.posy + self.leny
        linerightintersect = aLine[0]*lineright + aLine[1]
        if linerightintersect >= self.posy and linerightintersect <= self.posy + self.leny:
            return True
        return False
    
    @staticmethod
    def findSwitch(aSquare, direction, aLine):
        switch = None
        if direction[0] == 1:
            if aSquare.lineToLeft(aLine):
                switch = "HORIZONTAL"
        else:
            if aSquare.lineToRight(aLine):
                switch = "HORIZONTAL"
        
        if direction[1] == 1:
            if aSquare.lineToTop(aLine):
                switch = "VERTICAL"
        else:
            if aSquare.lineToBottom(aLine):
                switch = "VERTICAL"
        return switch
        
    
    @staticmethod
    def squareCollision(oneSquare, twoSquare):
        xcollision = (twoSquare.posx-oneSquare.lenx+1) <= oneSquare.posx and oneSquare.posx <= twoSquare.posx + twoSquare.lenx-1
        ycollision = (twoSquare.posy-oneSquare.leny+1) <= oneSquare.posy and oneSquare.posy <= twoSquare.posy + twoSquare.leny-1
        return xcollision and ycollision
