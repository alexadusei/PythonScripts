"""
    Course: CISC 121
    Details: This program uses a simplified algorithm for deciding opening bids
    in the game Bridge.

"""

# Main Functions

"""
    Takes a card list and returns the number of high points it has from face
    cards. Checks the rank of every card in an index of 13 and compares it to
    each face card (Jack, Queen, King, Ace) to find a match. Once a match is
    found, the variable 'points' adds a score in relation to the match found
    and breaks out of nested for loop. Returns points once for loop is done.
"""


def highCardPoints(hand):

    handList = handToList(hand)
    points = 0
    pointValue = [1, 2, 3, 4]
    faceCard = ['J', 'Q', 'K', 'A']

    for card in handList:
        for i in range(4):
            if card[0] == faceCard[i]:
                points += pointValue[i]
                break


    return points

"""
    Takes a card list and returns the number of distributive points it has
    from a hand having either zero, one, or two cards of a suit. Uses the
    function 'suitCounts' to see the number of cards in each suit, and checks
    if each suit has said value and assigns points respectively.
"""
def distPoints(hand):

    handList = suitCounts(hand)
    points = 0

    for suit in handList:
        if suit == 0:
            points += 3
        elif suit == 1:
            points += 2
        elif suit == 2:
            points += 1

    return points

"""
    Takes a card list and adds high points and distributive points from the
    functions 'highCardPoints' and 'distPoints'
"""
def totalPoints(hand):
    return highCardPoints(hand) + distPoints(hand)

"""
    Takes a card list and determines whether player should bid, and returns
    what type of bid (or pass) user should execute.
"""
def bid(hand):
    if totalPoints(hand) < 14:
        return 'pass'
    elif totalPoints(hand) >= 14:
        if distPoints(hand) <= 1:
            return '1 notrump'
        else:
            return '1 ' + suitName(bestSuit(hand))

# Helper Functions

"""
    Breaks a 26-character string of cards into a list of 13 spots, each index
    containing 2 strings of the initial card string, and returns the list.
"""
def handToList(cardString):
    cardList = []
    counter = 0

    while counter < 26:
        card = cardString[counter] + cardString[counter + 1]
        cardList.append(card)

        counter += 2

    return cardList

"""
    Takes a string of cards and checks how many cards of each suit are in one
    hand of cards and returns a list. The function checks the first index of a
    suit in a hand of cards (therefore, the counter starts at 1) and then checks
    if that index is spades, hearts, diamonds, or clubs, and breaks out of the
    for loop and increments cardList at that index [spades, hearts, diamonds,
    clubs]
"""
def suitCounts(cardString):
    cardList = [0, 0, 0, 0]
    suitList = ['S', 'H', 'D', 'C']
    counter = 1

    while counter < 26:
        for i in range(4):
            if cardString[counter] == suitList[i]:
                cardList[i] += 1
                break
        counter += 2

    return cardList

"""
    Takes a list of cards and decides which is the best suit to open with.
    The function return is based on the suit with the highest cards. Suits
    with equal number of cards are overridden by the highest ranking suit
"""
def bestSuit(cardList):
    newCardList = suitCounts(cardList)

    if (newCardList[0] >= newCardList[1] and newCardList[0] >= newCardList[2]
    and newCardList[0] >= newCardList[3]):
        return 'S'
    elif (newCardList[1] > newCardList[0] and newCardList[1] >= newCardList[2]
    and newCardList[1] >= newCardList[3]):
        return 'H'
    elif (newCardList[2] > newCardList[0] and newCardList[2] > newCardList[1]
    and newCardList[2] >= newCardList[3]):
        return 'D'
    elif (newCardList[3] > newCardList[0] and newCardList[3] > newCardList[1]
    and newCardList[3] > newCardList[2]):
        return 'C'

""" Takes a letter and returns the full name of that suit letter for a bid"""
def suitName(suitLetter):
    suitNames = ['spade', 'heart', 'diamond', 'club']

    for i in range(14):
        if suitLetter.lower() == suitNames[i][0]:
            return suitNames[i]

print suitName('H')
