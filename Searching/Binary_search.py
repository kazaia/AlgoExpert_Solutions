# Binary search: with recursion
# Time complexity: o(log(n))
# Space complexity: O(log(n))

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

	
#Iterative solution:
#Time complexity: O(log(n))
#Space complexity: O(1)

def binarySearch(array, target):
    left = 0
    right = len(array) -1
    while left <= right: 
	middle = (left + right)//2
	if array[middle] == target:
	     return middle
	elif array[middle] > target:
	     right = middle -1
	else:
	     left = middle + 1
    return -1		

