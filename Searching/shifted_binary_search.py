# Shifted binary search

def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) -1)

def shiftedBinarySearchHelper(array, target, left, right):
    # base case:
    if left > right:
        return -1 
    #left = 0
    #right = len(array) -1
    middle = (left + right)//2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif array[left] <= potentialMatch: # sorted
        if target >= array[left] and target < potentialMatch: # makaynch
            return shiftedBinarySearchHelper(array, target, left, middle -1)
        else:
            return shiftedBinarySearchHelper(array, target, middle+1, right)
    else:
        if  target < array[left] and target >= potentialMatch:
            return shiftedBinarySearchHelper(array, target, middle +1 , right)
        else:
            return shiftedBinarySearchHelper(array, target, left , middle -1)
