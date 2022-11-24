class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        def bfs():
            graph = defaultdict(set)
            indegree = {node:0 for node in range(n)}
            
            for u,v in edges:
                graph[v].add(u)
                indegree[u]=1+indegree.get(u,0)
            
            cnt = 0
            result = []
            
            q = deque([node for node,cnt in indegree.items() if cnt == 0])
            
            while q:
                k = len(q)
                
                for _ in range(k):
                    node = q.popleft()
                    result.append(node)
                    
                    cnt+=1
                    
                    for nei in graph[node]:
                        indegree[nei]-=1
                        
                        if indegree[nei] == 0:
                            q.append(nei)
                            
            return cnt if cnt == len(indegree) else []
            
        
        def dfs(node):
            visited.add(node)
            rec.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    if not dfs(nei):
                        return False
            
                elif nei in rec:
                    return False
                
            rec.remove(node)
            st.appendleft(node)
            
            return True
            
            
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[v].add(u)
            
        visited = set()
        rec = set()
        st = deque()
        
#         for i in range(n):
#             if i not in visited:
#                 if not dfs(i):
#                     return False
                
#         # print(st)
        
#         return True

        return bfs()