class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = {}
        
        for w in words:
            mp[w]=1+mp.get(w,0)
            
        res = sorted(mp.items(),key=lambda x:(-x[1],x[0]))
        
        return [x[0] for x in res][:k]