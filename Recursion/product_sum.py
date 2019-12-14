# Product sum 


def productSum(array, depth = 1):
	outputSum = 0 
	for item in array:
		if type(item) is list:
			outputSum += productSum(item, depth + 1)
		else:
			outputSum += item 
	return outputSum * depth
