class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isPalin(x):
            start, end = 0, len(x)-1
            
            while start <= end:
                if x[start] != x[end]:
                    return False
                start+=1
                end-=1
                
            return True
            
        res = ""
        
        for c in s:
            if c.isalnum():
                res+=c.lower()
                
        return isPalin(res)