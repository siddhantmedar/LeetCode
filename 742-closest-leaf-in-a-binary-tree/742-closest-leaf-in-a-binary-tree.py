# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, par=None):
            if not root:
                return 
            
            parent[root] = par
            mp[root.val] = root
            
            dfs(root.left,root)
            dfs(root.right, root)
            
            
        mp = {}
        parent = {}
        
        dfs(root)
        
        q = deque([mp[k]])
        visited = set()
        
        while q:
            n = len(q)
            
            for i in range(n):
                node = q.popleft()

                visited.add(node)
                
                if not node.left and not node.right:
                    return node.val
                
                for c in [parent[node], node.left, node.right]:
                    if c and c not in visited:
                        q.append(c)