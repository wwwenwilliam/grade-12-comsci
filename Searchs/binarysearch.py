def binarySearch(passedList, searchItem):
    #takes sorted list and an item
    #returns position of item in list
    top = 0
    bottom = len(passedList)-1
    middle = (bottom + top) // 2
    
    if len(passedList) == 0:
        return -1
    
    while top <= bottom:
        if passedList[middle] < searchItem:
            top = middle + 1
        elif passedList[middle] > searchItem: 
            bottom = middle - 1
        else:
            return middle
        middle = (bottom + top) // 2
    else:
        print("Item not found")
        return None
    
testList = []
print(binarySearch(testList, 0))