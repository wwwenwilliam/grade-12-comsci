def loadFileInfo( fileName ):
    file = open(  fileName )
    fileInfo = []
    text = file.readlines()


    for line in text:
        line = line.strip()
        line = line.split( "," )
        fileInfo.append( line )

    numItems = len( fileInfo )
    file.close()


    return fileInfo, numItems

dataFile, numEntries = loadFileInfo( "testdata.txt" )


# Program Set # 1 - bubble sort

def bubbleSort ( whichCol, arrayToSort ):
    n = len( arrayToSort )
    for i in range( 1, n ):
        isSorted = True
        for j in range ( n - i ):
            if arrayToSort[ j ][ whichCol ] > arrayToSort[ j + 1 ][ whichCol ]:
                arrayToSort[ j + 1 ], arrayToSort[ j ] = arrayToSort[ j ], arrayToSort[ j + 1 ]
                isSorted = False
        if isSorted:
            break
    return( arrayToSort )

limit = len( dataFile )
for i in range( limit ):
    dataFile[ i ][ 2 ] = int( dataFile[ i ][ 2 ] )

# 1.	Modified bubble sort
# You have been supplied with the bubble sort above
# Use the example below to test your code

# test1 = bubbleSort( 0, dataFile )
# for i in range ( limit ):
#     print ( test1[ i ] )
# print( "" )

# test2 = bubbleSort( 1, dataFile )
# for i in range ( limit ):
#     print ( test1[ i ] )

# print ( "" )
# test3 = bubbleSort( 2, dataFile )
# for i in range ( limit ):
#     print ( test1[ i ] )




#2.	Selection sort - Follow example above expand the same way as shown above so that you can pick which column of the data is to be sorted
def findMin(colNum, passedList):
    #takes list and finds the minimum
    minimum = passedList[0][colNum]
    minimumPos = 0
    for i in range(1, len(passedList)):
        if passedList[i][colNum] < minimum:
            minimum = passedList[i][colNum]
            minimumPos = i
    return (minimum, minimumPos)

def selectionSort(colNum, passedList):
    #takes list, sorts from small to big
    length = len(passedList)
    for i in range(length-1):
        #find minimum value in rest of list
        sublist = passedList[i:]
        minimumPos = findMin(colNum, sublist)[1] + i
        #switch min value with value at correct pos
        passedList[i], passedList[minimumPos] = passedList[minimumPos], passedList[i]
    return passedList

# test code --------------------------------------------------

# test1 = selectionSort( 0, dataFile )
# for i in range ( limit ):
#     print ( test1[ i ] )
# print( "" )

# test2 = selectionSort( 1, dataFile )
# for i in range ( limit ):
#     print ( test1[ i ] )

# print ( "" )
# test3 = selectionSort( 2, dataFile )
# for i in range ( limit ):
#     print ( test1[ i ] )

#3.	Insertion sort - - Follow example above expand the same way as shown above so that you can pick which column of the data is to be sorted

def insertionSort(colNum, passedList):
    #takes list, sorts from small to big
    length = len(passedList)
    for i in range(length-1):
        #find minimum value in rest of list
        sublist = passedList[i:]
        minimumPos = findMin(colNum, sublist)[1] + i
        #switch min value with value at correct pos
        passedList.insert(i, passedList[minimumPos])
        passedList.pop(minimumPos+1)
    return passedList

# test code --------------------------------------------------

# test1 = insertionSort( 0, dataFile )
# for i in range ( limit ):
#     print ( test1[ i ] )
# print( "" )

# test2 = insertionSort( 1, dataFile )
# for i in range ( limit ):
#     print ( test1[ i ] )

# print ( "" )
# test3 = insertionSort( 2, dataFile )
# for i in range ( limit ):
#     print ( test1[ i ] )

#4.	Binary search  - pick the result of any one individual results of the sorts above - I suggest sorting by name as the others will be repeated

def binarySearch(colNum, passedList, searchItem):
    #takes sorted list and an item
    #returns position of item in list
    top = 0
    bottom = len(passedList)
    middle = (bottom + top) // 2
    
    while True:
        #adjust top/bottom
        if top == bottom:
            break
        if passedList[middle][colNum] == searchItem:
            break
        elif passedList[middle][colNum] < searchItem:
            top = middle + 1
        else: 
            bottom = middle - 1
        #recalc middle
        middle = (bottom + top) // 2
    #check if thing was found
    if passedList[middle][colNum] == searchItem:
        return middle
    else:
        print("Item not found")
        return None

# test code --------------------------------------------------

# test1 = bubbleSort( 0, dataFile )
# for i in range ( limit ):
#     print ( test1[ i ] )

# print(binarySearch(0, test1, "JOHN"))
# print(binarySearch(0, test1, "NAME"))
# print( "" )

#5.	Indirect Array addressing - work with original data input from the file - show that the data can be accessed in order of name, course, mark

def indirectSorting(colNum, valueList):
    #modification of bubble sort
    limit = len(valueList)
    pList = [i for i in range(limit)]
    for i in range(1, limit):
        isSorted = True
        for j in range(limit-i):
            if valueList[pList[j]][colNum] > valueList[pList[j+1]][colNum]:
                (pList[j], pList[j+1]) = (pList[j+1], pList[j])
                isSorted = False
        if isSorted:
            break
    return pList

# test code --------------------------------------------------
# pListName = indirectSorting(0, dataFile)
# pListCourse = indirectSorting(1, dataFile)
# pListMark = indirectSorting(2, dataFile)

# for pointer in pListName:
#     print(dataFile[pointer])
# print("")

# for pointer in pListCourse:
#     print(dataFile[pointer])
# print("")

# for pointer in pListMark:
#     print(dataFile[pointer])
# print("")

#6.	Reading from a file / writing to a file - you can simply write the information from the file back to a file BUT show the different ways a file can be read and written to
# Be sure to show how you can read and then write to to the same line you read from a file using the rw parameters


#7.	Using pickle as you will need this in your major database program


#8.	Building and walking a dictionary
# Read the dictionary data file, use the words in the file as the keys to the main dictionary
#Inside the main dictionary create a sub-dictionary where the keys are the letters found in the word - case doesn't matter - the field for that sub-dictionary will be how many times that
#letter occurs
#Then walk the dictionary and determine how many times each letter occurs - check the file so that you know what the result should be
dataFile, numEntries = loadFileInfo( "dictionary data.txt" )
dataFile = dataFile[0]

def toUpper(data):
    for i in range(len(data)):
        data[i] = data[i].upper()
    return data

def createDict(aList, default):
    newDict = {}
    for element in aList:
        newDict[element] = default
    return newDict
        
def createSubDicts(aDict):
    for key in aDict:
        charList = list(key)
        subDict = {}
        for char in charList:
            if char in subDict:
                subDict[char] += 1
            else:
                subDict[char] = 1
        aDict[key] = subDict
    return aDict

def findLetters(aDict):
    newDict = {}
    for key1 in aDict:
        for key2 in aDict[key1]:
            charList = list(key2)
            for char in charList:
                if char in newDict:
                    newDict[char] += 1
                else:
                    newDict[char] = 1
    return newDict
            

# test code --------------------------------------------------

# dataFile = toUpper(dataFile)
# aDict = createDict(dataFile, None)
# aDict = createSubDicts(aDict)
# letterDict = findLetters(aDict)
# print(letterDict)
    






















