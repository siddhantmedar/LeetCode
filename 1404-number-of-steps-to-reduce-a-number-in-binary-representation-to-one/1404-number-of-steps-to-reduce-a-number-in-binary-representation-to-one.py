class Solution:
    def numSteps(self, s: str) -> int:
        def solve(n):
            if n == 1:
                return 0
            
            if n%2 == 0:
                return 1 + solve(n//2)
            
            else:
                return 1 + solve(n+1)
        
            
        n = 0
        
        pow = 0
        
        for i in range(len(s)-1,-1,-1):
            n+=int(s[i])*(2**pow)
            
            pow+=1
            
        return solve(n)