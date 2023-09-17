class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        mp = Counter(nums)
        
        lst = [(-v,k) for k,v in mp.items()]
        
        heapq.heapify(lst)
        
        result = []
        
        while K:
            result.append(heapq.heappop(lst)[1])
            K-=1
            
        return result