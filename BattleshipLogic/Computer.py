#AI

class Computer:
    
    def __init__(self, playerBoard):
        #could add modes
        self.playerBoard = playerBoard
        
    def makeMove(self):
        self.makeRandomMove()
            
    def makeRandomMove(self):
        #makes a random valid move
        randomX = int(random(0, 10))
        randomY = int(random(0, 10))
        if self.playerBoard.fire(randomX, randomY, None):
            return
        else:
            self.makeRandomMove()
        
    
