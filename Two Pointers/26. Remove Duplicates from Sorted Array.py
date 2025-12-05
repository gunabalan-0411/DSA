from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Using two pointers
        l, r = 0, 0
        n = len(nums)
        
        while r < n:
            nums[l] = nums[r]
            while r < n and nums[l] == nums[r]:
                r += 1
            l += 1

        return l