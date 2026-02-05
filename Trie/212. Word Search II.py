from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def add(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.add(word)

        res, visit = set(), set()
        ROWS, COLS = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c, node, word):
            if (
                r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or
                board[r][c] not in node.children
            ):
                return 
            visit.add((r, c))
            
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            for dr, dc in directions:
                dfs(r+dr, c+dc, node, word)
            visit.remove((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, "")
        return list(res)






