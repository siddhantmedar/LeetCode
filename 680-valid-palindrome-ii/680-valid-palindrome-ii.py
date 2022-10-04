class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalin(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                
                start+=1
                end-=1
                
            return True
        
        start, end = 0, len(s)-1
        
        while start <= end:
            if s[start] == s[end]:
                start+=1
                end-=1
                
            else:
                if isPalin(start+1, end) or isPalin(start, end-1):
                    return True
                else:
                    return False
                
        return True