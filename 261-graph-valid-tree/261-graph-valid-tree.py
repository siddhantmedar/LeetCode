class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # two conditions:
        #     no cycle
        #     e = v-1
        
        def dfs(node, parent=None):
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    if not dfs(nei, node):
                        return False
                    
                elif nei in visited and nei != parent:
                    return False
                
            return True
            
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        
        for i in range(n):
            if i not in visited:
                if not dfs(i):
                    return False
                
        return True
        