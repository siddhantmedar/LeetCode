class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele,0)
            
        heap = [(-v,k) for k,v in mp.items()]
        heapq.heapify(heap)
        
        result = []
        
        for _ in range(k):
            v,k = heapq.heappop(heap)
            
            result.append(k)
            
        return result