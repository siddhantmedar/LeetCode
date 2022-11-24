class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(node,parent):
            visited.add(node)
            
            if parent != node:
                result[node].append(parent)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei,parent)
            
        
        result = {node:list() for node in range(n)}
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
        
        for node in range(n):
            visited = set()
            dfs(node,node)
        
        return [v for k,v in result.items()]