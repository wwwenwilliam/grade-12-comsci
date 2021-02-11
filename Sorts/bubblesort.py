##bubble sort

def bubbleSort(passedList):
    #takes a list
    #returns sorted version of list
    limit = len(passedList)
    for i in range(limit):
        isSorted = True
        for j in range(limit-1):
            if passedList[j] > passedList[j+1]:
                (passedList[j], passedList[j+1]) = (passedList[j+1], passedList[j])
                isSorted = False
        if isSorted:
            break
    return passedList

def bubbleSortDimensional(column, passedList):
    #takes a list
    #returns sorted version of list
    limit = len(passedList)
    for i in range(limit):
        isSorted = True
        for j in range(limit-1):
            if passedList[j][column] > passedList[j+1][column]:
                (passedList[j], passedList[j+1]) = (passedList[j+1], passedList[j])
                isSorted = False
        if isSorted:
            break
    return passedList
    

##test program
numList = [7, 13, 15, 3, 6, 8]
print(bubbleSort(numList))

myList = [[ "Adam","Math",90 ], [ "Mike","English",70 ], [ "Bing Xin","CompSci",100 ]]
print(bubbleSortDimensional(0, myList))