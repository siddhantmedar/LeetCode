# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def link(root,parent=None):
            nonlocal par
            
            if not root:
                return
            
            par[root] = parent if parent else None
            
            link(root.left,root)
            link(root.right,root)
            
        def dfs(root):
            nonlocal mp
            
            if not root:
                return
            
            mp[root.val] = root
            
            dfs(root.left)
            dfs(root.right)
        
        
        def bfs(node):
            nonlocal par
            
            if not node:
                return
            
            q = [node]
            timer = 0
            visited = set()
            
            while q:
                n = len(q)
                
                for _ in range(n):
                    node = q.pop(0)
                    visited.add(node)
                    
                    for nei in (node.left, node.right, par[node]):
                        if nei and nei not in visited:
                            q.append(nei)
                            visited.add(nei)
                timer+=1
            
            return max(timer-1,0)
            
        
        par = dict()
        mp = dict()
        
        link(root)
        dfs(root)
        
        return bfs(mp[start])
        