class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greed = [x for x in g]
        bis = [x for x in s]
        
        heapq.heapify(greed)
        heapq.heapify(bis)
        
        cnt = 0
        
        while greed and bis:
            b = heapq.heappop(bis)
            
            if greed[0] <= b:
                cnt+=1
                heapq.heappop(greed)
                
        return cnt

    # [1 2 3]  [3,1,2]