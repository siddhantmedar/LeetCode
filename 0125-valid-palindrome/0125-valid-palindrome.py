class Solution:
    def isPalindrome(self, t: str) -> bool:
        
        t = [c.lower() for c in t if c.isalnum()]
        
        s,e = 0,len(t)-1

        while s < e:
            if t[s] == t[e]:
                s+=1
                e-=1
            else:
                return False
            
        return True
        
        