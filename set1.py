## Program set #1
# Modified bubble sort
def bubbleSort(passedList):
    #takes a list
    #returns sorted version of list
    limit = len(passedList)
    for i in range(1, limit):
        isSorted = True
        for j in range(limit-i):
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
    for i in range(1, limit):
        isSorted = True
        for j in range(limit-i):
            if passedList[j][column] > passedList[j+1][column]:
                (passedList[j], passedList[j+1]) = (passedList[j+1], passedList[j])
                isSorted = False
        if isSorted:
            break
    return passedList
    
numList = [7, 13, 15, 3, 6, 8]
# print(bubbleSort(numList))

myList = [[ "Adam","Math",90 ], [ "Mike","English",70 ], [ "Bing Xin","CompSci",100 ]]
# print(bubbleSortDimensional(0, myList))

# Selection sort
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
# print(selectionSort(testList))

# Insertion sort
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
# print(insertionSort(testList))

# Binary search
def binarySearch(passedList, searchItem):
    #takes sorted list and an item
    #returns position of item in list
    top = 0
    bottom = len(passedList)
    middle = (bottom + top) // 2
    
    while True:
        if top == bottom:
            break
        if passedList[middle] == searchItem:
            break
        elif passedList[middle] < searchItem:
            top = middle + 1
        else: 
            bottom = middle - 1
        middle = (bottom + top) // 2
    if passedList[middle] == searchItem:
        return middle
    else:
        print("Item not found")
        return None
    
testList = [2, 5, 6, 7, 8, 10, 15]
# print(binarySearch(testList, 3))

# Indirect Array addressing


# Reading from a file / writing to a file

# Using pickle – you will need this in your major database program

# Building and walking a dictionary

