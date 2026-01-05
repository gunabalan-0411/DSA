from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            cur_node = self.root
            for char in word:
                if char not in cur_node.children:
                    cur_node.children[char] = TrieNode()
                cur_node = cur_node.children[char]
            cur_node.is_word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary)
        n = len(s)

        dp = {n:0}

        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i+1)
            cur_node = trie.root
            for j in range(i, n):

                if s[j] not in cur_node.children:
                    break
                cur_node = cur_node.children[s[j]]
                if cur_node.is_word:
                    res = min(res, dfs(j+1))
                
            dp[i] = res
            return res
        
        return dfs(0)
