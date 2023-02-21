class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = {}
        
        for c in magazine:
            mp[c] = 1+mp.get(c,0)
            
        for c in ransomNote:
            if c not in mp:
                return False
            
            else:
                mp[c]-=1
                
                if mp[c]==0:
                    del mp[c]
                    
        return True