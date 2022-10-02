class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(a,n):
            if n == 0:
                return 1
            
            elif n == 1:
                return a
            
            if n%2 == 0:
                res = solve(a,n//2)
                return res*res
            
            elif n%2 == 1:
                res = solve(a,(n-1)//2)
                return res*res*a
            
        if n < 0:
            n*=-1
            return 1/solve(x, abs(n))
        
        else:
            return solve(x,n)