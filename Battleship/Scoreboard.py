import pickle

def findMin(colNum, passedList):
    #takes list and finds the minimum
    minimum = passedList[0][colNum]
    minimumPos = 0
    for i in range(1, len(passedList)):
        if passedList[i][colNum] < minimum:
            minimum = passedList[i][colNum]
            minimumPos = i
    return (minimum, minimumPos)


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


class Scoreboard:
    
    
    def __init__(self):
        #opens scores file
        try:
            file = open("scores.pickle", "rb")
        except IOError:
            print("scores not found, new scores file created")
            file = open("score.pickle", "wb")
            pickle.dump([], file)
            file.close()
            file = open("score.pickle", "rb")
        finally:    
            self.scores = pickle.load(file) #list of ["name", score]
            print(self.scores)
            file.close()
            
        
        
    def clearScores(self):
        #clears the scores file
        self.scores = []
        
        file = open("score.pickle", "wb")
        pickle.dump([], file)
        file.close()
    
    def displayScores(self):
        #prints scores to screen
        textSize(30)
        fill(255)
        text("Name", 300, 50)
        text("Score", 600, 50)
        for i in range(len(self.scores)):
            text(self.scores[i][0], 300, i*100 + 150)
            text(self.scores[i][1], 600, i*100 + 150)
        
    def addScore(self, score):
        #adds a score
        self.scores.append(score)
        
    def updateScores(self):
        #sorts scores
        self.scores = insertionSort(1, self.scores)
        pickle.dump(self.scores, open("scores.pickle", "wb"))
