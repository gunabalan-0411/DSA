from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # Starting with DFS to understand to understand the decision tree first

        # def dfs(i, cur_sum):
        #     # Exit condition with values
        #     if cur_sum == amount:
        #         return 1
        #     if i == len(coins) or cur_sum > amount:
        #         return 0

        #     cur_sum += coins[i]
        #     # Trying out all possible combination
        #
        #     return  dfs(i, cur_sum) + dfs(i+1, cur_sum-coins[i])

        # return dfs(0, 0)
        # -- Got Time limit exceed

        # Dynamic Programming
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        # assuming we make 0 amount using any coin
        # So assigning 1 to all nums at position 0
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]  # piling up coins to make the current amount
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]
