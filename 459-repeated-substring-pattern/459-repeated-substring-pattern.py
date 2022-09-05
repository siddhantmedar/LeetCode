class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def check(patt):
            tmp = ""
            
            while len(tmp) < len(s):
                tmp+=patt
            
            return True if tmp == s else False
            
        patt = ""
        
        for c in s[:-1]:
            patt+=c
            
            if check(patt):
                return True
            
        return False