# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def solve(root):
            if not root:
                return root

            if root in set(st):
                return root

            left = solve(root.left)
            right = solve(root.right)

            if left and right:
                return root

            return left or right
    
        st = set(nodes)
        
        return solve(root)