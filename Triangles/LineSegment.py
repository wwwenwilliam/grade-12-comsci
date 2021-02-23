class LineSegment:
    
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.bound1 = min(x1, x2)
        self.bound2 = max(x1, x2)
        self.a = y1-y2
        self.b = x2-x1
        self.c = (x1-x2)*y1 + (y2-y1)*x1
        
    def findIntersect(self, secondSegment):
        if self.a == secondSegment.a and self.b == secondSegment.b and self.c == secondSegment.c:
            return "Same line"
        if (self.a*secondSegment.b - secondSegment.a*self.b) != 0:
            xintersect = (self.b*secondSegment.c - secondSegment.b*self.c)/(self.a*secondSegment.b - secondSegment.a*self.b)
        else:
            #parallel lines
            return None
        if xintersect >= self.bound1 and xintersect <= self.bound2 and xintersect >= secondSegment.bound1 and xintersect <= secondSegment.bound2:
            yintersect = -(self.a*xintersect+self.c)/self.b
            fill(0, 255, 0)
            circle(xintersect, yintersect, 5)
            return (xintersect, yintersect)
        else:
            return None
        
    def drawLine(self):
        line(self.x1, self.y1, self.x2, self.y2)
