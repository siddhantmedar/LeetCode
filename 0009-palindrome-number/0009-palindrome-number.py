class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        rev = 0
        
        def solve(n):
            if n>0:
                nonlocal rev
                rev = rev*10+(n%10)
                solve(n//10)
        
        solve(x)
        
        return rev==x