from AllSquares import AllSquares
from Square import Square


squares = AllSquares()


squares.addSquare(Square(140, 100, 50, 50, 5, 8))
squares.addSquare(Square(500, 400, 100, 200, 4, 8))
squares.addSquare(Square(400, 600, 100, 100, 7, 4))
squares.addSquare(Square(100, 600, 100, 100, 2, 3))

'''
squares.addSquare(Square(140, 500, 50, 50, 5, -8))
squares.addSquare(Square(500, 500, 100, 200, -4, -8))
'''


def setup():
    size(800, 800)

def draw():
    background(0)
    global squares
    
    squares.drawSquares()
    squares.moveSquares()
    squares.wallCollide()
    squares.squareCollide()
    
def mouseClicked():
    noLoop()
