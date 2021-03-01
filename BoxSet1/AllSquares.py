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
                    if Square.squareCollision(squ1, squ2):
                        if abs(squ1.position.x - (squ2.position.x-squ1.lenx)) <= AllSquares.tolerance:
                            Square.squareBounce(squ2, squ1, "HORIZONTAL")
                        elif abs(squ1.position.x - (squ2.position.x+squ2.lenx)) <= AllSquares.tolerance:
                            Square.squareBounce(squ1, squ2, "HORIZONTAL")
                        
                        if abs(squ1.position.y - (squ2.position.y-squ1.leny)) <= AllSquares.tolerance:
                            Square.squareBounce(squ2, squ1, "VERTICAL")
                        elif abs(squ1.position.y - (squ2.position.y+squ2.leny)) <= AllSquares.tolerance:
                            Square.squareBounce(squ1, squ2, "VERTICAL")

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
