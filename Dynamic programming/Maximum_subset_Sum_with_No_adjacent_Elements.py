# Maximum suset sum with no adjacent elements 


def maxSubsetSumNoAdjacent(array):
    maxSums = array[:]
	if not array:
		return 0
	if len(array) == 1:
		return array[0]
	if len(array) == 2:
		return max(array[0], array[1])
	for i in range(2, len(array)):
		maxSums[i] = max( maxSums[i-2] + array[i], maxSums[i-1])
	return maxSums[-1]	






