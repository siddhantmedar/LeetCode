class Solution:
    def myPow(self, a: float, b: int) -> float:
        def solve(b):
            if b == 1:
                return a
            
            elif b == 0:
                return 1
            
            res = solve(b//2)
            
            if b%2 == 0:
                return res*res
            else:
                return a*res*res
            
        flag = False
        
        if b < 0:
            flag = True
            b = abs(b)
        
        if flag:
            return 1/solve(b)
        
        else:
            return solve(b)