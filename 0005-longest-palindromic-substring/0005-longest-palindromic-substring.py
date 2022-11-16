class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l,r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                    l-=1
                    r+=1
            
            l+=1
            r-=1
            
            return [l,r]
        
        best = 0
        res = None
        
        for i in range(len(s)):
            l,r = check(i,i)
            
            if r-l+1 > best:
                best = r-l+1
                res = s[l:r+1]
                
            l,r = check(i,i+1)
            
            if r-l+1 > best:
                best = r-l+1
                res = s[l:r+1]
        
        return res
            