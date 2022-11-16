# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root,level):
            if not root:
                return float("inf")
            
            result = float("inf")
            
            if not root.left and not root.right:
                result = min(result, level)
            
            
            return min(result, dfs(root.left, level+1), dfs(root.right, level+1))

        
        if not root:
            return 0
        
        return dfs(root,1)