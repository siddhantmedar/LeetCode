class Solution:
    def isPalindrome(self, x: int) -> bool:
        def rev(n):
            nonlocal s
            
            if n > 0:
                s+=str(n%10)
                rev(n//10)
            
        if x < 0:
            return False
        
        if x == 0:
            return True
        
        s=""
        
        rev(x)
        
        return int(s) == x
        