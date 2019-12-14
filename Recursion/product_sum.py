# Product sum 
# Time complexity: O(n) where n is the number of elements in the array
# Space complexity: O(n). due to recursion  

def productSum(array, depth = 1):
	outputSum = 0 
	for item in array:
		if type(item) is list:
			outputSum += productSum(item, depth + 1)
		else:
			outputSum += item 
	return outputSum * depth
