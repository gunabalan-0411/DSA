class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def count_palindrome(s, l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count 
        for i in range(len(s)):
            res += count_palindrome(s, i, i) # odd
            res += count_palindrome(s, i, i+1)
        return res
        
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        count = 0
        def dfs(i):
            if i == len(s):
                return
            nonlocal count
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    count += 1
            dfs(i+1)
            return count
        dfs(0)
        return count