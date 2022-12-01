class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node, t):
            visited.add(node)
            
            res = t
            
            for nei in graph[node]:
                res=max(res,dfs(nei,t+informTime[node]))
            
            return res
        
        
        graph = defaultdict(set)
        
        for i in range(len(manager)):
            graph[manager[i]].add(i)
        
        visited = set()
        
        return dfs(headID,0)