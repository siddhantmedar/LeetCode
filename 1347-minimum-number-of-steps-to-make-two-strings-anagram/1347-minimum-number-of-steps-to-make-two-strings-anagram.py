class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mp = {}
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
            
        for c in t:
            if c in mp:
                mp[c]-=1
                if not mp[c]:
                    del mp[c]
                    
        return sum([x for _, x in mp.items()])