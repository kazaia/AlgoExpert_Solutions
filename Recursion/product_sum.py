# Product sum 
# Time complexity: O(n) where n is the number of elements in the array
# Space complexity: O(n). due to recursion  

def productSum(array, depth = 1):
    outputSum = 0
    for element in array:
        if type(element) is list:
            outputSum += productSum(element, depth + 1)
        else:
	    outputSum += element
    return outputSum * depth
