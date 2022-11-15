class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
            
        res = 0
        odd = False
        
        for k,v in mp.items():
            if v%2:
                res+=(v-1)
                odd = True
                
            else:
                res+=v
                
        return res if not odd else res+1