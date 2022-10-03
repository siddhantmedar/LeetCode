class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        ref, mp = dict(), dict()
        k = len(s1)
        
        for c in s1:
            ref[c] = 1+ref.get(c,0)
            
        for i, ele in enumerate(s2[:k]):
            mp[ele] = 1+mp.get(ele, 0)
        
        if ref == mp:
            return True
        
        for i in range(k,len(s2)):
            mp[s2[i-k]]-=1
            
            if mp[s2[i-k]] == 0:
                del mp[s2[i-k]]
                
            mp[s2[i]] = 1+mp.get(s2[i], 0)
            
            if mp == ref:
                return True 
            
        return False