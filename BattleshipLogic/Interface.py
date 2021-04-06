##classes to help with input/output

class Menu():
    ##collection of buttons
    def __init__(self, x, y, lenx, leny, buttons=[]):
        self.x = x
        self.y = y
        self.lenx = lenx
        self.leny = leny
        self.buttons = buttons
        
    def clickIsIn(self):
        #checks if mouse if within menu
        if mouseX >= self.x and mouseX < self.x + self.lenx:
            if mouseY >= self.y and mouseY < self.y + self.leny:
                return True
        return False
    
    def click(self):
        #returns which button was clicked as index of buttons
        for i in range(len(self.buttons)):
            if self.buttons[i].isClicked():
                return i
        return None
        
    def drawMenu(self):
        #draws menu
        if self.clickIsIn():
            for button in self.buttons:
                button.drawButton()
        else:
            fill(255)
            rect(self.x, self.y, self.lenx, self.leny)
            fill(0)
            textSize(40)
            text("MENU", self.x+self.lenx/2, self.y+self.leny/2)
    

class Keyboard:
    
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    
    @staticmethod
    def keyIn(string):
        #takes string, modifies it based on key that was pressed
        try:
            if key.upper() in Keyboard.ALPHABET and len(string) != 15:
                string += key.upper()
            elif key == BACKSPACE:
                if len(string) > 0:
                    string = string[:-1]
        except AttributeError:
            print("invalid key")
            
        return string

class Button:
    
    def __init__(self, x, y, lenx, leny, message=""):
        self.x = x
        self.y = y
        self.lenx = lenx
        self.leny = leny
        self.message = message
        
    def drawButton(self):
        #draws
        fill(255)
        rect(self.x, self.y, self.lenx, self.leny)
        textSize(20)
        fill(0)
        text(self.message, self.x+self.lenx/2, self.y+self.leny/2)
    
    def setMessage(self, message):
        self.message = message
        
    def isClicked(self):
        #checks if mouse is within bounds
        if mouseX >= self.x and mouseX < self.x + self.lenx:
            if mouseY >= self.y and mouseY < self.y + self.leny:
                return True
        return False
    
class Messager:
    #prints messages to screen
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.message = ""
        
    def setMessage(self, message):
        self.message = message
        
    def printMessage(self, wordSize):
        #prints message to screen
        textSize(wordSize)
        fill(255)
        text(self.message, self.x, self.y)
    
    
