# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent = {}
        
        def dfs(root, level, par = None):
            if not root:
                return
            
            parent[root.val] = (level, par)
        
            dfs(root.left, level+1, root)
            dfs(root.right, level+1, root)
            
        dfs(root,1)
        
        return parent[x][0] == parent[y][0] and parent[x][1] != parent[y][1]