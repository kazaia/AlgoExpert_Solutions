# Shifted binary search
#Time complexity: O(log(n))
#Space complexity: O(log(n)) (Due to recursion)

def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) -1)

def shiftedBinarySearchHelper(array, target, left, right):
    # base case:
    if left > right:
        return -1 
    
    middle = (left + right)//2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif array[left] <= potentialMatch: 
        if target >= array[left] and target < potentialMatch: 
            return shiftedBinarySearchHelper(array, target, left, middle -1)
        else:
            return shiftedBinarySearchHelper(array, target, middle+1, right)
    else:
        if  target < array[right] and target >= potentialMatch:
            return shiftedBinarySearchHelper(array, target, middle +1 , right)
        else:
            return shiftedBinarySearchHelper(array, target, left , middle -1)
