class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {x:0 for x in s}
        
        for c in s:
            mp[c]+=1
            
        bucket = [[] for i in range(len(s)+1)]
        
        for k,v in mp.items():
            bucket[v].append(k)
            
        res = ""
        for i in range(len(bucket)-1,-1,-1):
            b = bucket[i]
            
            if b:
                for ele in b:
                    res+=(i*ele)
                    
        return res