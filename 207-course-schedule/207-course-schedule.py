class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        def DFS():
            def dfs(node):
                visited.add(node)    
                rec.append(node)

                for nei in graph[node]:
                    if nei not in visited:
                        if not dfs(nei):
                            return False

                    elif nei in rec:
                        return False

                rec.remove(node)
                return True


            graph = defaultdict(list)
            visited = set()
            rec = []

            for u, v in edges:
                graph[u].append(v)

            for i in range(n):
                if i not in visited:
                    if not dfs(i):
                        return False
            return True
            
        def BFS():
            graph = defaultdict(list)
            
            visited = set()
            indegree = {x:0 for x in range(n)}
            
            for u, v in edges:
                graph[u].append(v)
                indegree[v] = 1 + indegree.get(v, 0)
                
            q = deque()
            
            for k,v in indegree.items():
                if v == 0:
                    q.append(k)
            
            while q:
                node = q.popleft()
                visited.add(node)
                
                for nei in graph[node]:
                    indegree[nei]-=1
                    
                    if indegree[nei] == 0:
                        q.append(nei)
            
            print(visited)
            return len(visited) == n
        
        
        return BFS()
        