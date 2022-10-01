"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return
            
            visited.add(node)
            
            if node not in mp:
                mp[node] = Node(node.val)
                
            for nei in node.neighbors:
                if nei not in mp:
                    mp[nei] = Node(nei.val)
                
                mp[node].neighbors.append(mp[nei])
                
                if nei not in visited:
                    dfs(nei)
            
        mp = defaultdict()
        visited = set()
        
        dfs(node)
        
        return mp[node] if node in mp else None