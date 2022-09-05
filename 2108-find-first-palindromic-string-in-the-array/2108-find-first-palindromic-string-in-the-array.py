class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalin(w):
            start, end = 0, len(w)-1
            
            while start<=end:
                if w[start] != w[end]:
                    return False
                start+=1
                end-=1
                
            return True
        
        for w in words:
            if isPalin(w):
                return w
            
        return ""