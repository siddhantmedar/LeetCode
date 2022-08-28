class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = [-1*x for x in stones]
        heapq.heapify(lst)
        
        while len(lst) >= 2:
            stone1 = heapq.heappop(lst)*-1
            stone2 = heapq.heappop(lst)*-1
            
            if stone1 == stone2:
                continue
                
            else:
                
                heapq.heappush(lst, -1*abs(stone1-stone2))
                
        return lst[0]*-1 if lst else 0