class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
        
        heap = [(-v,k) for k,v in mp.items()]
        
        heapq.heapify(heap)
        
        result = ""
        
        while heap:
            v,k = heapq.heappop(heap)
            v*=-1
            
            result+=k*v
        
        return result
    
    
        # bucket
        # heap    