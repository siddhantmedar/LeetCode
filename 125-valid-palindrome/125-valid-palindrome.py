class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        
        for c in s:
            if c.isalnum():
                t+=c.lower()
        
        start, end = 0, len(t)-1
        
        while start <= end:
            if t[start] != t[end]:
                return False
            
            start+=1
            end-=1
            
        return True
        