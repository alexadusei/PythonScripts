from TrinaryTree import *
from random import shuffle, randint

def write_tree(tree, indent=0):
    """
    Returns whatever printTree would output as a string.
    """
    string = ""

    if tree == None:
        return # don't print anything
    elif tree['data2'] == None: # one data element, no children
        string += " "*indent + str(tree['data1']) + "\n"
    else: # two data elements, may have up to three children
        temp = write_tree(tree['right'],indent+4)
        if temp:
            string += temp + "\n"
        string += " "*indent + str(tree['data2']) + "\n"
        temp = write_tree(tree['middle'],indent+4)
        if temp:
            string += temp + "\n"
        string += " "*indent + str(tree['data1']) + "\n"
        temp = write_tree(tree['left'],indent+4)
        if temp:
            string += temp + "\n"

    return string

def test_del_min(tree, over=True):
    """
    Test finction for deleteMin().
    Sequentially reduces tree to size 0.
    If the log contains False, there is an error in your code. Some value which
    is in the tree cannot be found with your search function. Look at the output
    above the sequence of booleans to find your error.
    """
    log = open("testlog.txt", 'a+')
    if over:
        log.truncate()
    while tree:
        tree = deleteMin(tree)
        log.write(str(write_tree(tree)))
        log.flush()
        if tree:
            log.write("\n")
            log.flush()
            for e in treeToList(tree):
                log.write(str((e, search(tree, e)))+"\n")
                log.flush()

        log.write("-" * 80 + "\n")
        log.flush()

    log.seek(0)
    if "False" in log.read():
        print "There is an error in the test case. Refer to testlog.txt."
    else:
        print "No error in test case. Results stored in testlog.txt."
    log.close()


def test_del(tree, over=True):
    """
    Test function for delete().
    Works like test_del_min(), but randomizes which values it removes.
    Depends on the delete function being named delete().
    """
    log = open("testlog.txt", 'a+')
    if over:
        log.truncate()
    lis = treeToList(tree)
    shuffle(lis)
    while lis:
        tree = delete(tree, lis.pop(0))
        log.write(str(write_tree(tree)))
        log.flush()
        if tree:
            log.write("\n")
            log.flush()
            for e in treeToList(tree):
                log.write(str((e, search(tree, e)))+"\n")
                log.flush()
        log.write("-" * 80 + "\n")
        log.flush()

    log.seek(0)
    if "False" in log.read():
        print "There is an error in the test case. Refer to testlog.txt."
    else:
        print "No error in test case. Results stored in testlog.txt."
    log.close()

def test_del_a_lot(n=10, s=20, f=test_del_min, o=False, over=True):
    """
    Runs test_del or test_del_min n times on random trees of size s.
    """
    log = open("testlog.txt", 'a+')
    if over:
        log.truncate()
    for i in range(n):
        f(randomTree(s), over=o)
    log.flush()
    log.close()

def BE_PREPARED(n=randint(5,1000)):
    """
    Runs way too much.
    """
    for i in range(n):
        test_del_a_lot(over=False)
        test_del_a_lot(f=test_del, over=False)

def read_log():
    log = open("testlog.txt", 'r')
    log.seek(0)
    print log.read()
    log.close()

t1 = treeFromList([13, 42, 3, 6, 23, 32, 72, 90, 1, 10, 26, 85, 88, 73, 80])
t2 = treeFromList([13, 42, 23, 32, 72, 90, 24, 31, 85, 88, 25, 30, 73, 80, 26, 29])
t7 = treeFromList([32, 70, 15, 25, 34, 60, 71, 80, 3, 10, 20, 24, 30, 31])
t4 = {'data1': None, 'data2': 30, 'left': None, 'middle': \
        {'data1': None, 'data2': None, 'left': None, 'middle': None,\
        'right': None}, 'right': None}

t3 = {'data1': 13,\
 'data2': 42,\
 'left': None,\
 'middle': {'data1': 23,\
            'data2': 32,\
            'left': None,\
            'middle': {'data1': 24,\
                       'data2': 31,\
                       'left': None,\
                       'middle': {'data1': 25,\
                                  'data2': 30,\
                                  'left': None,\
                                  'middle': {'data1': 26,\
                                             'data2': 29,\
                                             'left': None,\
                                             'middle': None,\
                                             'right': None},\
                                  'right': None},\
                       'right': None},\
            'right': None},\
 'right': {'data1': 72,\
           'data2': 90,\
           'left': None,\
           'middle': {'data1': 85,\
                      'data2': 88,\
                      'left': {'data1': 73,\
                               'data2': 80,\
                               'left': None,\
                               'middle': None,\
                               'right': None},\
                      'middle': None,\
                      'right': None},\
           'right': None}}

t5 = {'data1': 32,
 'data2': 42,
 'left': None,
 'middle': None,
 'right': {'data1': 72,
           'data2': 90,
           'left': None,
           'middle': {'data1': 85,
                      'data2': 88,
                      'left': None,
                      'middle': None,
                      'right': None},
           'right': None}}

t6 = {'data1': 32,
 'data2': 42,
 'left': None,
 'middle': None,
 'right': {'data1': 72,
           'data2': 90,
           'left': None,
           'middle': {'data1': 85,
                      'data2': 88,
                      'left': {'data1': 73,
                               'data2': 80,
                               'left': None,
                               'middle': None,
                               'right': None},
                      'middle': None,
                      'right': None},
           'right': None}}