

def findElement(linked, element):
    nxt = linked
    while nxt[0] != element:
        nxt = nxt[1]
    return nxt

def appendElement(linked, element):
    newElement = [element, None]
            
    nxt = linked
    while nxt[1] != None:
        nxt = nxt[1]
    nxt[1] = newElement
    
    return linked

def addHeadElement(linked, element):
    return [element, linked]

def addElement(linked, before, element):
    newElement = [element, None]
    
    place = findElement(linked, before)
    newElement[1] = place[1][1]
    place[1][1] = newElement
    
    return linked
    


linked = ["Bob", None]

linked = appendElement(linked, "Alice")

linked = addHeadElement(linked, "Charlie")

linked = addElement(linked, "Bob", "Darrell")

print(linked)

print(findElement(linked, "Bob"))

