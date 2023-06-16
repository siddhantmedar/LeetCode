class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        i,j = len(t)-1, len(s)-1
        
        while i>=0 and j>=0:
            if t[i]==s[j]:
                j-=1
                
            i-=1
        
        print(i,j)
        return True if j<0 else False