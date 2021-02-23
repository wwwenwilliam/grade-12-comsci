from Triangle import Triangle
from LineSegment import LineSegment 

def setup():
    size(800, 800)
    
line2 = LineSegment(random(800), random(800), random(800), random(800))
triangle1 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))
triangle2 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))

def draw():
    background(0)
    global triangle1, triangle2
    stroke(255)
    strokeWeight(1)


    
    fill(255)
    #triangle1 = Triangle(100, 100, 50, 530, 600, 500)
    triangle1.drawTriangle()
    
    fill(255, 0, 0)
    # triangle2 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))
    triangle2.drawTriangle()
    
    print(triangle1.isCollision(triangle2))

def mousePressed():
    global triangle1, triangle2
    triangle2 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))
    triangle1 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))
