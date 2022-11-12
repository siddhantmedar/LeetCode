class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mp = dict()
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
            
        for c in t:
            if c in mp:
                mp[c]-=1
                
                if mp[c] == 0:
                    del mp[c]
            else:
                mp[c] = 1+mp.get(c,0)
                    
        return len(mp) == 0