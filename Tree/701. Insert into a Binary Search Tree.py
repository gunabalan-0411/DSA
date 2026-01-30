# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        def dfs(node):
            if not node:
                return
            
            if val < node.val and not node.left:
                node.left = TreeNode(val)
                return
            elif val > node.val and not node.right:
                node.right = TreeNode(val)
                return
            if val < node.val:
                dfs(node.left)
            elif val > node.val:
                dfs(node.right)
                
            return


        dfs(root)
        return root