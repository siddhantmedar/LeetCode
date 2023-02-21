class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}
        for c in s:
            mp[c]=1+mp.get(c,0)
            
        odd = False
        res=0
        
        for k,v in mp.items():
            if v%2==0:
                res+=v
            else:
                res+=(v-1)
                if not odd:
                    odd = True
                    
        return res if not odd else res+1