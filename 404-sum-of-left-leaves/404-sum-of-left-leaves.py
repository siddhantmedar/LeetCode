# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def solve(root, side=None):
            nonlocal sm
            
            if not root:
                return 
            
            if not root.left and not root.right and side == 0:
                sm+=root.val
            
            solve(root.left, 0)
            solve(root.right, 1)            
            
        sm = 0
        
        solve(root)
        
        return sm