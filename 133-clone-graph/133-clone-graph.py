"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def DFS():
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
    
        def BFS(src):
            if not src:
                return src

            clone = {}
            visited = set()

            clone[src] = Node(src.val)
            visited.add(src)
            
            q = deque([src])
            
            while q:
                node = q.popleft()
                
                for nei in node.neighbors:
                    clone[nei] = clone.get(nei, Node(nei.val))
                    
                    clone[node].neighbors.append(clone[nei])
                    
                for nei in node.neighbors:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            return clone[src]
        

        return BFS(node)