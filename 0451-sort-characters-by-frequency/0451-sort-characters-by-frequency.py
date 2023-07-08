class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}
        
        for c in s:
            mp[c]=1+mp.get(c,0)
            
        mp = sorted(mp.items(),key=lambda x:(-x[1]))
        
        res = ""
        
        for k,v in mp:
            while v:
                res+=k
                v-=1
                
        return res