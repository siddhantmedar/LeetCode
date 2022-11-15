class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        
        heapq.heapify(heap)
        
        while heap and len(heap) >= 2:
            stone1, stone2 = heapq.heappop(heap)*-1, heapq.heappop(heap)*-1
            
            if stone1 == stone2:
                continue
                
            else:
                diff = stone1-stone2 if stone1 > stone2 else stone2-stone1
                heapq.heappush(heap, diff*-1)
        
        if heap:
            return heap[0]*-1
        else:
            return 0