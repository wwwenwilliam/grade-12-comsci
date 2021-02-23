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
    
    def drawTriangle(self):
        triangle(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
    
    @staticmethod
    def findArea(x1, y1, x2, y2, x3, y3):
        area=0.5*( (x1*((-y2)-(-y3))) + (x2*((-y3)-(-y1))) + (x3*((-y1)-(-y2))) )
        return abs(area)
        
    def checkPoint(self, x, y):
        selfArea = Triangle.findArea(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
        subtri1 = Triangle.findArea(x, y, self.x2, self.y2, self.x3, self.y3)
        subtri2 = Triangle.findArea(self.x1, self.y1, x, y, self.x3, self.y3)
        subtri3 = Triangle.findArea(self.x1, self.y1, self.x2, self.y2, x, y)
        if selfArea >= subtri1+subtri2+subtri3:
            fill(0, 255, 0)
            circle(x, y, 5)
            return True
        else:
            return False
        
    def isCollision(self, secondTriangle):
        collide = False
        for selfline in self.lines:
            for otherline in secondTriangle.lines:
                if selfline.findIntersect(otherline) != None:
                    collide = True
                    
        if self.checkPoint(secondTriangle.x1, secondTriangle.y1):
            collide = True
        if self.checkPoint(secondTriangle.x2, secondTriangle.y2):
            collide = True
        if self.checkPoint(secondTriangle.x3, secondTriangle.y3):
            collide = True
        return collide
    
    
        
        
