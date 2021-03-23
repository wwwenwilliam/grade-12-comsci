def binarySearch(passedList, searchItem):
    #takes sorted list and an item
    #returns position of item in list
    top = 0
    bottom = len(passedList)
    middle = (bottom + top) // 2
    
    if passedList[middle] == searchItem:
        return middle
    
    while top != bottom:
        if passedList[middle] < searchItem:
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
print(binarySearch(testList, 6))