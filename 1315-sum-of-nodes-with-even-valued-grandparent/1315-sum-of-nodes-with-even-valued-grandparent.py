# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def solve(root, par=None, gpar=None):
            nonlocal res
            
            if not root:
                return
            
            if gpar and gpar%2 == 0:
                res.append(root.val)
                
            solve(root.left, root.val,par)
            solve(root.right, root.val, par)
            
        res = []
        
        solve(root)
        
        return sum(res)