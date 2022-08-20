class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        
        a = 1
        b = 1
        
        for i in range(2, n+1):
            res = a+b
            
            a = b
            b = res
            
        return b