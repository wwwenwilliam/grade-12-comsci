
class PlayerInfo:
    
    def __init__(self):
        self.name = ""
        self.score = 0
        
    def displayName(self, x, y):
        #prints name to screen
        textSize(40)
        text(self.name, x, y)
