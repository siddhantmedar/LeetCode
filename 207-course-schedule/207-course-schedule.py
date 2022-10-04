class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        def bfs():
            count = 0
            result = []
            
            q = deque([k for k,v in indegree.items() if v == 0])

            while q:
                nn = len(q)
                
                for k in range(nn):
                    node = q.popleft()
                    count+=1
                    result.append(node)
                    
                    for nei in graph[node]:
                        indegree[nei]-=1
                        
                        if indegree[nei] == 0:
                            q.append(nei)
            
            return True if len(result) == n else False
        
        graph = defaultdict(list)
        indegree = {i:0 for i in range(n)}
        
        for v,u in edges:
            graph[u].append(v)
            indegree[v] = 1+indegree.get(v,0)
            
        return bfs()