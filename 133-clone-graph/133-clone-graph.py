"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def bfs(src):
            if not src:
                return 
            
            visited = set()
            mp = {}
            
            mp[src] = Node(src.val)
            visited.add(src)
            
            q = deque([src])
            
            while q:
                n = len(q)
                
                for k in range(n):
                    node = q.popleft()
                    
                    for nei in node.neighbors:
                        mp[nei] = mp.get(nei, Node(nei.val))
                        
                        mp[node].neighbors.append(mp[nei])
                        
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                            
            return mp[src]
        
            
        return bfs(node)
        