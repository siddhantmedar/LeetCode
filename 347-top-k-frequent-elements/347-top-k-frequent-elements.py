class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict()
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele, 0)
            
        heap = [(-v,k) for k,v in mp.items()]
        
        heapq.heapify(heap)
        
        result = []
        
        while k:
            val, key = heapq.heappop(heap)
            result.append(key)
            k-=1
            
        return result