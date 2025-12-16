# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        path = 0
        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)
            # Bottom up so to calculate height from bottom
            nonlocal path
            path = max(path, left+ right)
            return 1 + max(left, right)


        dfs(root)
        return path
            