"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def bfs(node):
            if not node:
                return None
            
            mp = {node:Node(node.val)}
            visited = set([node])
            
            q = deque([node])
            
            while q:
                n = len(q)
                
                for k in range(n):
                    nd = q.popleft()
                        
                    for nei in nd.neighbors:
                        if nei not in mp:
                            mp[nei] = Node(nei.val)
                        
                        mp[nd].neighbors.append(mp[nei])
                        
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            
            return mp[node]
        
        return bfs(node)    
            
#         def dfs(node):
#             if node not in mp:
#                 mp[node] = Node(node.val)
            
#             visited.add(node)
            
#             for nei in node.neighbors:
#                 if nei not in mp:
#                     mp[nei] = Node(nei.val)
                    
#                 mp[node].neighbors.append(mp[nei])
                
#                 if nei not in visited:
#                     dfs(nei)
        
        
#         mp = {}
#         visited = set()
        
#         if not node:
#             return None
        
#         dfs(node)
        
#         return mp[node]