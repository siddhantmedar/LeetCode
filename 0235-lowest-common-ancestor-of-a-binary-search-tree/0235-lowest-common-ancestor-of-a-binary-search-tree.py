# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(root,p,q):
            if not root:
                return root
            
            if (root.val <= p.val and root.val >= q.val)\
            or (root.val >= p.val and root.val <= q.val):
                return root
            elif (root.val > p.val and root.val > q.val):
                return solve(root.left, p, q)
            else:
                return solve(root.right,p,q)
        
        return solve(root,p,q)