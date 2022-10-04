# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, row, col):
            if not root:
                return
            
            # mp[dist].append(root.val)
            q.append((col, row, root.val))
            
            dfs(root.left, row+1, col-1)
            dfs(root.right, row+1, col+1)
            
        q = []
        
        dfs(root, 0, 0)
        
        q.sort()
        
        mp = defaultdict(list)
        
        for col, row, val in q:
            mp[col].append(val)
        
        return [v for k,v in mp.items()]