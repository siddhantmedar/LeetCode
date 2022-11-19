class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        ref = {}
        
        for c in s1:
            ref[c] = 1+ref.get(c,0)
        
        mp = {}
        
        for i,c in enumerate(s2[:len(s1)]):
            mp[c] = 1+mp.get(c,0)
            
        if ref == mp:
            return True
        
        i=0
        for j,c in enumerate(s2[len(s1):]):
            mp[s2[j-i]]-=1
            
            if mp[s2[j-i]] == 0:
                del mp[s2[j-i]]
            
            mp[c] = 1+mp.get(c,0)
            
            if mp == ref:
                return True
            
        
        return False           