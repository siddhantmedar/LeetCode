# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def dfs(root):
            if not root:
                return root
            
            if root in nodes:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left and right:
                return root
            
            return left or right
        
        return dfs(root)