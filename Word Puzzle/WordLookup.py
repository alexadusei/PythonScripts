"""
This module assumes it's in a folder containing a file called
'MobyWordList.txt'.  When the module is loaded, it reads the
file and stores the words in a dict for quick
look-up.  The module provides a lookup function that
returns True or False, depending on whether the word is in the
dictionary.

The module uses a global variable: wordList, the dict containing all
of the words from the file.  This is one case where the use of a
global variable is definitely justified.  The lookup function must
use this dictionary and it would be very inefficient to recreate
the dictionary every time the function is called.
"""

def createDictionary():
    """
    Creates a global dict of all the words in the word file.
    Every word from the word list file because a key in the dict.
    Each word maps to the value None.  This is because all we care about
    is whether a given word is in the dict.
    """
    global wordList # Specifies that wordList will not go away at the end
                    # of this function call and that other functions may
                    # use it
    wordList = dict()
    wordFile = open('MobyWordList.txt')
    for word in wordFile:
        word = word.strip() # remove leading or trailing spaces
        wordList[word] = None
    wordFile.close()


def lookup(word):
    global wordList # states that the function is using this global variable
    return word in wordList

# create the dictionary one time, when this module is first loaded
createDictionary()
