class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(list)
        n = len(graph)
        for i in range(len(graph)):
            mp[i].extend(graph[i])
            
        res = []
        
        q = deque([(0,[0])])
        
        while q:
            k = len(q)
            
            for i in range(k):
                node, path = q.popleft()
                
                if node == n-1:
                    res.append(path)
                    
                for nei in mp[node]:
                    q.append((nei,path+[nei]))
                  
        return res