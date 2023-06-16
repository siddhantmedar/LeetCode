class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = dict()
        
        for ele in words:
            mp[ele] = 1+mp.get(ele,0)
            
        lst = sorted(mp.items(),key=lambda x:(-x[1],x[0]))
        
        return [x[0] for x in lst][:k]
        # nlogn
        # n+klogn