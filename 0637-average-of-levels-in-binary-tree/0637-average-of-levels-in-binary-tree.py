# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        mp = defaultdict(list)
        
        def dfs(root, l):
            if not root:
                return
            
            mp[l].append(root.val)
            
            dfs(root.left, l+1)
            dfs(root.right, l+1)
            
        dfs(root,1)
        
        return [sum(v)/len(v) for _,v in mp.items()]