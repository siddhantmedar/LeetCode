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
            st.append(node)
            
            return True
        
        
        graph = defaultdict(list)
        
        for v,u in edges:
            graph[u].append(v)
            
        visited = set()
        rec = set()
        st = []
        
        for i in range(n):
            if i not in visited:
                if not dfs(i):
                    return False
                
        return True