class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def add(ele):
            heapq.heappush(mx_heap, -1*ele)
            
            heapq.heappush(mn_heap, -1*heapq.heappop(mx_heap))
        
            while len(mn_heap) > len(mx_heap):
                heapq.heappush(mx_heap, -1*heapq.heappop(mn_heap))
            
        def median():
            if len(mx_heap) == len(mn_heap):
                return ((mx_heap[0]*-1) + (mn_heap[0])) / 2
            
            elif len(mx_heap) > len(mn_heap):
                return mx_heap[0]*-1
            
        def updateHeap(ele):
            if -1*mx_heap[0] >= ele and -1*ele in mx_heap:
                mx_heap.remove(-1*ele)
                heapq.heapify(mx_heap)
            else:
                mn_heap.remove(ele)
                heapq.heapify(mn_heap)
        
        mx_heap, mn_heap = list(), list()
        
        result = []
        
        for i, ele in enumerate(nums):
            if len(mx_heap) + len(mn_heap) < k:
                add(ele)
                
            if len(mx_heap) + len(mn_heap) == k:
                result.append(median())
                
                updateHeap(nums[i-k+1])
                
        return result