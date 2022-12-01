class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        
        indegree = {i:0 for i in range(1,n+1)}
        
        for u,v in relations:
            graph[u].add(v)
            indegree[v]+=1
            
        # print(graph)
        # print(indegree)
        
        level = None
        cnt = 0
        
        q = deque([(i,1) for i in range(1,n+1) if indegree[i]==0])
        
        while q:
            k = len(q)
            
            for _ in range(k):
                node,level = q.popleft()
                cnt+=1
                
                for nei in graph[node]:
                    if indegree[nei] > 0:
                        indegree[nei]-=1
                    
                        if indegree[nei]==0:
                            q.append((nei,level+1))
        
        # print(level)
        
        return level if cnt == n else -1