# Binary search
# Time complexity: o(n)
# Space complexity: O(n)

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
	if left > right: 
		return -1 
	
	middle = (left + right)//2
	if array[middle] == target:
		return middle
	elif array[middle] > target:
		return binarySearchHelper(array, target, left, middle -1)
	else:
		return binarySearchHelper(array, target, middle +1, right)
