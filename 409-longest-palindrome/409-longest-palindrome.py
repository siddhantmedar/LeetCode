class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
            
        odd = False
        
        sm = 0
        
        for k,v in mp.items():
            if v%2:
                odd = True
                sm+=(v-1)
                
            else:
                sm+=v
                
        return sm+1 if odd else sm