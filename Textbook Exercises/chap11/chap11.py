##chapter 11-file reading
def splitIntoList(file):
    student = []
    for line in file:
        currentLine = line.strip().split(" ")
        student.append(currentLine)
    return student

#Q1
file = open("studentdata.txt", 'r')

def findStuOverSix(file):
    studentsOverSix = []
    students = splitIntoList(file)

    for student in students:
        if len(student) >= 7:
            studentsOverSix.append(student[0])
    return studentsOverSix

#print(findStuOverSix(file))

file.close()

#Q2
file = open("studentdata.txt", 'r')
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

#print(findStuAverages(file))
        
file.close()

#Q3
file = open("studentdata.txt", 'r')
def findStuMinMax(file):
    students = splitIntoList(file)
    minmax = []
    for student in students:
        minmax.append([student[0], min(student[1:]), max(student[1:])])
    return minmax

#print(findStuMinMax(file))
    
file.close()

#Q4
import turtle
file = open("labdata.txt", "r")
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
    turtle.up()
    
    #draw line
    plotRegression(data, aturtle)
    
# wn = turtle.Screen()
# alex = turtle.Turtle()  
# linesin = toInt(splitIntoList(file))
# question4(linesin, alex)
# wn.exitonclick()
file.close()

#Q5
file = open("mystery.txt", "r")

def drawPicture(data, aturtle):
    for line in data:
        if line[0] == "UP":
            aturtle.up()
        elif line[0] == "DOWN":
            aturtle.down()
        else:
            aturtle.goto(int(line[0]), int(line[1]))

# wn = turtle.Screen()
# bill = turtle.Turtle()
# data = splitIntoList(file)
# drawPicture(data, bill)
# wn.exitonclick()
file.close()


