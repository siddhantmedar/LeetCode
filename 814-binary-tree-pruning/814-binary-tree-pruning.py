# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(root):
            if not root:
                return root
            
            if not root.left and not root.right:
                return root if root.val == 1 else None
            
            root.left = solve(root.left)
            root.right = solve(root.right)
            
            if root.val == 1 or root.left or root.right:
                return root
            
            return None
        
        return solve(root)
        