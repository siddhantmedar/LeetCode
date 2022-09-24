class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = defaultdict()
        
        for c in s:
            mp[c] = 1+mp.get(c, 0)
        
        for c in t:
            if c not in mp:
                return False
            
            else:
                mp[c]-=1
                
        for k,v in mp.items():
            if v != 0:
                return False
            
        return True