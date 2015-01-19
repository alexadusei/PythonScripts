"""
    Details: Functions to create, view and modify "trinary trees".
    Note: Bonus function 'delete' is fully functional worth evaluation

"""

# Author: Margaret Lamb
def printTree(tree, indent=0):
    """
    Prints an indented representation of a trinary tree.  The second
    parameter determines how far the tree is to be indented from the
    left margin.  Just like the indented representation of binary trees,
    this representation looks like a drawing of a tree without the
    connecting lines if you tilt your head to the left.
    """
    if tree == None:
        return # don't print anything
    elif tree['data2'] == None: # one data element, no children
        print " "*indent + str(tree['data1'])
    else: # two data elements, may have up to three children
        printTree(tree['right'],indent+4)
        print " "*indent + str(tree['data2'])
        printTree(tree['middle'],indent+4)
        print " "*indent + str(tree['data1'])
        printTree(tree['left'],indent+4)

def add(tree, newValue):
    """
    Adds newValue to tree and returns a pointer to the root of the
    modified tree.  If newValue is already in the tree, doesn't change
    the tree (but this is not an error).
    """
    #nothing in current root
    if tree == None:
        return {'data1':newValue, 'data2':None, 'left':None, 'middle':None, \
                'right':None}
    #value is already in root
    elif newValue == tree['data1'] or newValue == tree['data2']:
        return tree
    else:
        #value is less than data1, check if data2 exists. If not,
        #switch data1 and data2. If data2 does exist, go down 'left' branch
        #and start search again
        if newValue < tree['data1']:
            if tree['data2'] == None:
                tree['data1'], tree['data2'] = newValue, tree['data1']
            else:
                tree['left'] = add(tree['left'], newValue)
        #value is greater than data2, check if data2 exists. If not,
        #create data2 with value. If data2 does exist, go down 'right' branch
        #and start search again
        elif newValue > tree['data2']:
            if tree['data2'] == None:
                tree['data2'] = newValue
            else:
                tree['right'] = add(tree['right'], newValue)
        #value is greater than data1, but less than data2. Go down 'middle'
        #branch and start search again.
        else:
            tree['middle'] = add(tree['middle'], newValue)

        return tree

# Author: Margaret Lamb
def treeFromList(values):
    """
    Parameter must be a Python lists of values.  Returns a tree
    created by adding each value from the list to the tree, in order.
    A convenience function for testing.
    """
    tree = None
    for v in values:
        tree = add(tree,v)
    return tree

# Author: Margaret Lamb
import random
def randomTree(numNodes):
    """
    Creates a tree with the specified number of nodes using random numbers.
    A helper to generate trees for testing.  The tree may actually have fewer
    nodes than the requested number if randInt happens to come up with
    duplicates of the same number.
    """
    tree = None
    for i in range(numNodes):
        tree = add(tree, random.randint(1,100))
    return tree

def search(tree,value):
    """
    Searches a tree for a value.  Returns True if value occurs somewhere
    inside tree, False otherwise.
    """
    if tree == None:
        return False
    elif value == tree['data1'] or value == tree['data2']:
        return True
    else:
        if value < tree['data1']:
            return search(tree['left'], value)
        elif value > tree['data2']:
            return search(tree['right'], value)
        else:
            return search(tree['middle'], value)

def total(tree):
    """
    Returns the total of all the numbers in a tree.  If the tree is empty,
    the total is zero.
    """
    if tree == None:
        return 0
    else:
        leftTree = total(tree['left'])
        middleTree = total(tree['middle'])
        rightTree = total(tree['right'])

        result = leftTree + middleTree + rightTree

        if tree['data2'] == None:
            result += tree['data1']
        else:
            result +=(tree['data1'] + tree['data2'])

        return result

def height(tree):
    """
    Returns the height of the tree -- the length of the longest path from
    the root to a leaf.
    """
    if tree == None:
        return 0
    else:
        leftHeight = height(tree['left'])
        middleHeight = height(tree['middle'])
        rightHeight = height(tree['right'])

        return max(leftHeight, middleHeight, rightHeight) + 1

def findMin(tree):
    """
    Returns the smallest value in the tree, or None if the tree is empty.
    """
    if tree == None:
        return None
    else:
        if tree['left'] == None:
            return tree['data1']
        else:
            return findMin(tree['left'])

def deleteMin(tree):
    """
    Deletes the smallest value in the tree and returns the modified tree.
    No effect if the tree is empty.
    """
    target = findMin(tree)

    #No subtrees
    if tree == None:
        return None
    elif tree['left'] == None and tree['middle'] == None and tree['right'] \
    == None:
        #one data value
        if tree['data1'] != None and tree['data2'] == None:
            return None
        #two data values
        elif tree['data1'] != None and tree['data2'] != None:
            tree['data1'], tree['data2'] = tree['data2'], None
            return tree
    #Left subtree
    elif tree['left'] != None:
        tree['left'] = deleteMin(tree['left'])
        return tree
    #Middle subtree
    elif tree['middle'] != None:
        tree['data1'] = findMin(tree['middle'])
        tree['middle'] = deleteMin(tree['middle'])
        return tree
    #Right subtree
    elif tree['right'] != None:
        tree['data1'], tree['data2'] = tree['data2'], findMin(tree['right'])
        tree['right'] = deleteMin(tree['right'])
        return tree

def treeToList(tree):
    """
    Returns a list of all the values in the tree, in ascending order
    """
    if tree == None:
        return []
    else:
        leftList = treeToList(tree['left'])
        middleList = treeToList(tree['middle'])
        rightList = treeToList(tree['right'])

        lis = leftList +  middleList + rightList

        if tree['data2'] != None:
            result = [tree['data1']] + [tree['data2']] + lis
        else:
            result = [tree['data1']] + lis

        result.sort()
        return result

#BONUS FUNCTION
def delete(tree, value):
    """
    Deletes the requested value in the tree and returns the modified tree.
    No effect if the tree is empty.
    """
    if tree == None:
        return None
    else:
        #value == ['data1']
        if value == tree['data1'] or value == tree['data2']:
            if value == tree['data1']:
                if tree['left'] != None:
                    tree['data1'] = findMax(tree['left'])
                    tree['left'] = deleteMax(tree['left'])
                elif tree['middle'] != None:
                    tree['data1'] = findMin(tree['middle'])
                    tree['middle'] = deleteMin(tree['middle'])
                elif tree['right'] != None:
                    tree['data1'] = findMin(tree['right'])
                    tree['right'] = deleteMin(tree['right'])
            else:# value == ['data2']
                if tree['right'] != None:
                    tree['data2'] = findMin(tree['right'])
                    tree['right'] = deleteMin(tree['right'])
                elif tree['middle'] != None:
                    tree['data2'] = findMax(tree['middle'])
                    tree['middle'] = deleteMax(tree['middle'])
                elif tree['left'] != None:
                    tree['data1'], tree['data2'] = findMax(tree['left']), \
                    tree['data1']
                    tree['left'] = deleteMax(tree['left'])

            return tree
        #Value not found in root, looks in appropiate subtree and starts
        else:
            if value < tree['data1']:
                tree['left'] =  delete(tree['left'], value)
            elif value > tree['data2']:
                tree['right'] =  delete(tree['right'], value)
            else:
                tree['middle'] = delete(tree['middle'], value)

            return tree

#Helper functions for delete.
def deleteMax(tree):
    """
    Deletes the largest value in the tree and returns the modified tree.
    No effect if the tree is empty.
    """
    target = findMax(tree)

    #No subtrees
    if tree == None:
        return None
    elif tree['left'] == None and tree['middle'] == None and tree['right'] \
    == None:
        #one data value
        if tree['data1'] != None and tree['data2'] == None:
            return None
        #two data values
        elif tree['data1'] != None and tree['data2'] != None:
            tree['data2'] = None
            return tree
    #Right subtree
    elif tree['right'] != None:
        tree['right'] = deleteMax(tree['right'])
        return tree
    #Middle subtree
    elif tree['middle'] != None:
        tree['data2'] = findMax(tree['middle'])
        tree['middle'] = deleteMax(tree['middle'])
        return tree
    #Left subtree
    elif tree['left'] != None:
        tree['data1'], tree['data2'] = findMax(tree['left']), tree['data1']
        tree['left'] = deleteMax(tree['left'])
        return tree

def findMax(tree):
    """
    Returns the largest value in the tree, or None if the tree is empty.
    """
    if tree == None:
        return None
    else:
        if tree['right'] == None:
            if tree['data2'] == None:
                return tree['data1']
            else:
                return tree['data2']
        else:
            return findMax(tree['right'])
