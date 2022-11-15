class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(x,n):
            if n == 1:
                return x
            
            if n == 0:
                return 1
            
            res = solve(x,n//2)
            
            if n%2:
                return x*res*res
            
            else:
                return res*res
        
        
        if n<0:
            n*=-1
            return 1/solve(x,n)
        
        return solve(x,n)