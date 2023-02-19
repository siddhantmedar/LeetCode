class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        
        for c in s:
            if c.isalnum():
                t+=c.lower()
          
        # print(t)
        
        low, high = 0, len(t)-1
        
        while low<high:
            if t[low] != t[high]:
                return False
            
            low+=1
            high-=1
            
        return True