import copy

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]



def printTable(someTable):
    newTable = copy.deepcopy(someTable)
    maxList = []
    for listOFThings in newTable:
        for things in listOFThings:
            listOFThings[listOFThings.index(things)] = len(things)
        maxList.append(max(listOFThings))   # the max function just returns the maximum from a group of numbers

    for y in range (len(someTable[0])):
        for x in range(len(someTable)):
            print(someTable[x][y].rjust(maxList[x]), end = ' ')
        print()

        
printTable(tableData)

