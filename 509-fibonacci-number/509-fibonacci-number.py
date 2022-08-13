class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        x = 0
        y = 1
        
        for i in range(2, n+1):
            res = x+y
            x = y
            y = res
            
        return y