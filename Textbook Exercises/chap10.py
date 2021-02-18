## 10
def countfivelenwords(passedList):
    count = 0
    for word in passedList:
        if len(word) == 5:
            count += 1
    return count

#print(countfivelenwords(["hello", "bye", "hi", "words"]))

## 11
def uptoevenSum(passedList):
    numSum = 0
    for num in passedList:
        if num % 2 == 0:
            break
        numSum += num
    return numSum

#print(uptoevenSum([1, 3, 4, 5]))

## 12
def uptosam(passedList):
    count = 0
    for word in passedList:
        count += 1
        if word == "sam":
            break
    return count

#print(uptosam(["hi", "hi", "hi", "sam", "hi"]))

## 13
#count
def mycount(obj, passedList):
    count = 0
    for thing in passedList:
        count += 1
        if thing == obj:
            break
    return count
#print(mycount(3, [1, 2, 3, 4, 5, 3, 4, 3]))

#in
def myin(obj, passedList):
    index = 0
    while index < len(passedList):
        if passedList[index] == obj:
            return True
        index += 1
    return False
#print(myin(3, [1, 2, 3, 4, 5]))
#print(myin(6, [1, 2, 3, 4, 5]))

#reverse
def myreverse(passedList):
    outList = []
    for i in range(1, len(passedList)+1):
        outList.append(passedList[-i])
    return outList
#print(myreverse([1, 2, 3, 4, 5]))

#index
def myindex(obj, passedList):
    for i in range(len(passedList)):
        if passedList[i] == obj:
            return i
    return -1
#print(myindex(3, [1, 2, 3, 4, 5]))

#insert
def myinsert(index, obj, passedList):
    return passedList[:index] + [obj] + passedList[index:]
#print(myinsert(3, 0, [1, 2, 3, 4, 5]))


## 14
def myreplace(string, old, new):
    charlist = list(string)
    for i in range(len(charlist)):
        if charlist[i] == old:
            charlist[i] = new
    return "".join(charlist)
#print(myreplace('Mississippi', 'i', 'I'))

## 15 & 16
import turtle
def expandL(rulekeys, rules, string, depth):
    for i in range(depth):
        for j in range(len(rules)):
            string = applyRule(rulekeys[j], rules[j], string)
            return string

def applyRule(rulekey, rule, string):
    stringlist = list(string)
    for i in range(len(stringlist)):
        if stringlist[i] == rulekey:
            stringlist[i] = rule
    return "".join(stringlist)
    
def drawLines(string, turtlein, distance, angle):
    savedTurtles = []
    for char in string:
        if char == "F":
            turtlein.forward(distance)
        elif char == "B":
            turtlein.backward(distance)
        elif char == "+":
            turtlein.right(angle)
        elif char == "-":
            turtlein.left(angle)
        elif char == "[":
            savedTurtles.append(turtlein.clone())
        elif char == "]":
            turtlein = savedTurtles[-1]
            savedTurtles.pop(-1)

def Q15driver():
    rulekeys = ["H", "X"]
    rules = ["HFX[+H][-H]", "X[-FFF][+FFF]FX"]
    
    wn = turtle.Screen()
    clyde = turtle.Turtle()
    
    string = expandL(rulekeys, rules, "H", 4)
    print(string)
    drawLines(string, clyde, 50, 25)
    
Q15driver()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    