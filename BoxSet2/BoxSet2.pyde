from Square import Square
from AllSquares import AllSquares

squares = AllSquares([])

def setup():
    global squares
    size(800, 800)
    squares.addASquare(Square(0, 0, 200, 200, 0, 0))
    squares.addASquare(Square(400, 400, 100, 100, 5, 5))
    
def draw():
    global squares
    background(0)
    squares.drawSquares()
    squares.checkForMouseMove(mouseX, mouseY)
    squares.moveSquares()
    squares.checkWallCollisions()
    squares.squareCollisions()
    
def mousePressed():
    global squares
    squares.setDragTrueSquares(mouseX, mouseY)

def mouseReleased():
    global squares
    squares.setDragFalseSquares()
