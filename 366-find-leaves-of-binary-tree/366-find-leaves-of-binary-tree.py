# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def solve(root):
            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)
            
            height = max(left, right)
            
            mp[height].append(root.val)
            
            return 1+height
        
        mp = {i:[] for i in range(101)}
        res = []
        
        solve(root)
        
        for _, v in mp.items():
            if v:
                res.append(v)
        
        return res