#Chap. 16

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

import turtle
import random

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

def generatePoint(range1, range2, roughness):
    averagex = (range1[0] + range2[0])/2
    averagey = (range1[1] + range2[1])/2
    
    distx = int(abs(range1[0]-range2[0])/2)
    disty = int(abs(range1[1]-range2[1])/2)
    if distx > 50:
        distx = 50
    if disty > 50:
        disty = 50
    
    addx = random.randint(-distx, distx)*roughness
    addy = random.randint(-disty, disty)*roughness
    
    if addy < 10:
        addy = random.randint(-20, 20)
        
    return (averagex+addx, averagey+addy)

def generateSmallTri(point1, point2):
    point = generatePoint(point1, point2)
    return [point1, point2, point]

def generateMountain(existingTriangles, roughness, depth=0):
    if depth > 3:
        return existingTriangles
    else:
        for i in range(len(existingTriangles)-1, -1, -1):
            newpoint1 = generatePoint(existingTriangles[i][0], existingTriangles[i][1], roughness)
            newpoint2 = generatePoint(existingTriangles[i][1], existingTriangles[i][2], roughness)
            newpoint3 = generatePoint(existingTriangles[i][0], existingTriangles[i][2], roughness)
            existingTriangles.append([newpoint1, newpoint2, existingTriangles[i][1]])
            existingTriangles.append([newpoint2, newpoint3, existingTriangles[i][2]])
            existingTriangles.append([newpoint1, newpoint3, existingTriangles[i][0]])
            existingTriangles.append([newpoint1, newpoint2, newpoint3])
            existingTriangles.pop(i)
        
        existingTriangles = generateMountain(existingTriangles, roughness, depth+1)
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
# t.speed(0)
# myWin = turtle.Screen()
# mountain = generateMountain([[(-300, -200), (0, 200), (300, -200)]], 0.8)
# drawMountain(mountain, t)
# myWin.exitonclick()

# Call code for exercise # 5

# print(fib(20))

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
