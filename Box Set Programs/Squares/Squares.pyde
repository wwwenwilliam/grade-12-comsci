
allSquares = []
sizeLimit = 400
screenLimit = 800
count = 0

def drawASquare(aSquare):
    #takes a list in form:
    #[x, y, width, length, colour]
    fill(aSquare[4])
    rect(aSquare[0], aSquare[1], aSquare[2], aSquare[3])

def squareCollision(oneSquare, twoSquare):
    xcollision = (twoSquare[0]-oneSquare[2]+1) <= oneSquare[0] and oneSquare[0] <= twoSquare[0]+twoSquare[2]-1
    ycollision = (twoSquare[1]-oneSquare[3]+1) <= oneSquare[1] and oneSquare[1] <= twoSquare[1]+twoSquare[3]-1
    return xcollision and ycollision

def generateRandomSquare(sizeLimit, screenLimit):
    return [random(screenLimit), random(screenLimit), random(sizeLimit), random(sizeLimit), None]

def assignColor(aSquare, allSquares):
    touchedGroups = []
    for i in range(len(allSquares)):
        for oneSquare in allSquares[i]:
            if squareCollision(oneSquare, aSquare):
                touchedGroups.append(i)
                break
    
    if len(touchedGroups) > 0:
        biggestGroup = touchedGroups[0]
        for i in touchedGroups:
            if len(allSquares[i]) > len(allSquares[biggestGroup]):
                biggestGroup = i
                
        dominantGroup = allSquares[touchedGroups[0]]
        dominantColour = dominantGroup[0][4]
        
        aSquare[4] = dominantColour
        dominantGroup.append(aSquare)
        
        for i in touchedGroups:
            if allSquares[i] == dominantGroup:
                continue
            for oneSquare in allSquares[i]:
                oneSquare[4] = dominantColour
            dominantGroup += allSquares[i]
            allSquares[i] = []
            
        for i in range(len(allSquares)-1, 0-1, -1):
            if len(allSquares[i]) == 0:
                allSquares.pop(i)
    else:
        aSquare[4] = color(random(255), random(255), random(255))
        allSquares.append([aSquare])

    return allSquares


def setup():
    size(800, 800)
    
    
def draw():
    global allSquares, sizeLimit, screenLimit, count
    background(0)
    
    thisSquare = generateRandomSquare(sizeLimit, screenLimit)
    allSquares = assignColor(thisSquare, allSquares)
    
    for i in allSquares:
        for j in i:
            drawASquare(j)
    
    count += 1
    if count == 10:
        print(allSquares)
        noLoop()
    delay(1000)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
