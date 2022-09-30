class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = defaultdict()
        
        for word in words:
            mp[word] = 1+mp.get(word, 0)
            
        heap = [(-v,k) for k,v in mp.items()]
        
        heapq.heapify(heap)
        
        result = []
        
        while k:
            result.append(heapq.heappop(heap)[1])
            k-=1
            
        return result