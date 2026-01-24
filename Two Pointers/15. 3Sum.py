from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # sorting it to work better for two pointer

        """
        sort the list and iterate each neg num find its remaining two number which adds to 0 by using two pointers
        """
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1  # noqa: E741
            while l < r:
                threeSum = nums[l] + nums[r] + a
                if threeSum == 0:
                    result.append([nums[l], nums[r], a])
                    l += 1  # noqa: E741
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1  # noqa: E741
                elif threeSum < 0:
                    l += 1  # noqa: E741
                else:
                    r -= 1
        return result
