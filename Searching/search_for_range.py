# Search for range 

#Recursive solution:
#Time complexity: O(log(n))
#Space complexity: O(log(n)) , due to the recursive calls 

def searchForRange(array, target):
    range = [-1, -1]
    alteredBinarySerach(array, target, 0, len(array) -1, range, True)
    alteredBinarySerach(array, target, 0, len(array) -1, range, False)
    return range

def alteredBinarySerach(array, target, left, right, range, goLeft):
    if left > right:
        return
    
    middle = (left+ right)//2

    if array[middle] > target:
        alteredBinarySerach(array, target, left, middle -1, range, goLeft)
    elif array[middle] < target:
        alteredBinarySerach(array, target, middle +1, right, range, goLeft)
    else:
        if goLeft:
            if middle == 0 or array[middle -1] != target:
                range[0] = middle
            else:
                alteredBinarySerach(array, target, left, middle -1 , range, goLeft)
        else:
            if middle == len(array) -1 or array[middle+1] != target:
                range[1] = middle
            else:
                alteredBinarySerach(array, target, middle +1, right , range, goLeft)

