class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(root, par=None):
            visited.add(root)
            
            for nei in graph[root]:
                if nei not in visited:
                    if dfs(nei, root):
                        return True
                    
                elif nei in visited and nei != par:
                    return True
                
            return False
        
        
        visited = set()
        graph = {i:[] for i in range(n)}
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(n):
            if i not in visited:
                if dfs(i):
                    return False
        
        if len(edges) == n-1 and len(visited) == n:
            return True
        
        
        # no cycle+ e=n-1