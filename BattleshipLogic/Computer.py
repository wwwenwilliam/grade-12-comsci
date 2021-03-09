#AI

class Computer:
    
    def __init__(self, mode, playerBoard):
        #could add modes
        self.mode = mode
        self.playerBoard = playerBoard
        
    def makeMove(self):
        if self.mode == 0:
            self.makeRandomMove()
            
            
    def makeRandomMove(self):
        randomX = int(random(0, 10))
        randomY = int(random(0, 10))
        if self.playerBoard.fire(randomX, randomY, None):
            return
        else:
            self.makeRandomMove()
        
    
