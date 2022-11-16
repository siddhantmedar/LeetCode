# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root,level):
            nonlocal result
            
            if not root:
                return 
            
            if not root.left and not root.right:
                result = min(result, level)
            
            dfs(root.left, level+1)
            dfs(root.right, level+1)
            
            
        result = float("inf")
        
        if not root:
            return 0
        
        dfs(root,1)
        
        return result
    