import turtle
import random

#Chap. 16 -------------------------------------------------------------------

# Exercise # 1

def computeFactorial(number):
    if number == 0:
        return 1
    elif number <= -1:
        return
    elif number > 1:
        number *= computeFactorial(number-1)
    return number

# Exercise # 2

def reverseList(lst):
    if len(lst) > 1:
        return (reverseList(lst[1:])+[lst[0]])
    else:
        return lst
    return lst

# Exercise # 3

def tree(branchLen,t):
    if branchLen > 5:
        newBranchLen = branchLen - 15
        width = newBranchLen/3
        randomNum = random.randint(15, 45)
        if newBranchLen < 30:
            color = "green"
        else:
            color = "brown"
        
        t.width(width)
        t.color(color)
        t.forward(branchLen)
        t.right(randomNum)
        tree(newBranchLen,t)
        
        t.width(width)
        t.color(color)
        t.left(randomNum*2)
        tree(newBranchLen,t)
        t.right(randomNum)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75,t)
    myWin.exitonclick()
    
# Exercise # 4

def findMid(pointA, pointB):
    midx = (pointA[0] + pointB[0])/2
    midy = (pointA[1] + pointB[1])/2
    
    return (midx, midy)

def generateMountain(existingTriangles, depth=0):
    if depth > 3:
        return existingTriangles
    else:
        length = len(existingTriangles)
        for i in range(length-1, length-2**depth-1, -1):
            pointOne = findMid(existingTriangles[i][0], existingTriangles[i][1])
            pointTwo = findMid(existingTriangles[i][1], existingTriangles[i][2])
            pointThree = findMid(existingTriangles[i][0], existingTriangles[i][2])
            
            existingTriangles.append([existingTriangles[i][0], pointOne, pointThree])
            existingTriangles.append([pointThree, pointTwo, existingTriangles[i][2]])

        existingTriangles = generateMountain(existingTriangles, depth+1)
    return existingTriangles

def drawMountain(mountain, t):
    for triangle in mountain:
        t.up()
        t.goto(triangle[2])
        t.down()
        for point in triangle:
            t.goto(point)
            
# Exercise # 5
def fib(index):
    if index < 0:
        return
    elif index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fib(index-1) + fib(index-2)
    
def printFib(index):
    for i in range(index+1):
        print(fib(i), end=" ")
    print("")
    
# Exercise # 6
def move(numDisks, current, goal, extra):
    if numDisks > 0:
        move(numDisks-1, current, extra, goal)
        goal.append(current.pop())
        print(current, extra, goal)
        move(numDisks-1, extra, goal, current)
    return goal

# Exercise # 7
def expandL(rulekeys, rules, string):
    if len(string) == 1:
        if string in rulekeys:
            return rules[rulekeys.index(string)]
        else:
            return string
    else:
        return expandL(rulekeys, rules, string[:-1]) + expandL(rulekeys, rules, string[-1])
       
def expand(rulekeys, rules, string, depth):
    for i in range(depth):
        string = expandL(rulekeys, rules, string)
        print(string)
    return string        
    
def drawLines(string, turtlein, distance, angle):
    for char in string:
        if char == "F":
            turtlein.forward(distance)
        elif char == "+":
            turtlein.left(angle)
        elif char == "-":
            turtlein.right(angle)
            
def draw7():
    wn = turtle.Screen()
    jim = turtle.Turtle()
    rulekeys = ['A', 'B']
    rules = ["+BF-AFA-FB+", "-AF+BFB+FA-"]
    
    string = expand(rulekeys, rules, "A", 5)
    print(string)
    drawLines(string, jim, 5, 90)
    wn.exitonclick()

# Exercise # 8

def draw8():
    wn = turtle.Screen()
    jim = turtle.Turtle()
    rulekeys = ['F']
    rules = ["F+F--F+F"]
    
    string = expand(rulekeys, rules, "F", 5)
    print(string)
    drawLines(string, jim, 5, 60)
    wn.exitonclick()
    
# Exercise # 9/10

def solveJugs(current1, capacity1, current2, capacity2, goal):
  #assume 1 is <= 2

  #if either are goal, break
  if current2 == goal:
    return
  if current1 == goal:
    current2 == 0
    print(current1, current2)
    current2 = current1
    current1 = 0
    print(current1, current2)
    return

  #if first jug empty, fill
  if current1 == 0:
    current1 = capacity1
    print(current1, current2)

  #pour into second jug
  spacein2 = capacity2 - current2
  if current1 > spacein2:
    current2 = capacity2
    current1 = current1 - spacein2
  else:
    current2 += current1
    current1 = 0
  print(current1, current2)
  
  #if second jug full, empty it
  if current2 == capacity2:
      current2 = 0
      print(current1, current2)
  
  solveJugs(current1, capacity1, current2, capacity2, goal)
   
# Exercise # 11

def mission(state, prevStates=[]):
    #state - [misonside1, canonside1, misonside2, canonside2, boatside]
    
    for field in state:
        if field < 0:
            return
        
    if state[0] < state[1] or state[2] < state[3]:
        return
    
    prevStates.append(state)
    
    if state[0] == 0 and state[1] == 0:
        print(prevStates)
        return prevStates
    
    if state[4]:
        #boat on side 1
        for i in range(3):
            for j in range(3):
                if i+j != 2:
                    continue
                else:
                    mission([state[0]-i, state[1]-j, state[2]+i, state[3]+j, not(state[4])], prevStates)
        
    else:
        #boat on side 2
        for i in range(1):
            for j in range(1):
                if i+j > 2:
                    continue
                else:
                    mission([state[0]-i, state[1]-j, state[2]+i, state[3]+j, not(state[4])], prevStates)


# Exercise # 12
import time

def moveanddraw(numDisks, current, goal, extra, turtles):
    if numDisks > 0:
        moveanddraw(numDisks-1, current, extra, goal, turtles)
        moveTurtle(turtles, current, extra, goal)
        goal.append(current.pop())
        time.sleep(0.5)
        moveanddraw(numDisks-1, extra, goal, current, turtles)
    return goal

def moveTurtle(turtles, current, extra, goal):
    turtles[current[-1]-1].goto(goal[0]*200-200, len(goal)*50-150)
    
def draw(current, extra, goal, turtles):
    allLists = [current, extra, goal]
    for i in range(len(allLists)):
        for j in range(len(allLists[i])):
            turtles[allLists[i][j]-1].goto(allLists[i][0]*200-200, j*50-150)

def draw12():
    wn = turtle.Screen()
    turA = turtle.Turtle()   
    turB = turtle.Turtle()
    turC = turtle.Turtle()
    turD = turtle.Turtle()
    turE = turtle.Turtle()
    turF = turtle.Turtle()
    
    turtles = [turA, turB, turC, turD, turE, turF]
    for i in range(6):
        turtles[i].up()
        turtles[i].shapesize(1, i+3)
        turtles[i].shape("square")
    
    A = [0, 6, 5, 4, 3, 2, 1]
    B = [1]
    C = [2]
    draw(A, C, B, turtles)
    moveanddraw(6, A, C, B, turtles)
    
    wn.exitonclick()
        
    


# Exercise # 13
def calcRow(row, col):
    if row == 0:
        return 0
    if col == 0 or col == row:
        return 1
    else:
        return calcRow(row-1, col-1) + calcRow(row-1, col)
    
def pascal(rows):
    for i in range(rows):
        for j in range(i+1):
            print(calcRow(i, j), end=' ')
        print("")
    

# Test code ---------------------

# Call code for exercise # 1

# print(computeFactorial(4))

# Call code for exercise # 2

# print(reverseList([0, 1, 2, 3, 4, 5]))

# Call code for exercise # 3

# main()

# Call code for exercise # 4

# t = turtle.Turtle()
# myWin = turtle.Screen()
# mountain = generateMountain([[(-200, -200), (0, 200), (200, -200)]])
# drawMountain(mountain, t)
# myWin.exitonclick()

# Call code for exercise # 5

# printFib(20)

# Call code for exercise # 6

# A = [6, 5, 4, 3, 2, 1]
# B = []
# C = []
# print(move(6, A, C, B))

# Call code for exercise # 7

# draw7()

# Call code for exercise # 8

# draw8()

#Call code for exercise # 9

# solveJugs(0, 3, 0, 4, 2)

#Call code for exercise # 10

# solveJugs(0, 3, 0, 5, 4)

#Call code for exercise # 11

# mission([4, 4, 0, 0, True])

# Call code for exercise # 12

# draw12()

# Call code for exercise # 13

# pascal(9)


# sorts -------------------------------------------------------------------------

# Quick Sort
def quickSort(passedList):
    length = len(passedList)
    
    if length <= 1:
        return passedList
    
    pivot = 0
    pivotValue = passedList[pivot]
    
    leftMark = 1
    rightMark = length-1
    done = False
    
    while not done:
        while leftMark <= rightMark and passedList[leftMark] <= pivotValue:
            leftMark += 1
            
        
        while passedList[rightMark] > pivotValue and leftMark <= rightMark:
            rightMark -= 1
        
        if rightMark < leftMark:
            done = True
        else:
            (passedList[leftMark], passedList[rightMark]) = (passedList[rightMark], passedList[leftMark])
        
    (passedList[pivot], passedList[rightMark]) = (passedList[rightMark], passedList[pivot])

    return quickSort(passedList[:rightMark]) + [passedList[rightMark]] + quickSort(passedList[rightMark+1:])


# Merge sort
def mergeSort(passedList):
    if len(passedList) > 1:
        mid = len(passedList)//2
        
        #sort halves
        leftHalf = passedList[:mid]
        leftHalf = mergeSort(leftHalf)
        
        rightHalf = passedList[mid:]
        rightHalf = mergeSort(rightHalf)
        
        #combine halves
        newList = []
        
        while len(leftHalf) != 0 and len(rightHalf) != 0:
            if leftHalf[0] >= rightHalf[0]:
                newList.append(rightHalf.pop(0))
            else:
                newList.append(leftHalf.pop(0))
            
            if len(leftHalf) == 0:
                newList += rightHalf
                rightHalf = []
            elif len(rightHalf) == 0:
                newList += leftHalf
                leftHalf = []
        
        return newList
    else:
        return passedList
        

# test code -------------------------

randomList = [random.randint(0, 50) for i in range(20)]

# sortList = mergeSort(randomList)

# sortList = quickSort(randomList)

# print(sortList)
# print(sorted(randomList) == sortList)

# BFS/DFS ------------------------------------------------------------------------------

def loadFileInfo( fileName ):
    file = open(  fileName )
    fileInfo = []
    text = file.readlines()


    for line in text:
        line = line.strip()
        line = line.split( " " )
        fileInfo.append( line )

    numItems = len( fileInfo )
    file.close()


    return fileInfo, numItems

dataFile, numEntries = loadFileInfo( "bfsdfs.txt" )

numHouses = int(dataFile[0][0])
numRoads = int(dataFile[0][1])
houseA = int(dataFile[0][2])
houseB = int(dataFile[0][3])
adjHouses = {}

for i in range(numHouses):
    adjHouses[i+1] = []
    
for i in range(1, numRoads+1):
    roadOne = int(dataFile[i][0])
    roadTwo = int(dataFile[i][1])
    adjHouses[roadOne].append(roadTwo)
    adjHouses[roadTwo].append(roadOne)

    
#DFS ------------------------------------------------------------------------------

def dfs(current, visited, adjList):
    visited[current-1] = True
    for house in adjHouses[current]:
        if not visited[house-1]:
            dfs(house, visited, adjList)
    
# visited = [False for i in range(numHouses)]

# dfs(houseA, visited, adjHouses)

# if visited[houseB-1]:
#     print("GO ALBERT")
# else:
#     print("NO ALBERT")

#BFS -------------------------------------------------------------------------------------

def bfs(queue, adjList, visited, distMap):
    if len(queue) == 0:
        return

    current = queue.pop(0)
    for item in adjList[current]:
        if not visited[item-1]:
            visited[item-1] = True
            distMap[item] = [distMap[current][0]+1, current]
            queue.append(item)
            
    bfs(queue, adjList, visited, distMap)


# distMap = {}
# for i in range(numHouses):
#     distMap[i+1] = []
    
# queue = [houseA]
# visited = [False for i in range(numHouses)]
# visited[houseA-1] = True
# distMap[houseA] = [0, 0]

# bfs(queue, adjHouses, visited, distMap)


# if visited[houseB-1]:
#     path = [houseB]
#     while path[-1] != 0:
#         path.append(distMap[path[-1]][1])
#     path.pop()
#     print("GO ALBERT")
#     print(path)
# else:
#     print("NO ALBERT")


# linkedlist ----------------------------------------------------------------------


def findElement(linked, head, element):
    nxt = linked[head[1]]
    while nxt[0] != element:
        nxt = linked[nxt[1]]
    return nxt

def appendElement(linked, head, element):
    newElement = [element, None]
    linked.append(newElement)
            
    nxt = linked[head[1]]
    while nxt[1] != None:
        nxt = linked[nxt[1]]
    nxt[1] = len(linked)-1
    
    return linked

def addHeadElement(linked, head, element):
    newElement = [element, linked.index(head)]
    linked.append(newElement)
    head = newElement
    return(head, linked)

def addElement(linked, head, before, element):
    newElement = [element, None]
    linked.append(newElement)
    
    place = findElement(linked, head, before)
    newElement[1] = place[1]
    place[1] = len(linked)-1
    
    return linked

def printLinked(linked, head):
    nxt = head
    while nxt[1] != None:
        print(nxt[0], end=" ")
        nxt = linked[nxt[1]]
    print(nxt[0], end=" ")
    print("")
    


# head = ["grape", None]
# linked = [["grape", None]]

# (head, linked) = addHeadElement(linked, head, "apple")
# linked = appendElement(linked, head, "banana")
# linked = addElement(linked, head, "grape", "fig")

# print(linked)
# printLinked(linked, head)


