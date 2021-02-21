##chapter 11-file reading
def splitIntoList(file):
    #used for multiple questions
    student = []
    for line in file:
        currentLine = line.strip().split(" ")
        student.append(currentLine)
    return student

# Exercise # 1-------------------------------------------

def findStuOverSix(file):
    studentsOverSix = []
    students = splitIntoList(file)

    for student in students:
        if len(student) >= 7:
            studentsOverSix.append(student[0])
    return studentsOverSix

# Exercise # 2-------------------------------------------------

def calcAverage(passedList):
    numSum = 0
    for i in passedList:
        numSum += int(i)
    return numSum/len(passedList)
        
def findStuAverages(file):
    students = splitIntoList(file)
    averages = []
    for student in students:
        averages.append([student[0], calcAverage(student[1:])])
    return averages

# Exercise # 3--------------------------------------

def findStuMinMax(file):
    students = splitIntoList(file)
    minmax = []
    for student in students:
        minmax.append([student[0], min(student[1:]), max(student[1:])])
    return minmax

# Exercise # 4------------------------------------------------

def toInt(lines):
    for i in lines:
        for j in range(len(i)):
            i[j] = int(i[j])
    return lines

def findAverages(data):
    xdata = []
    ydata = []
    length = len(data)
    for i in data:
        xdata.append(i[0])
        ydata.append(i[1])
    return (sum(xdata)/length, sum(ydata)/length)
    
def plotRegression(numbers, aturtle):
    (xaverage, yaverage) = findAverages(numbers)
    n = len(numbers)
    m = sum([number[0]*number[1]-n*xaverage*yaverage for number in numbers])/sum([number[0]**2-n*xaverage**2 for number in numbers])
    
    aturtle.up()
    for i in range(-50, 150):
        aturtle.goto(i, yaverage+m*(i-xaverage))
        aturtle.down()

def drawAxis(data, aturtle):
    aturtle.goto(500, 0)
    aturtle.goto(-500, 0)
    aturtle.goto(0, 0)
    aturtle.goto(0, 500)
    aturtle.goto(0, -500)

def drawPoints(points, aturtle):
    for point in points:
        aturtle.up()
        aturtle.goto(point[0], point[1])
        aturtle.down()
        aturtle.forward(1)
        
def question4(data, aturtle):
    #draw axis&points
    drawAxis(data, aturtle)
    drawPoints(data, aturtle)
    aturtle.up()
    
    #draw line
    plotRegression(data, aturtle)
    
# Exercise # 5---------------------------------------

def drawPicture(data, aturtle):
    for line in data:
        if line[0] == "UP":
            aturtle.up()
        elif line[0] == "DOWN":
            aturtle.down()
        else:
            aturtle.goto(int(line[0]), int(line[1]))

# ________________________________________

file = open("studentdata.txt", 'r')
# Call code for Exercise 1--------------
# print(findStuOverSix(file))

# Call code for Exercise 2--------------
# print(findStuAverages(file))

# Call code for Exercise 3--------------
# print(findStuMinMax(file))

file.close()

# Call code for Exercise 4---------------

import turtle
file = open("labdata.txt", "r")

# wn = turtle.Screen()
# alex = turtle.Turtle()  
# linesin = toInt(splitIntoList(file))
# question4(linesin, alex)
# wn.exitonclick()

file.close()

# Call code for Exercise 5-----------------

file = open("mystery.txt", "r")

# wn = turtle.Screen()
# bill = turtle.Turtle()
# data = splitIntoList(file)
# drawPicture(data, bill)
# wn.exitonclick()

file.close()
