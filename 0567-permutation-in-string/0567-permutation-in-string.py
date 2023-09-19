class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        if len(p) > len(s):
            return False
        
        mp = dict()
        ref  = dict()
        
        for c in p:
            ref[c]=1+ref.get(c,0)
        
        k = len(p)
        i = 0
        
        for i in range(k):
            mp[s[i]]=1+mp.get(s[i],0)
            
        if ref==mp:
            return True
            
        for i in range(k,len(s)):
            mp[s[i-k]]-=1
            
            if mp[s[i-k]]==0:
                del mp[s[i-k]]
            
            mp[s[i]]=1+mp.get(s[i],0)
            
            if mp==ref:
                return True
        
        return False