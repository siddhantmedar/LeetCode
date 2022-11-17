# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root,par=None):
            if not root:
                return 
            
            parent[root] = par
                
            dfs(root.left,root)
            dfs(root.right,root)
            
        
        if not root:
            return
        
        parent = {}
        
        dfs(root)
        
        visited = set([target])
        
        q = deque([target])
        
        while q:
            n = len(q)
            
            if k == 0:
                return [x.val for x in q]
                
            for _ in range(n):
                node = q.popleft()
                
                for nei in {node.left, node.right, parent[node]}:
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            
            k-=1            
        
        return []