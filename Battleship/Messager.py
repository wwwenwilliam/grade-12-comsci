#exists to print messages to screen

class Messager:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.message = ""
        
    def setMessage(self, message):
        self.message = message
        
    def printMessage(self, wordSize):
        textSize(wordSize)
        fill(255)
        text(self.message, self.x, self.y)
