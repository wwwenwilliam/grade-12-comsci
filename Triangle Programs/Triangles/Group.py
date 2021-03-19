from Triangle import Triangle

class Group:
    
    def __init__(self, listOfTriangles, colour):
        self.triangles = listOfTriangles
        self.count = len(listOfTriangles)
        self.colour = colour
        
    def drawGroup(self):
        fill(self.colour)
        for tri in self.triangles:
            tri.drawTriangle()
            
    def emptySelf(self):
        self.triangles = []
        self.count = 0
            
    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False
    
    @staticmethod
    def compareGroups(groupOne, groupTwo):
        #checks for collision
        #returns (bigger group, smaller group)
        isTouching = False
        for tri1 in groupOne.triangles:
            for tri2 in groupTwo.triangles:
                if Triangle.isCollision(tri1, tri2):
                   isTouching = True
       
        if isTouching:
            if groupOne.count >= groupTwo.count:
                return (groupOne, groupTwo)
            else:
                return (groupTwo, groupOne)
        else:
            return (None, None)
            
            
    def combineGroups(self, subGroup):
        for tri in subGroup.triangles:
            self.triangles.append(tri)
        
        self.count += subGroup.count
        subGroup.emptySelf() #flags for removal
       
       
       
