class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node):
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)            
            
        graph = defaultdict(list)
        indegree = {i:0 for i in range(n)}
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v]+=1    
            
        q = deque()
        
        for ele, count in indegree.items():
            if count == 0:
                q.append(ele)
        
        visited = set()
    
        result = []
        
        while q:
            node = q.popleft()
            result.append(node)
            
            dfs(node)
            
            if len(visited) == n:
                return result
            
            # O(V*(V+E))