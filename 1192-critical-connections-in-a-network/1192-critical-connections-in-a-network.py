class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(node, parent):
            nonlocal timer
            timer+=1
            
            tin[node] = timer
            low[node] = timer
            
            visited.add(node)
            
            for nei in graph[node]:
                if nei == parent:
                    continue
                    
                if nei not in visited:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])
                    
                    if low[nei] > tin[node]:
                        res.append([node, nei])
                else:
                    low[node] = min(low[node], tin[nei])
                        
            
        timer = 0
        low = {}
        tin = {}
        
        graph = defaultdict(list)
        
        visited = set()
        res = []
        
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                
        return res
        