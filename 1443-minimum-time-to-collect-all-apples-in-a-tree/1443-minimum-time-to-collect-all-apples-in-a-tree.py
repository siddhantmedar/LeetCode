class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node):
            visited.add(node)
            
            if hasApple[node]:
                res.update(path)
                
            for nei in graph[node]:
                if nei not in visited:
                    path.add((node,nei))
                    dfs(nei)
                    path.remove((node,nei))
                
        
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
           
        res = set()
        path = set()
        visited = set()
        
        dfs(0)
        
        return len(res)*2