class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def product(n):
            res = 1
            
            while n:
                res*=n%10
                n//=10
                
            return res
        
        def acc(n):
            res = 0
            
            while n:
                res+=n%10
                n//=10
                
            return res
        
        return product(n)-acc(n)