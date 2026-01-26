from typing import List
from functools import lru_cache


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Attempted

        memo = {}

        @lru_cache(None)
        def dfs(state: tuple) -> int:
            if state in memo:
                return memo[state]

            n = len(state)

            if n == 0:
                return 0
            if n == 1:
                return state[0]

            ans = float("inf")
            for i in range(n):
                for j in range(i + 1, n):
                    diff = abs(state[i] - state[j])

                    nxt = []
                    for k in range(n):
                        if k != i and k != j:
                            nxt.append(state[k])
                    if diff != 0:
                        nxt.append(diff)

                    ans = min(ans, dfs(tuple(sorted(nxt))))
            memo[state] = ans
            return ans

        return dfs(tuple(sorted(stones)))


stones = [[2, 7, 4, 1, 8, 1], [31, 26, 33, 21, 40]]

for stone in stones:
    print(stone)
    print(Solution().lastStoneWeightII(stone))
