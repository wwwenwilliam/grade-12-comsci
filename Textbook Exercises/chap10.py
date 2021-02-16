## 2
def Q2():
    myList = []
    myList.append(76)
    myList.append(92.3)
    myList.append("hello")
    myList += [True] + [4] + [76]
    return myList
    
#print(Q2())

## 3
def Q3():
    myList = Q2()
    myList.append("apple")
    myList.append(76)
    myList.insert(0, 99)
    print(myList.index("hello"))
    print(myList.count(76))
    myList.remove(76)
    myList.pop(myList.index(True))
    return myList
    
#print(Q3())

## 4
def average(passedList):
    numSum = 0
    for num in passedList:
        numSum += num
    return numSum/len(passedList)

#print(average([1, 2, 3, 4, 5]))

## 5
def maximum(passedList):
    big = 0
    for num in passedList:
        if num > big:
            big = num
    return big

#print(maximum([1, 2, 3, 4, 5]))

## 6
def sum_of_squares(xs):
    numSum = 0
    for x in xs:
        numSum += x**2
    return numSum

#print(sum_of_squares([1, 2, 3, 4, 5]))


## 7
def odd(passedList):
    count = 0
    for num in passedList:
        if not(num % 2 == 0):
            count+=1
    return count

#print(odd([1, 2, 3, 4, 5]))

## 8
def even(passedList):
    count = 0
    for num in passedList:
        if num % 2 == 0:
            count+=1
    return count

#print(even([1, 2, 3, 4, 5]))

## 9
def negativeSum(passedList):
    numSum = 0
    for num in passedList:
        if num < 0:
            numSum += num
    return numSum

#print(negativeSum([1, -2, 3, -4, 5]))

## 10
def countfivelenwords(passedList):
    count = 0
    for word in passedList:
        if len(word) == 5:
            count += 1
    return count

#print(countfivelenwords(["hello", "bye", "hi", "words"]))

## 11
def uptoevenSum(passedList):
    numSum = 0
    for num in passedList:
        if num % 2 == 0:
            break
        numSum += num
    return numSum

#print(uptoevenSum([1, 3, 4, 5]))

## 12
def uptosam(passedList):
    count = 0
    for word in passedList:
        count += 1
        if word == "sam":
            break
    return count

#print(uptosam(["hi", "hi", "hi", "sam", "hi"]))

## 13
#count
def mycount(obj, passedList):
    count = 0
    for thing in passedList:
        count += 1
        if thing == obj:
            break
    return count
#print(mycount(3, [1, 2, 3, 4, 5, 3, 4, 3]))

#in
def myin(obj, passedList):
    index = 0
    while index < len(passedList):
        if passedList[index] == obj:
            return True
        index += 1
    return False
#print(myin(3, [1, 2, 3, 4, 5]))
#print(myin(6, [1, 2, 3, 4, 5]))

#reverse
def myreverse(passedList):
    outList = []
    for i in range(1, len(passedList)+1):
        outList.append(passedList[-i])
    return outList
#print(myreverse([1, 2, 3, 4, 5]))

#index
def myindex(obj, passedList):
    for i in range(len(passedList)):
        if passedList[i] == obj:
            return i
    return -1
#print(myindex(3, [1, 2, 3, 4, 5]))

#insert
def myinsert(index, obj, passedList):
    return passedList[:index] + [obj] + passedList[index:]
#print(myinsert(3, 0, [1, 2, 3, 4, 5]))


## 14
def myreplace(string, old, new):
    charlist = list(string)
    for i in range(len(charlist)):
        if charlist[i] == old:
            charlist[i] = new
    return "".join(charlist)
#print(myreplace('Mississippi', 'i', 'I'))

## 15
## 16

## 17
import random
randlist = [random.randint(0, 1000) for i in range(100)]
print(randlist)
