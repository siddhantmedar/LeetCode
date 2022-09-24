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
            if node:
                visited.add(node)

                if node not in clone:
                    clone[node] = Node(node.val)

                for nei in node.neighbors:
                    if nei not in clone:
                        clone[nei] = Node(nei.val)

                    clone[node].neighbors.append(clone[nei])

                for nei in node.neighbors:
                    if nei not in visited:
                        dfs(nei)
                        
        if not node:
            return node
        
        clone = {}
        visited = set()
        
        dfs(node)
        
        return clone[node]
        