class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x,y):
            if parent[(x,y)] != (x,y):
                parent[(x,y)] = find(parent[(x,y)][0],parent[(x,y)][1])
                
            return parent[(x,y)]
                
        def union(x,y,i,j):
            setX = find(x,y)
            setY = find(i,j)
            
            if setX != setY:
                parent[setY] = setX
                return True
            
            return False
            
        
        heap = []
        
        for (u,v) in points:
            for (i,j) in points:
                if (u,v) == (i,j):
                    continue
                dist = abs(u-i)+abs(v-j)
                heap.append((dist,(u,v),(i,j)))
                
        heapq.heapify(heap)
        
        parent = {(x,y):(x,y) for (x,y) in points}
        result = 0
        cnt = 0
        
        while heap:
            if cnt == len(points)-1:
                break
            
            dist,node1,node2 = heapq.heappop(heap)
            
            if union(node1[0],node1[1],node2[0],node2[1]):
                result+=dist
                cnt+=1
                
        return result