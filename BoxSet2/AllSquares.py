from Square import Square

class AllSquares:
    tolerance = 20
    
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
                        if squ1.velx == 0:
                            switch = "HORIZONTAL"
                        elif squ1.vely == 0:
                            switch = "VERTICAL"
                        else:
                            squ1direction = squ1.findDirection()
                            squ1line = squ1.calcLine(squ1direction)
                            switch = None
                            if squ1direction[0] == 1:
                                if squ2.lineToLeft(squ1line):
                                    switch = "HORIZONTAL"
                            else:
                                if squ2.lineToRight(squ1line):
                                    switch = "HORIZONTAL"
                            
                            if squ1direction[1] == 1:
                                if squ2.lineToTop(squ1line):
                                    switch = "VERTICAL"
                            else:
                                if squ2.lineToBottom(squ1line):
                                    switch = "VERTICAL"

                            
                        squ1.switchDirection(switch)
                        
                        
        
    
        
        
        
        
        
