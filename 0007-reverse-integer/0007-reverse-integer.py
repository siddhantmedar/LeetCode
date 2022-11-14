class Solution:
    def reverse(self, x: int) -> int:
        def solve(n):
            nonlocal result
            
            if n > 0:
                result = result*10+(n%10)
                solve(n//10)

        
        neg = False
        
        if x < 0:
            x*=-1
            neg = True
            
        result = 0
        
        solve(x)
        
        if not -2**31<=result<=2**31-1:
            return 0
        
        return -1*result if neg else result