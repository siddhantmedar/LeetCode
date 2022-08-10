class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        graph = defaultdict(list)
        
        for i in range(len(rooms)):
            graph[i].extend(rooms[i])
            
        visited = set()
        
        dfs(0)
        
        return len(visited) == len(rooms)