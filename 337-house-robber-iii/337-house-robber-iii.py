# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return root.val
    
        inc = root.val
        
        if root.left:
            inc+=self.rob(root.left.left)+self.rob(root.left.right)
            
        if root.right:
            inc+=self.rob(root.right.left) + self.rob(root.right.right)
            
        exc = 0
        
        if root.left:
            exc+=self.rob(root.left)
            
        if root.right:
            exc+=self.rob(root.right)
            
        return max(inc, exc)