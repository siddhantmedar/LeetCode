# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(p,q):
            if not p:
                return q
            
            if not q:
                return p
            
            p.val+=q.val
            
            p.left = merge(p.left,q.left)
            p.right = merge(p.right,q.right)
            
            return p
        
        
        return merge(root1, root2)