# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(root, p, q):
            if p.val < root.val and q.val < root.val:
                return solve(root.left, p, q)
            
            elif p.val > root.val and q.val > root.val:
                return solve(root.right, p, q)
            
            else:
                return root
            
        return solve(root, p, q)