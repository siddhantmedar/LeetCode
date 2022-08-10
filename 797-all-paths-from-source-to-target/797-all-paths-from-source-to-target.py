class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def DFS():
            res = []
            path = []
            
            def dfs(node):
                path.append(node)
                
                if node == len(graph)-1:
                    res.append(path.copy())
                    path.remove(node)
                    return
                
                for nei in mp[node]:
                    dfs(nei)
                    
                path.remove(node)
            
            dfs(0)
            
            return res
        
        def BFS():
            res = []
            q = deque([(0,[0])])

            while q:
                k = len(q)

                for i in range(k):
                    node, path = q.popleft()

                    if node == len(graph)-1:
                        res.append(path)

                    for nei in mp[node]:
                        q.append((nei,path+[nei]))

            return res
        
        mp = defaultdict(list)
        
        for i in range(len(graph)):
            mp[i].extend(graph[i])
            
        return DFS()