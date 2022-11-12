class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node,par=None):
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    if not dfs(nei,node):
                        return False
                    
                elif nei != par:
                    return False
                
            return True
            
        graph = defaultdict(set)
        visited = set()
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        for i in range(n):
            if i not in visited:
                if not dfs(i):
                    return False
        
        return True if len(edges) == n-1 else False