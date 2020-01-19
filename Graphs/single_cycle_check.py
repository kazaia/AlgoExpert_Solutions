# Single cycle check 


def hasSingleCycle(array):
    numOfVisitedElements = 0
    n = len(array)
    currentIdx = 0
    while numOfVisitedElements < n :
        if numOfVisitedElements > 0 and currentIdx == 0:
            return False
        numOfVisitedElements += 1
        currentIdx = getNextIdx(currentIdx, array)
    return currentIdx == 0

def getNextIdx(i, array):
    nextIdx = (i + array[i]) % len(array)
    return nextIdx if nextIdx >= 0  else nextIdx + len(array)



