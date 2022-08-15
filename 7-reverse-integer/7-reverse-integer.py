class Solution:
    def reverse(self, n: int) -> int:
        def rev(n):
            nonlocal res
            
            if n > 0:
                res = res*10 + n%10
                rev(n//10)
                
        
        res = 0
        neg = False
        
        if n < 0:
            n*=-1
            neg = True    
        
        rev(n)
        
        if neg:
            res*=-1
        
        if -2**31<=res<=2**31-1:
            return res
        
        return 0