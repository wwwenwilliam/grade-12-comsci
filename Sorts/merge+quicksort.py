import random

# Quick Sort
def quickSort(passedList):
    length = len(passedList)
    
    if length <= 1:
        return passedList
    
    pivot = 0
    pivotValue = passedList[pivot]
    
    leftMark = 1
    rightMark = length-1
    done = False
    
    while not done:
        while leftMark <= rightMark and passedList[leftMark] <= pivotValue:
            leftMark += 1
            
        
        while passedList[rightMark] > pivotValue and leftMark <= rightMark:
            rightMark -= 1
        
        if rightMark < leftMark:
            done = True
        else:
            (passedList[leftMark], passedList[rightMark]) = (passedList[rightMark], passedList[leftMark])
        
    (passedList[pivot], passedList[rightMark]) = (passedList[rightMark], passedList[pivot])

    return quickSort(passedList[:rightMark]) + [passedList[rightMark]] + quickSort(passedList[rightMark+1:])
    
    




# Merge sort
def mergeSort(passedList):
    if len(passedList) > 1:
        mid = len(passedList)//2
        
        #sort halves
        leftHalf = passedList[:mid]
        leftHalf = mergeSort(leftHalf)
        
        rightHalf = passedList[mid:]
        rightHalf = mergeSort(rightHalf)
        
        #combine halves
        newList = []
        
        while len(leftHalf) != 0 and len(rightHalf) != 0:
            if leftHalf[0] >= rightHalf[0]:
                newList.append(rightHalf.pop(0))
            else:
                newList.append(leftHalf.pop(0))
            
            if len(leftHalf) == 0:
                newList += rightHalf
                rightHalf = []
            elif len(rightHalf) == 0:
                newList += leftHalf
                leftHalf = []
        
        return newList
    else:
        return passedList
        

# test code -------------------------

randomList = [random.randint(0, 50) for i in range(20)]
print(randomList)

# sortList = mergeSort(randomList)

sortList = quickSort(randomList)

print(sortList)
print(sorted(randomList) == sortList)

