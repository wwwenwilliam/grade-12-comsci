def selectionSort(passedList):
    #takes list, sorts from small to big
    length = len(passedList)
    for i in range(length-1):
        #find minimum value in rest of list
        minimum = passedList[i+1]
        minimumPosition = i+1
        for j in range(i+1, length):
            if passedList[j] < minimum:
                minimum = passedList[j]
                minimumPosition = j
        #put the minimum value at the start of the rest
        passedList[i], passedList[minimumPosition] = passedList[minimumPosition], passedList[i]
    return passedList


testList = [3, 6, 2, 5, 9, 4]
print(selectionSort(testList))
