import pickle

class Scoreboard:
    
    def __init__(self):
        #opens scores file
        try:
            file = open("scores.pickle", "rb")
        except IOError:
            print("scores not found, new scores file created")
            file = open("scores.pickle", "wb")
            pickle.dump({}, file)
            file.close()
            file = open("scores.pickle", "rb")
        finally:    
            self.scores = pickle.load(file) #dict of names w/scores
            file.close()
            
        self.start = 0
            
    def clearScores(self):
        #clears the scores file
        self.scores = {}
        
        file = open("scores.pickle", "wb")
        pickle.dump({}, file)
        file.close()
        
    def toList(self):
        outList = []
        for name in self.scores:
            outList.append([name, self.scores[name]])
        return outList
    
    def displayScores(self, x, y):
        #prints scores to screen
        display = self.toList()
        display = quickSort(1, display)
        textSize(30)
        fill(255)
        text("NAME", x, 50 + y)
        text("SCORE", x+300, 50 + y)
        for i in range(self.start, self.start+5):
            if i >= len(display):
                break
            text(display[i][0], x, (i-self.start)*100 + 150 + y)
            text(display[i][1], x+300, (i-self.start)*100 + 150 + y)
            
    def incrementStart(self, direction):
        if self.start + 5 < len(self.scores) and direction == 1:
            self.start += direction
        elif self.start > 0 and direction == -1:
            self.start += direction
            
    def resetStart(self):
        self.start = 0
        
    def addScore(self, player):
        #adds a score
        if player.name in self.scores:
            if self.scores[player.name] > player.score:
                self.scores[player.name] = player.score
        else:
            self.scores[player.name] = player.score
        
    def updateFile(self):
        #sorts scores
        f = open("scores.pickle", "wb")
        pickle.dump(self.scores, f)
        f.close()
        
    def findScore(self, player):
        if player.name in self.scores:
            return self.scores[player.name]
        else:
            return None
        
def findMin(colNum, passedList):
    #takes list and finds the minimum
    minimum = passedList[0][colNum]
    minimumPos = 0
    for i in range(1, len(passedList)):
        if passedList[i][colNum] < minimum:
            minimum = passedList[i][colNum]
            minimumPos = i
    return (minimum, minimumPos)

def binarySearch(colNum, passedList, searchItem):
    #takes sorted list and an item
    #returns position of item in list
    top = 0
    bottom = len(passedList)
    middle = (bottom + top) // 2
    
    if passedList[middle][colNum] == searchItem:
        return middle
    
    while top != bottom:
        if passedList[middle][colNum] < searchItem:
            top = middle + 1
        else: 
            bottom = middle - 1
        middle = (bottom + top) // 2
    if passedList[middle][colNum] == searchItem:
        return middle
    else:
        print("Item not found")
        return None
    
def insertionSort(colNum, passedList):
    #takes list, sorts from small to big
    length = len(passedList)
    for i in range(length-1):
        #find minimum value in rest of list
        sublist = passedList[i:]
        minimumPos = findMin(colNum, sublist)[1] + i
        #insert min value with value at correct pos
        passedList.insert(i, passedList[minimumPos])
        passedList.pop(minimumPos+1)
    return passedList

def quickSort(colNum, passedList):
    length = len(passedList)
    
    if length <= 1:
        return passedList
    
    pivot = 0
    pivotValue = passedList[pivot][colNum]
    
    leftMark = 1
    rightMark = length-1
    done = False
    
    while not done:
        while leftMark <= rightMark and passedList[leftMark][colNum] <= pivotValue:
            leftMark += 1
        
        while passedList[rightMark][colNum] > pivotValue and leftMark <= rightMark:
            rightMark -= 1
        
        if rightMark < leftMark:
            done = True
        else:
            (passedList[leftMark], passedList[rightMark]) = (passedList[rightMark], passedList[leftMark])
        
    (passedList[pivot], passedList[rightMark]) = (passedList[rightMark], passedList[pivot])

    return quickSort(colNum, passedList[:rightMark]) + [passedList[rightMark]] + quickSort(colNum, passedList[rightMark+1:])
        
