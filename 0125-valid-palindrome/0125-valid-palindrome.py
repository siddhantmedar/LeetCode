class Solution:
    def isPalindrome(self, s: str) -> bool:
        def pal(txt):
            s,e = 0, len(txt)-1
            
            while s<=e:
                if txt[s]!=txt[e]:
                    return False
                s+=1
                e-=1
                
            return True
            
            
        txt = ""
        
        for c in s:
            if c.isalnum():
                txt+=c.lower()
                
        return pal(txt)