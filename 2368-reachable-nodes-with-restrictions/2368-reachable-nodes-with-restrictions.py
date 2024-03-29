class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def bfs():
            q = deque([0])
            
            cnt = 0
            
            while q:
                k = len(q)
                
                for _ in range(k):
                    node = q.popleft()
                    cnt+=1
                    
                    for nei in graph[node]:
                        if nei not in visited and nei not in restricted:
                            visited.add(nei)
                            q,append(nei)
                            
            return len(visited)
        
        
        def dfs(node):
            if node in restricted:
                return 0
            
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        
        restricted = set(restricted)
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        
        dfs(0)
        
        # print(graph,visited)
        
        # return len(visited)
        
        return bfs()