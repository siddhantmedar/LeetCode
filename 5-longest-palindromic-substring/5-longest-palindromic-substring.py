class Solution:
    def longestPalindrome(self, strs: str) -> str:
        def check(l,r):
            while l>=0 and r<len(strs)  and strs[l] == strs[r]:
                l-=1
                r+=1
                
            l+=1
            r-=1
            
            return l,r
            
        mx = float("-inf")
        resi, resj = 0, 0
        
        for i in range(len(strs)):
            s,e = check(i,i)
            
            if e-s+1 > mx:
                mx = e-s+1
                resi, resj = s,e
            
            if i+1 < len(strs):
                s,e = check(i,i+1)

                if e-s+1 > mx:
                    mx = e-s+1
                    resi,resj = s,e
                    
        return strs[resi:resj+1]