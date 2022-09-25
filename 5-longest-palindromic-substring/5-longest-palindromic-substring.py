class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            
            l+=1
            r-=1
            
            return l,r
        
        mx = 0
        l,r = None, None
        
        for i in range(len(s)):
            start, end = check(i,i)
            
            if end-start+1 > mx:
                mx = end-start+1
                l,r = start, end
            
            if i+1 < len(s):
                start, end = check(i,i+1)

                if end-start+1 > mx:
                    mx = end-start+1
                    l,r = start, end
        
        return s[l:r+1]