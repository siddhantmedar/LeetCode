# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def dfs(root, level):
            if not root:
                return
            
            mp[level].append(root.val)
            
            dfs(root.left, level+1)
            dfs(root.right, level+1)
            
        mp = defaultdict(list)
        
        dfs(root,1)
        
        print(mp)
        
        result = []
        
        for k,v in mp.items():
            result.append(sum(v)/len(v))
        
        return result