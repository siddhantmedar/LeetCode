# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            
            if (not p and q) or (p and not q):
                return False
            
            return p.val == q.val and check(p.left, q.left) and check(p.right, q.right)
        
        return check(p,q)