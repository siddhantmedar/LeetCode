class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        def solve(n):
            nonlocal res
            
            if n>0:
                res = res*10+(n%10)
                solve(n//10)
                
        res = 0
        
        solve(x)
        
        return x == res