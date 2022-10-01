class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
        
        bucket = [[] for _ in range(len(s)+1)]
            
        for k,v in mp.items():
            count = v
            while count:
                bucket[v].append(k)
                count-=1
            
        result = ""
        
        for i in range(len(bucket)-1,-1,-1):
            b = bucket[i]
            
            if b:
                result+="".join(b)
            
        return result