# Maximum suset sum with no adjacent elements 


def rob(array):
    maxSums = array[:]
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array[0], array[1])
    if len(array) > 2:
        for i in range(2, len(array)):
            maxSums[i] = max(maxSums[i -1] , maxSums[i -2] + array[i])
    return maxSums[-1]
