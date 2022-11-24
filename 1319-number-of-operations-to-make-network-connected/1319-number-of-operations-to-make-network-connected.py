class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        def bfs(node):
            q = deque([node])
            visited.add(node)
            
            while q:
                n = len(q)
                
                for _ in range(n):
                    node = q.popleft()
                    
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)                        
        
        
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
                bfs(i)
                cnt+=1
                
        return cnt-1
    
        #TC O(V+E)