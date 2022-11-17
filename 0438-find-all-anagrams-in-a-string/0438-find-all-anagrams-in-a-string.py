class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        k = len(p)
        result = []
        
        ref = {}
        
        for c in p:
            ref[c] = 1+ref.get(c,0)
        
        mp = {}
        
        for c in s[:k]:
            mp[c] = 1+mp.get(c,0)
            
        if mp == ref:
            result.append(0)
            
        for i in range(k,len(s)):
            mp[s[i-k]]-=1
            
            if mp[s[i-k]] == 0:
                del mp[s[i-k]]
                
            mp[s[i]] = 1+mp.get(s[i],0)
            
            if ref == mp:
                result.append(i-k+1)
                
        return result