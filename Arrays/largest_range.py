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
            
  
