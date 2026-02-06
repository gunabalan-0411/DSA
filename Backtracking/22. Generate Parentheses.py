from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(p, open_b, close):
            nonlocal res
            if p and p[0] == ')':
                return
            if open_b+close >= 2*n and p[-1] != '(':
                res.append(p)
                return
            if open_b < n:
                p += '('
                dfs(p, open_b+1, close)
                p = p[:-1]
            if close < open_b:
                p += ')'
                dfs(p, open_b, close+1)
                p = p[:-1]

        dfs('', 0, 0)
        return res