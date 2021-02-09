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
    

##test program
numList = [7, 13, 15, 3, 6, 8]
print(bubbleSort(numList))