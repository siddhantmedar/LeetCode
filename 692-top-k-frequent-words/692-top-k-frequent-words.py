class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = defaultdict()
        
        for word in words:
            mp[word] = 1+mp.get(word, 0)
            
        tmp = sorted(mp.items(), key=lambda x:(-x[1],x[0]))
        
        result = []
        
        for i in range(k):
            result.append(tmp[i][0])
            
        return result