# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        def dfs(root):
            nonlocal sm,cnt
            
            if not root:
                return
            
            sm+=root.val
            
            if sm-target in mp:
                cnt+=mp[sm-target]
                
            mp[sm] = 1+mp.get(sm,0)
            
            dfs(root.left)
            dfs(root.right)
            
            mp[sm]-=1
            
            if mp[sm] == 0:
                del mp[sm]
            
            sm-=root.val
            
        
        cnt = 0
        sm = 0
        
        mp = {0:1}
                                                    
        dfs(root)
        
        return cnt