class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        mp = dict()
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
            
        for c in t:
            if c not in mp or (c in mp and mp[c] == 0):
                return False
            
            mp[c]-=1
            
            if mp[c] == 0:
                del mp[c]
        
        # print(mp)
        
        return True if not mp else False