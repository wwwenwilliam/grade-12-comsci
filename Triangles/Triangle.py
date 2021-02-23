from LineSegment import LineSegment 

class Triangle:
    
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        
        self.line1 = LineSegment(x1, y1, x2, y2)
        self.line2 = LineSegment(x2, y2, x3, y3)
        self.line3 = LineSegment(x1, y1, x3, y3)
        self.lines = [self.line1, self.line2, self.line3]
        
    def isCollision(self, secondTriangle):
        collide = False
        for selfline in self.lines:
            for otherline in secondTriangle.lines:
                if selfline.findIntersect(otherline) != None:
                    collide = True
        return collide
    
    def drawTriangle(self):
        triangle(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
