""" Name: Alex Adusei
    Date: Friday September 13 2013
    Program: Grid
    Details: Program has a function that draws a grid

"""

def grid(x, y):

    numRows = x
    numCols = y

    def printGrid():
        print numRows * ('+ - - - - ') + str('+')
        print 4 * (numRows * ('|         ') + str('|\n')),

    def loop(cols):
        counter = 1;
        while counter <= cols:
            printGrid()
            counter += 1

        print numRows * ('+ - - - - ') + str('+')

    loop(numCols)

