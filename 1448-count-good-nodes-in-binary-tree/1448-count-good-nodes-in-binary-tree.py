# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root, mx=float("-inf")):
            nonlocal cnt
            
            if not root:
                return
            
            if mx<=root.val:
                cnt+=1
                
            solve(root.left, max(mx, root.val))
            solve(root.right, max(mx, root.val))
            
            
        cnt = 0
        
        solve(root)
        
        return cnt