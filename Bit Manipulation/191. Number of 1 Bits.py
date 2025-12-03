class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            # AND Operation of 1 with last digit of binary sequence
            # 1 & 1 = 1, 1 & 0 = 0
            count += n & 1
            # shifting by 1 bit to right (last bit will be removed)
            n >>= 1
        return count