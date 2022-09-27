class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        heap = []
        
        mp = {}
        
        for ele in nums:
            mp[ele] = 1 + mp.get(ele, 0)
            
        for k,v in mp.items():
            heapq.heappush(heap, (-v, k))
            
        heapq.heapify(heap)
        
        result = []
        
        while K:
            result.append(heapq.heappop(heap)[1])
            K-=1
            
        return result