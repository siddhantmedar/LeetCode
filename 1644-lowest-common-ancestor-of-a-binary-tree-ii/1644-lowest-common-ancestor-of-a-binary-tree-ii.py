# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def exists(root, node):
            if not root:
                return False
            
            if root == node:
                return True
            
            left = exists(root.left, node)
            right = exists(root.right, node)
            
            return left or right
        
        def dfs(root, p, q):
            if not root:
                return
            
            if root == p or root == q:
                return root
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            
            if left and right:
                return root
            
            return left or right
        
        
        if not exists(root, p) or not exists(root, q):
            return None
        
        
        return dfs(root, p, q)