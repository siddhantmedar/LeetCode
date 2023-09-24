# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        mp = defaultdict()
        
        def dfs(root,level):
            if not root:
                return 
            
            mp[level] = root.val
            
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        dfs(root,1)
        
        return [v for v in mp.values()]