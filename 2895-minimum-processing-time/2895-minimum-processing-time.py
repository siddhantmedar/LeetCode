class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        heap = [-x for x in tasks]
        heapq.heapify(heap)
        
        res = float("-inf")
        
        for t in sorted(processorTime):
            curr = t
            cnt = 0
            mx = float("-inf")
        
            while heap and cnt < 4:
                tsk = -heapq.heappop(heap)
                mx = max(mx,curr+tsk)
                
                cnt+=1
                
            res = max(res, mx)
            
        return res
                
            