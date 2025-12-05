from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Brute Force
        # temp = []
        # for n in nums:
        #     if n == val:
        #         continue
        #     else:
        #         temp.append(n)
        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        # return len(temp)

        # Two pointers
        l = 0
        r = len(nums)
        while l < r:
            if nums[l] == val:
                r -= 1
                nums[l] = nums[r]
            else:
                l += 1
        return r