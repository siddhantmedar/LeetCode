class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mp = {chr(i):(0,0) for i in range(97,123)}
        
        for c in s:
            c1,c2 = mp[c]
            mp[c] = (c1+1,c2)
            
        for c in t:
            c1,c2 = mp[c]
            mp[c] = (c1,c2+1)
        
        res = 0
        
        for k,v in mp.items():
            res+=abs(v[0]-v[1])
        
        return res