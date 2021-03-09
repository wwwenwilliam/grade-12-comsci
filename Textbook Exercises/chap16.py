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

def generatePoint(range1, range2):
    averagex = (range1[0] + range2[0])/2
    averagey = (range1[1] + range2[1])/2
    addx = random.randint(0, int(max(range1[0], range2[0])) - int(min(range1[0], range2[0])))
    addy = random.randint(0, int(max(range1[1], range2[1])) - int(min(range1[1], range2[1])))
    return (averagex+min(addx, addy), averagey+min(addx, addy))

def generateSmallTri(point1, point2):
    point = generatePoint(point1, point2)
    return [point1, point2, point]

def generateMountain(existingTriangles, depth=0):
    if depth > 2:
        return existingTriangles
    else:
        for i in range(len(existingTriangles)-1, -1, -1):
            newpoint1 = generatePoint(existingTriangles[i][0], existingTriangles[i][1])
            newpoint2 = generatePoint(existingTriangles[i][1], existingTriangles[i][2])
            newpoint3 = generatePoint(existingTriangles[i][0], existingTriangles[i][2])
            existingTriangles.append([newpoint1, newpoint2, existingTriangles[i][1]])
            existingTriangles.append([newpoint2, newpoint3, existingTriangles[i][2]])
            existingTriangles.append([newpoint1, newpoint3, existingTriangles[i][0]])
            existingTriangles.pop(i)
        
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

def solveJugs(jugOne, capOne, jugTwo, capTwo):
    pass
   
# Exercise # 11


# Exercise # 12

def moveanddraw(numDisks, current, goal, extra, turA, turB, turC):
    if numDisks > 0:
        move(numDisks-1, current, extra, goal)
        goal.append(current.pop())
        draw(current, extra, goal, turA, turB, turC)
        move(numDisks-1, extra, goal, current)
    return goal

def draw(current, extra, goal, turA, turB, turC):
    allLists = [current, extra, goal]
    for i in  range(len(allLists)):
        for disk in allLists[i]:
            if disk == 1:
                turA.goto(i*100, 100)
            elif disk == 2:
                turB.goto(i*100, 0)
            elif disk == 3:
                turC.goto(i*100, -100)

def draw12():
    wn = turtle.Screen()
    turA = turtle.Turtle()
    turA.speed(1)
    turA.up()
    turA.goto(-100, 100)
    turA.shape("square")
    turA.shapesize(1, 3)
    
    turB = turtle.Turtle()
    turB.up()
    turB.speed(1)
    turB.goto(-100, 0)
    turB.shapesize(1, 4)
    turB.shape("square")
    
    turC = turtle.Turtle()
    turC.up()
    turC.speed(1)
    turC.goto(-100, -100)
    turC.shapesize(1, 5)
    turC.shape("square")
    
    A = [3, 2, 1]
    B = []
    C = []
    moveanddraw(3, A, C, B, turA, turB, turC)
    
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
# mountain = generateMountain([[(-100, -100), (0, 200), (100, -200)]])
# drawMountain(mountain, t)
# myWin.exitonclick()

# Call code for exercise # 5

# print(fib(20))

# Call code for exercise # 6

# A = [3, 2, 1]
# B = []
# C = []
# print(move(3, A, C, B))

# Call code for exercise # 7

# draw7()

# Call code for exercise # 8

# draw8()


# Call code for exercise # 12

draw12()

# Call code for exercise # 13

# pascal(9)
