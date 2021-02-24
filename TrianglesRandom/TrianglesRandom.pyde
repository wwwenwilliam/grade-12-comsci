from Triangle import Triangle
from LineSegment import LineSegment 

def setup():
    size(800, 800)
    background(0)
    textSize(30)
    stroke(255)
    strokeWeight(1)
    
line2 = LineSegment(random(800), random(800), random(800), random(800))
triangle1 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))
triangle2 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))

def loadFileInfo( fileName ):
    file = open(  fileName )
    fileInfo = []
    text = file.readlines()

    for line in text:
        line = line.strip()
        line = line.split( "," )
        fileInfo.append( line )

    numItems = len( fileInfo )
    file.close()
    return fileInfo, numItems

def turnToInt(data, numData):
    for i in range(numData):
        for j in range(1, len(data[i])):
            data[i][j] = int(data[i][j])
    return data
    
caseCounter = 0

def draw():
    background(0)
    global triangle1, triangle2, caseCounter
    delay(3000)
    
    (testCases, numOfCases) = loadFileInfo( "testcases.txt" )
    testCases = turnToInt(testCases, numOfCases)
    
    triangle1 = Triangle(testCases[caseCounter][1], testCases[caseCounter][2], testCases[caseCounter][3], testCases[caseCounter][4], testCases[caseCounter][5], testCases[caseCounter][6])
    triangle2 = Triangle(testCases[caseCounter][7], testCases[caseCounter][8], testCases[caseCounter][9], testCases[caseCounter][10], testCases[caseCounter][11], testCases[caseCounter][12])
    noFill()
    triangle1.drawTriangle()
    triangle2.drawTriangle()
    print(testCases[caseCounter][0])
    text(str(Triangle.isCollision(triangle1, triangle2)), 25, 750)
    
    if caseCounter < numOfCases - 1:
        caseCounter += 1

    '''
    noFill()
    #triangle1 = Triangle(100, 100, 50, 530, 600, 500)
    triangle1.drawTriangle()
    # triangle2 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))
    triangle2.drawTriangle()
    textSize(30)
    text(str(Triangle.isCollision(triangle1, triangle2)), 25, 750)
    '''

def mousePressed():
    global triangle1, triangle2
    triangle2 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))
    triangle1 = Triangle(random(800), random(800), random(800), random(800), random(800), random(800))
