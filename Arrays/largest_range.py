# Largest range

# Time complexity: O(nlog(n))
# Space complexity: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) ==1:
            return 1
        longest_count = 1
        current_count = 1
        nums.sort()
        for i in range(len(nums) -1):
            if nums[i] != nums[i+1]:
                if nums[i] +1 == nums[i+1]:
                    current_count += 1
                else:
                    longest_count = max(longest_count, current_count)
                    current_count = 1               
        return max(longest_count, current_count)
            
  
# Time complexity:O(n)
# Space complexity: O(n)
def largestRange(array):
    bestRange  = []
    longestLength = 0
    dict = {}
    for num in array:
        dict[num] = True
    for num in array:
        if not dict[num]:
            continue
        dict[num] = False
        currentLength =1
        left = num - 1
        right = num + 1
        while left in dict:
            dict[left] = False
            currentLength += 1
            left -= 1
        while right in dict:
            dict[right] = False
            currentLength += 1
            right += 1
            
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left +1, right -1]
            
        return bestRange
