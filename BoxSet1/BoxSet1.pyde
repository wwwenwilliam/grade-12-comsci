from Square import Square
from AllSquares import AllSquares

squares = AllSquares([])

def setup():
    global squares
    size(800, 800)
    squares.addASquare(Square(10, 10, 400, 400))
    squares.addASquare(Square(500, 100, 100, 100))
    squares.addASquare(Square(100, 500, 100, 200))
    squares.addASquare(Square(100, 700, 50, 50))
    
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
