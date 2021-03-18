import math

class Point:

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)
     
    ##Exercise # 1
    def distanceFromPoint(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
    
    ##Exercise # 2
    def reflect_x(self):
        self.x = - self.x
        
    ##Exercise # 3
    def slopeFromPoint(self, point):
        if self.x-point.x == 0:
            return None
        return (self.y-point.y)/(self.x-point.x)
    
    def slopeFromOrigin(self):
        return self.slopeFromPoint(Point(0, 0))
    
    ##exercise # 4
    def get_line_to(self, point):
        m = self.slopeFromPoint(point)
        b = self.y - m*(self.x)
        return (m, b)
    
    ##exercise # 5
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
##exercise # 6
def findIntersection(lineA, lineB):
    interX = (lineB[1]-lineA[1])/(lineA[0]-lineB[0])
    interY = lineA[0]*interX + lineA[1]
    return (interX, interY)
    
def findCircle(pointA, pointB, pointC):
    #perpendicular lines
    ABmid = Point((pointA.x+pointB.x)/2, (pointA.y+pointB.y)/2)
    ABslope = - pointA.slopeFromPoint(pointB)**(-1)
    ABb = ABmid.y - ABslope*ABmid.x
    
    ACmid = Point((pointA.x+pointC.x)/2, (pointA.y+pointC.y)/2)
    ACslope = - pointA.slopeFromPoint(pointC)**(-1)
    ACb = ACmid.y - ACslope*ACmid.x
    
    circleMid = findIntersection((ABslope, ABb), (ACslope, ACb))
    circleR = pointA.distanceFromPoint(Point(circleMid[0], circleMid[1]))
    
    return(circleMid, circleR)

##test code --------------------------------------------------------------

pointOne = Point(5, 6)
pointTwo = Point(2, 3)
#exercise # 1
# print(pointOne.distanceFromPoint(pointTwo))

#exercise # 2
# pointOne.reflect_x()
# print(pointOne)

#exercise # 3
# print(pointOne.slopeFromOrigin())

#exercise # 4
# print(pointOne.get_line_to(pointTwo))

#xercise # 5
# pointOne.move(4, 4)
# print(pointOne)

#exercise # 6
pointThree = Point(0, 8)
# print(pointOne, pointTwo, pointThree)
# print(findCircle(pointOne, pointTwo, pointThree))
        
        
        