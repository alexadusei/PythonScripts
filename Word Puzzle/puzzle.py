"""
    Details: Program simulates a Changeling puzzle. Two words are given with a
             number of steps, and the program transforms the first given word
             into the desired word without exceeding the given amount of steps.
             Only one letter may be transformed at each step and all steps must
             be legitimate English words within WordLookup.
"""

from WordLookup import *

"""
    Takes one word, a target word, and a number of steps and returns a list of
    letters that have a one letter difference while getting closer to the
    target word, in a certain amount of steps of less. Returns none if the words
    aren't equal or don't exist, or when thh target word can't be reached in a
    certain amount of steps.
"""
def changeling(firstWord, secondWord, steps):
    print firstWord, secondWord, steps
    if (len(firstWord) != len(secondWord) or \
        lookup(firstWord) == False or lookup(secondWord) == False or steps < 1):

        if (firstWord == secondWord and steps >= 0):
            return [firstWord]

        return None
    else:
        if (firstWord == secondWord):
            return [firstWord]
        else:
            """
                If # of steps is less than number of differing
                words between firstWord and secondWord, cancel search
            """
            counter = 0

            for i in range(len(firstWord)):
                if not firstWord[i] == secondWord[i]:
                    counter += 1

            if counter > steps:
                return None

            """
                For every word within the one letter difference function, start
                the changeling function again and check if those words are
                equal to the target word. If not, function will reach this for
                look again and branch off continuously until target word is
                found.
            """
            for word in oneLetterDiff(firstWord):
                lis = changeling(word, secondWord, steps-1)

                if not lis == None:
                    return [firstWord] + lis

"""
    Takes a word and returns a list of all words that have a one letter
    difference to the target word. For every word within the dictionary in
    WordLookup.py, it checks if that word is equal in length to the word the
    function takes. If this is so, for every letter in that word, the first
    letter is removed, and the remaining letters are checked to see if they're
    equal to the remaining letters of the target word. If this is so, the word
    is added to the list and the for loop moves to the second letter, and so
    forth to the end of the word.
"""
def oneLetterDiff(targetWord):
    targetList = []

    for word in wordList:
        if len(word) == len(targetWord) and word != targetWord:
            for i in range(len(targetWord)):
                if (word[:i] + word[i+1:]) == (targetWord[:i] + targetWord[i+1:]):
                    targetList.append(word)

    return targetList
