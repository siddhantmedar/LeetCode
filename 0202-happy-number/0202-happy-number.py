class Solution:
    def isHappy(self, n: int) -> bool:
        def sod(n):
            res = 0
            
            while n:
                res+=(n%10)**2
                
                n//=10
                
            return res
        
        seen = set()
        
        while True:
            n = sod(n)
            if n in seen or n==1:
                break
            seen.add(n)
            
        return True if n==1 else False