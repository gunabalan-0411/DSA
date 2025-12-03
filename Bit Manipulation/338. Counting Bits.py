class Solution:
    def countBits(self, n: int) -> List[int]:
        
        '''
        Pattern Analysis:
        For every power of 2 such as (2, 4, 8, 16, 32..)
        We need to update the offset to that iteration
        dp[i] = 1 + dp[i-offset]

        It means for every power of 2 if we add 1 + power of 2 before elements value we get the result
        '''

        # Dynamic programming approach
        dp = [0] * n*1
        offset = 1
        for i in range(1, n+1):
            # Update the offset for every power of 2
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp