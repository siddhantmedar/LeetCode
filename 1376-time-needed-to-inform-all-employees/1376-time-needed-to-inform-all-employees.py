class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node, time, par=None):
            nonlocal res
            
            visited.add(node)
            
            if len(graph[node]) == 1 and par in graph[node]:
                res = max(res, time)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, time+informTime[node], node)
        
        graph = defaultdict(list)
        visited = set()
        
        for i, node in enumerate(manager):
            if node == -1:
                continue
            
            graph[i].append(node)
            graph[node].append(i)
            
        res = 0
        
        dfs(headID, 0)
        
        return res