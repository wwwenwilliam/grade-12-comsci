class Button:
    
    def __init__(self, x, y, lenx, leny):
        self.x = x
        self.y = y
        self.lenx = lenx
        self.leny = leny
        self.message = ""
        
    def drawButton(self):
        fill(255)
        rect(self.x, self.y, self.lenx, self.leny)
        textSize(20)
        fill(0)
        text(self.message, self.x+self.lenx/2-len(self.message)*10, self.y+self.leny/2)
    
    def setMessage(self, message):
        self.message = message
        
    def isClicked(self):
        if mouseX >= self.x and mouseX < self.x + self.lenx:
            if mouseY >= self.y and mouseY < self.y + self.leny:
                return True
        return False
