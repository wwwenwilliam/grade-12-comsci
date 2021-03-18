from Square import Square

class AllSquares:
    
    
    def  __init__(self):
        self.squares = []
        
    def addSquare(self, squ):
        self.squares.append(squ)
        
    def drawSquares(self):
        for squ in self.squares:
            squ.drawSquare()
            
    def moveSquares(self):
        for squ in self.squares:
            squ.moveSquare()
            
    def wallCollide(self):
        for squ in self.squares:
            if squ.x < 0:
                squ.x = 0
                squ.switchDirection("HORIZONTAL")
            elif squ.x+squ.lenx > 800:
                squ.x = 800-squ.lenx
                squ.switchDirection("HORIZONTAL")
            if squ.y < 0:
                squ.y = 0
                squ.switchDirection("VERTICAL")
            elif squ.y+squ.leny > 800:
                squ.y = 800 - squ.leny
                squ.switchDirection("VERTICAL")
            
    def squareCollide(self):
        for squ1 in self.squares:
            for squ2 in self.squares:
                if squ1 != squ2:
                    if squ1.squareCollision(squ2):
                        switch = None
                        if squ1.velx == 0:
                            switch = "VERTICAL"
                            
                        elif squ1.vely == 0:
                            switch = "HORIZONTAL"
                        
                        else:
                            direction = squ1.findDirection()
                            switch = None
                            
                            squ2pos = (squ2.x, squ2.y)
                            if direction[0] == -1:
                                if squ1.pointInSquare(squ2pos[0]+squ2.lenx, squ2pos[1]):
                                    if squ1.pointInSquare(squ2pos[0]+squ2.lenx, squ2pos[1]+squ2.leny):
                                        switch = "HORIZONTAL"

                            if direction[0] == 1:
                                if squ1.pointInSquare(squ2pos[0], squ2pos[1]):
                                    if squ1.pointInSquare(squ2pos[0], squ2pos[1]+squ2.leny):
                                        switch = "HORIZONTAL"

                            if direction[1] == 1:
                                if squ1.pointInSquare(squ2pos[0], squ2pos[1]):
                                    if squ1.pointInSquare(squ2pos[0]+squ2.lenx, squ2pos[1]):
                                        switch = "VERTICAL"

                            if direction[1] == -1:
                                if squ1.pointInSquare(squ2pos[0]+squ2.lenx, squ2pos[1]+squ2.leny):
                                    if squ1.pointInSquare(squ2pos[0], squ2pos[1]+squ2.leny):
                                        switch = "VERTICAL"
                                        
                            if switch == None:
                                lead = squ1.findLeadingPoint(direction)
                                leadLine = squ1.findLine(direction)
                                switch = squ2.findIntersect(leadLine, direction)
                                
                                if switch == None:
                                    newdirection = (-direction[0], direction[1])
                                    lead = squ1.findLeadingPoint(newdirection)
                                    leadLine = squ1.findLine(newdirection)
                                    switch = squ2.findIntersect(leadLine, direction)
                                
                                if switch == None:
                                    newdirection = (direction[0], -direction[1])
                                    lead = squ1.findLeadingPoint(newdirection)
                                    leadLine = squ1.findLine(newdirection)
                                    switch = squ2.findIntersect(leadLine, direction)
                                    
                                if switch == None:
                                    noLoop()
                                    #raise Exception("cant calc direction")
                            
                            
                            if switch == "HORIZONTAL":
                                if direction[0] == 1:
                                    squ1.x = squ2.x - squ1.lenx - 1
                                else:
                                    squ1.x = squ2.x + squ2.lenx + 1
                            elif switch == "VERTICAL":
                                if direction[1] == 1:
                                    squ1.y = squ2.y - squ1.leny - 1
                                else:
                                    squ1.y = squ2.y + squ2.leny + 1
                            
                            
                            
                        #print(switch)
                        squ1.switchDirection(switch)
                        squ1.colour = color(random(0, 255), random(0, 255), random(0, 255))
                        
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
