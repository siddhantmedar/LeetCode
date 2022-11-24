# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check(root, target):
            if not root:
                return False
            
            if root == target:
                return True
            
            return check(root.left,target) or check(root.right,target)
        
        def dfs(root):
            if not root:
                return root
            
            if root == p or root == q:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left and right:
                return root
            
            return left or right
        
        if not check(root,p) or not check(root,q):
            return None
        
        return dfs(root)