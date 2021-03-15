from Square import Square

class AllSquares:
    
    def __init__(self, squares):
        self.squares = squares
        
    def addASquare(self, asquare):
        self.squares.append(asquare)
        
    def drawSquares(self):
        for squ in self.squares:
            squ.drawSquare()
        
    def moveSquares(self):
        for squ in self.squares:
            squ.moveSquare()
            
    def setDragTrueSquares(self, mousex, mousey):
        for squ in self.squares:
            squ.setDragTrue(mousex, mousey)
            
    def setDragFalseSquares(self):
        for squ in self.squares:
            squ.setDragFalse()
    
    def checkForMouseMove(self, mousex, mousey):
        for squ in self.squares:
            squ.mouseAcceleration(mousex, mousey)
            
    def checkWallCollisions(self):
        for squ in self.squares:
            squ.wallCollision()
            
    def squareCollisions(self):
        for squ1 in self.squares:
            for squ2 in self.squares:
                if squ1 != squ2:
                    if squ1.willCollide(squ2): 
                        squ1direction = None
                                            
                        if squ1.velx == 0:
                            switch = "VERTICAL"
                        elif squ1.vely == 0:
                            switch = "HORIZONTAL"
                        else:
                            squ1direction = squ1.findDirection()
                            print(squ1direction)
                            squ1line = squ1.calcLine(squ1direction)
                            switch = Square.findSwitch(squ2, squ1direction, squ1line)
                                    
                            if switch == None:
                                squ1direction2 = (squ1direction[0], -squ1direction[1])
                                squ1line2 = squ1.calcLine(squ1direction2)
                                switch = Square.findSwitch(squ2, squ1direction, squ1line2)
                            
                            if switch == None:
                                squ1direction3 = (-squ1direction[0], squ1direction[1])
                                squ1line3 = squ1.calcLine(squ1direction3)
                                switch = Square.findSwitch(squ2, squ1direction, squ1line3)
                        
                        
                        if squ1direction != None:
                            if switch == "HORIZONTAL":
                                if squ1direction[0] == 1:
                                    squ1.posx = squ2.posx - squ1.lenx
                                else:
                                    squ1.posx = squ2.posx + squ2.lenx
                            else:
                                if squ1direction[1] == 1:
                                    squ1.posy = squ2.posy - squ1.leny
                                else:
                                    squ1.posy = squ2.posy + squ2.lenx
                        
                        print(switch)
                        squ1.switchDirection(switch)
                        squ2.switchDirection(switch)
                        
                        
        
    
        
        
        
        
        
