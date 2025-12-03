from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR two numbers always return 0
        # keeping XOR will finally yield the result as XOR 0 with n gives n
        res = 0
        for n in nums:
            res ^= n
        return res