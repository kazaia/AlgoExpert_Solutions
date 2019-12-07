# Three number sum 
# Time complexity: O(n^2), because O(n^2) + O(nlog(n)) ~ O(n^2)
# Space ecomplexity: O(n): due to the extra triplets we created, in the worst case we could go store evry single element

# Caveat: The given array is non-empty array with distincts elements 

def threeSum(nums):
    nums.sort()
    triplet = [] 
    for i in range(len(nums) -2):
        left = i + 1
        right = len(nums) -1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if currentSum > 0:
                right -= 1
            elif currentSum < 0:
                left += 1
            elif currentSum == 0:
                triplet.append([nums[i], nums[left], nums[right]])
                left += 1
                right -=1            
    return triplet


