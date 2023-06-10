from funcStats import meter

def testList(testArg):
    currentList = []
    for var in ['a', 'b', 'c', 'd', 'e', '']:
        currentList.append(var)
        currentList.remove(var)

    return currentList

meter(testList, 3)
