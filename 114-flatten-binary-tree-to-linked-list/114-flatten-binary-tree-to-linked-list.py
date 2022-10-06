# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def solve(root):
            if not root:
                return None
            
            solve(root.left)
            solve(root.right)
            
            tmp = root.right
            
            root.right = root.left
            root.left = None
            
            tmp1 = root
            
            while tmp1.right:
                tmp1 = tmp1.right
                
            tmp1.right = tmp
            
            return root
        
        return solve(root)