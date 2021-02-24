from Screen import Screen
from Triangle import Triangle
from LineSegment import LineSegment 

screen = Screen([])

def setup():
    size(800, 800)
    background(0)
    textSize(30)
    stroke(255)
    strokeWeight(1)

def draw():
    global screen
    background(0)
    screen.drawGroups()
    


def mousePressed():
    global screen
    screen.addRandomGroup()
