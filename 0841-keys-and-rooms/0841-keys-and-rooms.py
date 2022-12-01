class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
                    
        
        graph = defaultdict(set)
        
        for i,lst in enumerate(rooms):
            graph[i].update(set(lst))
        
        visited = set()
        
        dfs(0)
        
        return True if len(visited) == len(rooms) else False