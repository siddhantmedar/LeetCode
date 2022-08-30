# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return 0

            if not root.left and not root.right:
                return root.val
            
            if root in dp:
                return dp[root]
            
            inc = root.val

            if root.left:
                inc+=solve(root.left.left)+solve(root.left.right)

            if root.right:
                inc+=solve(root.right.left) + solve(root.right.right)

            exc = 0

            if root.left:
                exc+=solve(root.left)

            if root.right:
                exc+=solve(root.right)
            
            dp[root] = max(inc, exc)
            
            return dp[root]
        
        dp = defaultdict()
        
        return solve(root)