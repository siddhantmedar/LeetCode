# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal mx 
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            left = 0 if left < 0 else left
            right = 0 if right < 0 else right
            
            mx = max(mx, left+right+root.val)
            
            return max(left, right) + root.val
        
        mx = float("-inf")
        
        dfs(root)
        
        return mx