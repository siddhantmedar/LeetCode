class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        
        heap = [(0,tuple(points[0]))]

        n = len(points)
        cnt = 0
        
        result = 0
        
        while cnt < n:
            cost,node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)

            result+=cost
            
            cnt+=1

            for nei in points:
                if tuple(nei) not in visited:
                    dist = abs(node[0]-nei[0]) + abs(node[1]-nei[1])
                    heapq.heappush(heap,(dist,tuple(nei)))
       
    
        return result