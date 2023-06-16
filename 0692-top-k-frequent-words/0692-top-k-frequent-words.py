class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = dict()
        
        for ele in words:
            mp[ele] = 1+mp.get(ele,0)
        
        heap = []
        
        for key,val in mp.items():
            heap.append((-val,key))
            
        heapq.heapify(heap)
        
        res = []
        
        while k:
            res.append(heapq.heappop(heap)[1])
            k-=1
        
        return res
    
        # nlogn ok
        # n+klogn