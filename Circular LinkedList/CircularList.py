"""
    Details: Program puts a linked list into a circlular linked list,
             allowing it to rotate its current node periodically.
"""

# Main Functions

"""
    Takes a linked list and prints a representation of a list starting from
    the current node
"""
def printList(circList):
    if circList == None:
        print '[]'
    else:
        result = ""
        linkedList = straighten(circList)
        
        for i in range(len(linkedList)):
            result += str(linkedList[i])

            if i != len(linkedList)-1:
                result += ", "
                
        print '[' + result + ']'

"""
    Takes a linked list and a value and adds nodes to the start of the
    circular list. Returns the modified circular list.
"""
def add(circList, newValue):
    if circList == None:
        newNode = {'data':newValue, 'next':None}
        newNode['next'] = newNode
        return newNode
    else:
        newNode = {'data':newValue, 'next':circList}
        lastNode = last(circList)

        lastNode['next'] = newNode

        return newNode

"""
    Takes a circular list and determines what is the first, or current node
    of the circular list.
"""
def current(circList):
    if circList == None:
        return None
    else:
        return circList['data']

"""
    Takes a circular list and changes the current disposition of each node.
    The first node will become the second, and the second will become the third,
    all the way through until the last node becomes the first node. Returns the
    modified, advanced circular list.
"""
def advance(circList):
    if count(circList) > 1:
        circList = circList['next']

    return circList

"""
    Counts and keeps track of how many nodes are currently in the circular
    list.
"""
def count(circList):
    return len(straighten(circList))

"""
    Takes a linked list and a value and searches for that certain data value
    within the circular list. If the value is found, returns true, otherwise
    it returns false.
"""
def search(circList, value):
    linkedList = straighten(circList)

    for data in linkedList:
        if data == value:
            return True
        
    return False

"""
    Takes a circular list and deletes the the current node from the circular
    list, while changing the pointer of the last node to the nre first node
    of the circular list. Returns the modified circular list.
"""
def delete(circList):
    if circList != None:
        if count(circList) == 1:
            newNode = None
            return newNode
        else:
            newNode = circList['next']
            lastNode = last(circList)

            lastNode['next'] = newNode

            return newNode

# Helper Functions

"""
    A helper function that takes a circular list and 'straightens' it into a
    simple, linear list and returns it. This allows for a temporary
    representation of the circular list to have a beginning and an end which
    allow the add, search, count, and printList functions to work much more
    smoothly.
"""
def straighten(circList):
    linkedList = []

    if circList == None:
        return linkedList
    
    ptr = circList
    startNode = ptr
    isSame = False

    while isSame == False:
        linkedList.append(ptr['data'])
        ptr = ptr['next']

        if startNode is ptr:
            isSame = True

    return linkedList

"""
    A helper function which is a slight variation of the previous helper
    function straighten. Takes a circular list and 'straightens' it into
    a linear list. It defines a beginning and an end of a circular list, but
    this function returns the last node of the circular list.
"""
def last(circList):
    
    if circList == None:
        return None

    ptr = circList
    startNode = ptr
    isSame = False

    while isSame == False:
        ptr = ptr['next']

        if startNode is ptr['next']:
            isSame = True

    return ptr
