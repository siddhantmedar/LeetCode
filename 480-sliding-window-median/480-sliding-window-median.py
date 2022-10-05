class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def add(ele):
            heapq.heappush(mx, -1*ele)
            
            heapq.heappush(mn, -1*heapq.heappop(mx))
            
            while len(mn) > len(mx):
                heapq.heappush(mx, -1*heapq.heappop(mn))
            
        def getMedian():
            if len(mx) > len(mn):
                return -1*mx[0]
            
            else:
                return (-1*mx[0] + mn[0]) / 2
            
        def updateHeaps(ele):
            if ele <= -1*mx[0]:
                mx.remove(-1*ele)
                heapq.heapify(mx)
                
            else:
                mn.remove(ele)
                heapq.heapify(mn)
        
        
        mn, mx = [], []
        
        result = []
        
        for i in range(k):
            add(nums[i])
            
        result.append(getMedian())
        
        for i in range(k, len(nums)):
            updateHeaps(nums[i-k])
            
            add(nums[i])
            
            result.append(getMedian())
            
        return result