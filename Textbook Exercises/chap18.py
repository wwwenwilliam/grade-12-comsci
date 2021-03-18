##from chapter 17 ---------------------
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
        
#-------------------------------------------------

class Rectangle:
    
    ##question 7
    def __init__(self, point, x, y):
        self.point = point
        self.x = x
        self.y = y
    
    ##question 8
    def getWidth(self):
        return self.x
    
    def getHeight(self):
        return self.y
    
    def __str__(self):
        return "Point: {} ; Width: {} ; Height {}".format(self.point, self.x, self.y)
    
    ##question 9
    def area(self):
        return self.x * self.y
    
    ##question 10
    def perimeter(self):
        return (self.x+self.y)*2
    
    ##question 11
    def transpose(self):
        (self.x, self.y) = (self.y, self.x)
        
    ##question 12
    def contains(self, point):
        if point.x >= self.point.x and point.x < self.point.x + self.x:
            if point.y >= self.point.y and point.y < self.point.y + self.y:
                return True
        return False
    
    ##question 13
    def diagonal(self):
        corner = Point(self.point.x + self.x, self.point.y + self.y)
        return self.point.distanceFromPoint(corner)
    
    ##question 14
    def collide(self, rect):
        xcollision = (rect.point.x-self.x) <= self.point.x+1 and self.point.x <= rect.point.x + rect.x-1
        ycollision = (rect.point.y-self.y) <= self.point.y+1 and self.point.y <= rect.point.y + rect.y-1
        return xcollision and ycollision
    
def test(thing1, thing2):
    if thing1 == thing2:
        print("PASS")
    else:
        print("FAIL")
    
##test code -------------------------------------------------------------------------
###question 7
r = Rectangle(Point(4, 5), 6, 5)

###question 8
##print(r.getHeight())
##print(r.getWidth())
##print(r)

###question 9
##r = Rectangle(Point(0, 0), 10, 5)
##test(r.area(), 50)

###question 10
##r = Rectangle(Point(0, 0), 10, 5)
##test(r.perimeter(), 30)

###question 11
##r = Rectangle(Point(100, 50), 10, 5)
##test(r.x, 10)
##test(r.y, 5)
##r.transpose()
##test(r.x, 5)
##test(r.y, 10)

###question 12
##r = Rectangle(Point(0, 0), 10, 5)
##test(r.contains(Point(0, 0)), True)
##test(r.contains(Point(3, 3)), True)
##test(r.contains(Point(3, 7)), False)
##test(r.contains(Point(3, 5)), False)
##test(r.contains(Point(3, 4.99999)), True)
##test(r.contains(Point(-3, -3)), False)

###question 13
##print(r)
##print(r.diagonal())

###question 14
r2 = Rectangle(Point(5, 3), 6, 5)
##print(r)
##print(r2)
##print(r.collide(r2))

r2 = Rectangle(Point(-8, 0), 4, 3)
##print(r)
##print(r2)
##print(r.collide(r2))


























