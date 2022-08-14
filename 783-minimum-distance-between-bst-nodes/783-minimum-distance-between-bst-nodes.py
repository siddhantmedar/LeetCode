# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            return solve(root.left)+[root.val]+solve(root.right) if root else []
        
        res = float("inf")
        lst = solve(root)
        
        for i in range(len(lst)-1):
            res = min(res, lst[i+1]-lst[i])
        
        return res