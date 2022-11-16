class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def add(ele):
            heapq.heappush(mx,-ele)
            heapq.heappush(mn, -heapq.heappop(mx))
            
            while len(mn) > len(mx):
                heapq.heappush(mx, -heapq.heappop(mn))
            
        def median():
            if len(mx) > len(mn):
                return -mx[0]
            else:
                return (-mx[0]+mn[0])/2
            
        def update(ele):
            if -mx[0] >= ele:
                mx.remove(-ele)
                heapq.heapify(mx)
            else:
                mn.remove(ele)
                heapq.heapify(mn)
        
        mx, mn, res = [], [], []
        
        for i in range(k):
            add(nums[i])
            
        res.append(median())
        
        for i in range(k, len(nums)):
            update(nums[i-k])
            add(nums[i])
            res.append(median())
            
        return res