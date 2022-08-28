class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        
        for c in s:
            if 65<=ord(c)<=90:
                res+=chr(ord(c)+32)
                
            else:
                res+=c
                
        return res