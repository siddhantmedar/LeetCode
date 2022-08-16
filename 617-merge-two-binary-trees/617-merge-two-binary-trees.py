# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(p,q):
            if not p:
                return q
            
            if not q:
                return p
            
            p.val+=q.val
            
            p.left = solve(p.left, q.left)
            p.right = solve(p.right, q.right)
            
            return p
        
        return solve(p,q)
            
        
        