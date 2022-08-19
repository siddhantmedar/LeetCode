# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        res = None
        
        def solve(root):
            nonlocal res
            
            if not root:
                return
            
            if root.val <= p.val:
                solve(root.right)
                
            else:
                res = root
                solve(root.left)
                
        solve(root)
        
        return res