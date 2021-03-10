
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
    newElement = [element, head[1]]
    linked.append(newElement)
    head = [element, len(linked)-1]
    return(head, linked)

def addElement(linked, head, before, element):
    newElement = [element, None]
    linked.append(newElement)
    
    place = findElement(linked, head, before)
    newElement[1] = place[1]
    place[1] = len(linked)-1
    
    return linked


head = ["grape", 0]
linked = [["grape", None]]

(head, linked) = addHeadElement(linked, head, "apple")
linked = appendElement(linked, head, "banana")
linked = addElement(linked, head, "grape", "fig")

print(linked)
