class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        
        if len(edges) < n-1:
            return -1
        
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        visited = set()
        cnt = 0
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt+=1
                
        return cnt-1