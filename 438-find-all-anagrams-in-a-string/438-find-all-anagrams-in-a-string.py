class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        result = []
        
        ref = {}
        mp = {}
        
        k = len(p)
        
        for i,c in enumerate(p):
            ref[c] = 1+ref.get(c,0)
            
        for i in range(k):
            mp[s[i]] = 1+mp.get(s[i],0)
            
        if ref == mp:
            result.append(0)
        
        for i in range(k, len(s)):
            print(i, s[i-k], s[i])
            mp[s[i-k]]-=1
            
            if mp[s[i-k]] == 0:
                del mp[s[i-k]]
                
            mp[s[i]] = 1+mp.get(s[i],0)
            
            if ref == mp:
                result.append(i-k+1)
                
        return result
    
        # c b a e b a b a c d
        # 0 1 2 3 4 5 6 7 8 9