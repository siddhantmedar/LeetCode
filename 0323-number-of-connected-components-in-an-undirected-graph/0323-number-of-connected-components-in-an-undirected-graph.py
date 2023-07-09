class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
                
            
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        visited = set()
        cnt = 0
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                cnt+=1
                
        return cnt