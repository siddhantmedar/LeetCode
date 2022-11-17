# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal result
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            left = left if left > 0 else 0
            right = right if right > 0 else 0
            
            result = max(result, left+right+root.val)
            
            return max(left, right)+root.val
        
        
        result = float("-inf")
        
        dfs(root)
        
        return result