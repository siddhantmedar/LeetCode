class Solution:
    def topKFrequent(self, words: List[str], K: int) -> List[str]:
        mp = {}
        
        for w in words:
            mp[w]=1+mp.get(w,0)
        
        heap = []
        
        for k, v in mp.items():
            heapq.heappush(heap,(-v,k))
            
        res = []
        
        while K:
            res.append(heapq.heappop(heap)[1]*1)
            K-=1
            
        return res