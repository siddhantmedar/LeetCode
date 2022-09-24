class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
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
            
            
        
        