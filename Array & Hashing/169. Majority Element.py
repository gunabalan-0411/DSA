from typing import List
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore voting algorithm
        res, count = 0, 0
        for n in nums:
            # Whenever we saw a new number we assume that could be the pottential high number
            # As the potential high number could be make the previous high num count as 0
            if count == 0:
                res = n
            count += (1 if res == n else -1)
        return res
        # Time O(n), Space O(n)
        count_nums = defaultdict(int)
        res, maxCount = 0, 0
        for n in nums:
            count_nums[n] += 1
            if maxCount < count_nums[n]:
                maxCount = count_nums[n]
                res = n
        return res


