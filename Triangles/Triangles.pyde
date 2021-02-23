from Triangle import Triangle
from LineSegment import LineSegment 

def setup():
    size(800, 800)
    
    
def draw():
    background(0)
    
    stroke(255)
    strokeWeight(1)
    
    line1 = LineSegment(0, 0, 400, 500)
    line1.drawLine()
    line2 = LineSegment(random(800), random(800), random(800), random(800))
    line2.drawLine()
    print(line1.findIntersect(line2))


    
    # fill(255)
    # triangle1 = Triangle(100, 100, 50, 230, 600, 500)
    # triangle1.drawTriangle()
    
    # fill(255, 0, 0)
    # triangle2 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))
    # triangle2.drawTriangle()
    
    # print(triangle1.isCollision(triangle2))
    delay(3000)
