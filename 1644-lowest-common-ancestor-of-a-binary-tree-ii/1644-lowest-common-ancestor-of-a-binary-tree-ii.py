# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def exists(root, target):
            if not root:
                return False
            
            if root == target:
                return True
            
            return exists(root.left, target) or exists(root.right, target)
        
        def solve(root, p, q):
            if not root:
                return root
            
            if root == p or root == q:
                return root

            left = solve(root.left,p,q)
            right = solve(root.right,p,q)

            if left and right:
                return root
            
            if left or right:
                return left if left else right
            
        if exists(root, p) and exists(root, q):
            return solve(root, p, q)

        else:
            return None