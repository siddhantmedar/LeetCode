# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, left=None):
            nonlocal sm
            
            if not root:
                return
            
            if (not root.left and not root.right) and left:
                sm+=root.val
                return
            
            dfs(root.left, 1)
            dfs(root.right,0)
        
        sm = 0
        
        dfs(root)
        
        return sm