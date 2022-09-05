# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def solve(root):
            if not root:
                return
            
            mp[root.val] = 1+mp.get(root.val, 0)
            
            solve(root.left)
            solve(root.right)
            
        mp = {}
        solve(root)
        mx = max([v for _, v in mp.items()])
        
        res = []
        
        for k,v in mp.items():
            if v == mx:
                res.append(k)
                
        return res
        