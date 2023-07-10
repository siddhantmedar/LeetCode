# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        mp = {}
        
        def dfs(root,l):
            if not root:
                return
            
            mp[l] = mp.get(l, root.val)
            mp[l] = root.val
            
            dfs(root.left,l+1)
            dfs(root.right,l+1)
            
        dfs(root,1)
        
        return [v for _,v in mp.items()]