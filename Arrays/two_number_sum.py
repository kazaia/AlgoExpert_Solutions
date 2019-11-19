# Two number sum 

# Solution1: Brute force 



# Solution2: with hash table



# Solution3: with two pointers 


def twoNumberSum(array, targetSum):
	array.sort()
	i = 0
	j = len(array) - 1
	while i < j:
		if array[i] + array[j] > targetSum:
			j -= 1
		elif array[i] + array[j] < targetSum:
			i += 1
		elif array[i] + array[j] == targetSum:
			return [array[i], array[j]]
		else:
			return [ ]
