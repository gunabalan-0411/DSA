"""
Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # O(n) Dynamic programming

        def rob_n_skip(nums):
            rob1 = 0
            rob2 = 0
            for n in nums:
                newRob = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2

        return max(nums[0], rob_n_skip(nums[:-1]), rob_n_skip(nums[1:]))

        # O(n*n)
        # Backtracking for linear house robbing solution
        memo = {}

        def dfs(i, end):
            if i > end:
                return 0
            if (i, end) in memo:
                return memo[(i, end)]
            memo[(i, end)] = max(
                dfs(i + 1),  # Explore all possible by skip each
                nums[i]
                + dfs(
                    i + 2
                ),  # after skip rob it and move to house after adjacent house
            )
            return memo[(i, end)]

        # for circular
        return max(dfs(0, len(nums) - 2), dfs(1, len(nums) - 1))
