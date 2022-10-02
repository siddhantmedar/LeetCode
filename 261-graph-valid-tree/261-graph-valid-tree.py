class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        def dfs(node, parent=None):
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    if not dfs(nei, node):
                        return False
                    
                elif nei in visited and nei != parent:
                    return False
            
            return True
            
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        
        for i in range(n):
            if i not in visited:
                if not dfs(i):
                    return False
                
        return True