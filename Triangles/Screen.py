from Group import Group
from Triangle import Triangle

class Screen:
    
    def __init__(self, listOfGroups):
        self.groups = listOfGroups
        
    def drawGroups(self):
        for group in self.groups:
            group.drawGroup()
            
    def addTriangle(self, tri, colour):
        group = Group([tri], colour)
        self.groups.append(group)
        self.checkForOverlap()
        
    def addRandomGroup(self):
        tri = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))
        colour = color(random(255), random(255), random(255))
        self.addTriangle(tri, colour)
        
    def checkForOverlap(self):
        for group1 in self.groups:
            for group2 in self.groups:
                if group1 != group2:
                    (bigGroup, smallGroup) = Group.compareGroups(group1, group2)
                    if bigGroup != None:
                        bigGroup.combineGroups(smallGroup)
        
        for i in range(len(self.groups)-1, 0-1, -1):
            if self.groups[i].isEmpty():
                self.groups.pop(i)
        
    
