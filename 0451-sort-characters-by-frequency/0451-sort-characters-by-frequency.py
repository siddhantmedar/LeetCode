class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
            
        mp = dict(sorted(mp.items(), key=lambda x:-x[1]))
        
        result = ""
        
        for k,v in mp.items():
            while v:
                result+=k
                v-=1
                
        return result