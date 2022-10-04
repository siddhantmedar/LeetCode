# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        def solve(root):
            nonlocal prefix, result
            
            if not root:
                return
            
            prefix+=root.val
            
            if prefix-target in mp:
                result+=mp[prefix-target]
                
            mp[prefix] = 1+mp.get(prefix,0)
            
            solve(root.left)
            solve(root.right)
            
            mp[prefix]-=1
            
            if not mp[prefix]:
                del mp[prefix]
                
            prefix-=root.val
            
                
        mp = {0:1}
        result = 0
        prefix = 0
        
        solve(root)
        
        return result