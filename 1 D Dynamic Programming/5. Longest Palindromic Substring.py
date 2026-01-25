class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        resIdx = 0
        resLen = 0
        n = len(s)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1
        return s[resIdx : resIdx + resLen]

        memo = {}

        def dfs(l, r):
            if l >= r:
                return ""
            if (l, r) in memo:
                return memo[(l, r)]

            if s[l:r] == s[l:r][::-1]:
                memo[(l, r)] = s[l:r]
                return memo[(l, r)]

            left = dfs(l, r - 1)
            right = dfs(l + 1, r)

            memo[(l, r)] = left if len(left) > len(right) else right
            return memo[(l, r)]

        return dfs(0, len(s))


s = "babad"
print(Solution().longestPalindrome(s=s))
