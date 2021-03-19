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
        #finds area of tri based of three points
        area=0.5*( (x1*((-y2)-(-y3))) + (x2*((-y3)-(-y1))) + (x3*((-y1)-(-y2))) )
        return abs(area)
        
    def checkPoint(self, x, y):
        #checks if point is within the triangle
        selfArea = Triangle.findArea(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
        subtri1 = Triangle.findArea(x, y, self.x2, self.y2, self.x3, self.y3)
        subtri2 = Triangle.findArea(self.x1, self.y1, x, y, self.x3, self.y3)
        subtri3 = Triangle.findArea(self.x1, self.y1, self.x2, self.y2, x, y)
        if selfArea >= subtri1+subtri2+subtri3:
            fill(0, 255, 0)
            circle(x, y, 8)
            return True
        else:
            return False
    
    @staticmethod
    def checkTrianglePoints(tri1, tri2):
        isIn = False
        #uses if (not elif) to draw circles if inside
        if tri1.checkPoint(tri2.x1, tri2.y1):
            isIn = True
        if tri1.checkPoint(tri2.x2, tri2.y2):
            isIn = True
        if tri1.checkPoint(tri2.x3, tri2.y3):
            isIn = True
        if tri2.checkPoint(tri1.x1, tri1.y1):
            isIn = True
        if tri2.checkPoint(tri1.x2, tri1.y2):
            isIn = True
        if tri2.checkPoint(tri1.x3, tri1.y3):
            isIn = True
        return isIn
        
    @staticmethod
    def isCollision(firstTriangle, secondTriangle):
        #check for line intersections
        collide = False
        for selfline in firstTriangle.lines:
            for otherline in secondTriangle.lines:
                if selfline.findIntersect(otherline) != None:
                    collide = True
        
        #checks for points
        if Triangle.checkTrianglePoints(firstTriangle, secondTriangle):
            collide = True
            
        return collide
    
    
        
        
