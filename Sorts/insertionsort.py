def insertionSort(passedList):
    # takes list & sorts it
    length = len(passedList)
    for i in range(length-1):
        minimum = passedList[i]
        minimumPosition = i
        for j in range(i, length):
            if passedList[j] < minimum:
                minimum = passedList[j]
                minimumPosition = j

        passedList.insert(i, passedList[minimumPosition])
        passedList.pop(minimumPosition+1)

    return passedList


testList = [5, 4, 32, 6236, 43, 26, 43, 2, 6, 23, 45, 243, 5]
print(insertionSort(testList))
