# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return root.val
            
            if root in dp:
                return dp[root]
            
            include = root.val
            
            if root.left:
                include+=dfs(root.left.left)+dfs(root.left.right)
            if root.right:
                include+=dfs(root.right.left)+dfs(root.right.right)
            
            exclude = 0
            
            if root.left:
                exclude+=dfs(root.left)
            if root.right:
                exclude+=dfs(root.right)
                
            dp[root] = max(include,exclude)
            
            return dp[root]
        
        
        dp = {}
        
        return dfs(root)