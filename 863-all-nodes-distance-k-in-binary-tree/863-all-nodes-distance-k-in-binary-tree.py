# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root, parent=None):
            if not root:
                return
            
            mp[root] = parent
                
            dfs(root.left, root)
            dfs(root.right, root)
            
        
        mp = dict()
        
        dfs(root)
        
        visited = set()
        q = deque([(0,target)])
        visited.add(target)
        
        while q:
            n = len(q)
            
            if q and q[0][0] == k:
                return [x[1].val for x in q]
            
            for y in range(n):
                dist, node = q.popleft()
                
                for nei in (node.left, node.right, mp[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append((dist+1, nei))
            
        return []