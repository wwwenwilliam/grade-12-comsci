
def findElement(linked, head, element):
    nxt = linked[head[1]]
    while nxt[0] != element:
        nxt = linked[nxt[1]]
    return nxt

def appendElement(linked, head, element):
    newElement = [element, None]
    linked.append(newElement)
            
    nxt = linked[head[1]]
    while nxt[1] != None:
        nxt = linked[nxt[1]]
    nxt[1] = len(linked)-1
    
    return linked

def addHeadElement(linked, head, element):
    newElement = [element, linked.index(head)]
    linked.append(newElement)
    head = newElement
    return(head, linked)

def addElement(linked, head, before, element):
    newElement = [element, None]
    linked.append(newElement)
    
    place = findElement(linked, head, before)
    newElement[1] = place[1]
    place[1] = len(linked)-1
    
    return linked

def printLinked(linked, head):
    nxt = head
    while nxt[1] != None:
        print(nxt[0], end=" ")
        nxt = linked[nxt[1]]
    print(nxt[0], end=" ")
    print("")
    


head = ["grape", None]
linked = [["grape", None]]

(head, linked) = addHeadElement(linked, head, "apple")
linked = appendElement(linked, head, "banana")
linked = addElement(linked, head, "grape", "fig")

print(linked)
printLinked(linked, head)
