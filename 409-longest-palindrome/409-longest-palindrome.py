class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = False
        
        mp = {}
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
            
        sm = 0
        
        for k,v in mp.items():
            if v%2 == 0:
                sm+=v
                
            else:
                odd = True
                sm+=(v-1)
                    
        return sm+1 if odd else sm