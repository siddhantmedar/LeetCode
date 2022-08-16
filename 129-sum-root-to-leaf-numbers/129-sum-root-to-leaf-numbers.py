# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            nonlocal res
            
            if not root:
                return
            
            path.append(root.val)
            
            if not root.left and not root.right:
                res.append("".join([str(x) for x in path]))
                path.pop()
                return
            
            solve(root.left)
            solve(root.right)
            
            path.pop()
            
        res = []
        path = []
        
        solve(root)
        
        return sum([int(x) for x in res])