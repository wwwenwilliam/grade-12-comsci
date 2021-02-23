
allSquares = []
sizeLimit = 400
screenLimit = 800

def drawASquare(aSquare):
    #takes a list in form:
    #[x, y, width, length, colour]
    fill(aSquare[4])
    rect(aSquare[0], aSquare[1], aSquare[2], aSquare[3])

def squareCollision(oneSquare, twoSquare):
    xcollision = (oneSquare[0] <= twoSquare[0] + twoSquare[2]) and (oneSquare[0] + oneSquare[2] >= twoSquare[0])
    ycollision = (oneSquare[1] <= twoSquare[1] + twoSquare[3]) and (oneSquare[1] + oneSquare[3] >= twoSquare[1])
    return xcollision and ycollision

def generateRandomSquare(sizeLimit, screenLimit):
    return [random(screenLimit), random(screenLimit), random(sizeLimit), random(sizeLimit), None]

def assignColor(aSquare):
    global allSquares
    isAssigned = False
    groupNumber = -1
    for i in range(len(allSquares)):
        currentColour = allSquares[i][0][4]
        for oneSquare in allSquares[i]:
            if squareCollision(oneSquare, aSquare) and not(isAssigned):
                aSquare[4] = currentColour
                allSquares[i].append(aSquare)
                groupNumber = i
                isAssigned = True
            
    if isAssigned:
        forRemoval = []
        for i in range(len(allSquares)):
            for j in range(len(allSquares[i])):
                if squareCollision(allSquares[i][j], aSquare):
                    for k in range(len(allSquares[i])-1, 0-1, -1):
                        allSquares[i][k][4] = aSquare[4]
                        allSquares[groupNumber].append(allSquares[i][k])
                        allSquares[i].pop(k)
                    break
                        
        
        for i in range(len(allSquares)-1, 0-1, -1):
            if len(allSquares[i]) == 0:
                allSquares.pop(i)
                
    else:
        aSquare[4] = color(random(255), random(255), random(255))
        allSquares.append([aSquare])


def setup():
    size(800, 800)
    
    
def draw():
    global allSquares, sizeLimit, screenLimit
    background(0)
    
    thisSquare = generateRandomSquare(sizeLimit, screenLimit)
    assignColor(thisSquare)
    
    for i in allSquares:
        for j in i:
            drawASquare(j)
    
    delay(1000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
