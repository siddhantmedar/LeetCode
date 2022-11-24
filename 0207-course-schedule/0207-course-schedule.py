class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
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
        
        for i in range(n):
            if i not in visited:
                if not dfs(i):
                    return False
                
        # print(st)
        
        return True