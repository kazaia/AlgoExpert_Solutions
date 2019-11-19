# Two number sum 

# Solution1: Brute force 
# Time complexity: O(n^2)
# Space complexity: O(n)

def twoNumberSum(array, targetSum):
	for i in range(len(array)):
	    for j in range(i, len(array)):
		if array[i] + array[j] == targetSum:
		     return [array[i], array[j]]
	return []		



# Solution2: with hash table
# Time complexity: O(n)
# Space complexity: O(n)



# Solution3: with two pointers 
# Time complexity: O(nlog(n))
# Space complexity: O(1)

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
