# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,p,q):
            if (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val):
                return root
            
            if root.val==p.val or root.val==q.val:
                return root
            
            if (p.val > root.val and q.val > root.val):
                return dfs(root.right,p,q)
            else:
                return dfs(root.left,p,q)
            
        
        return dfs(root,p,q)