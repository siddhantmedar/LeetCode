class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(a,n):
            if n == 0:
                return 1
            
            res = solve(a,n//2)
            
            if n%2 == 0:
                return res*res
            
            else:
                return res*res*a
            
        if n < 0:
            n*=-1
            return 1/solve(x, abs(n))
        
        else:
            return solve(x,n)