from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        min_sub_arr_len = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_sub_arr_len = min(min_sub_arr_len, r - l + 1)
                total -= nums[l]
                l += 1
        return min_sub_arr_len if min_sub_arr_len != float("inf") else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(Solution().minSubArrayLen(target=target, nums=nums))
